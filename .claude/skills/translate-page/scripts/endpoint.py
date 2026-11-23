#!/usr/bin/env python3
"""Manage where the translation model runs.

Endpoints are saved per user (not in the repo), because which machine runs the
model, and whether it's reachable, depends on where you are working. One endpoint
is "current"; translate_page.py uses it unless told otherwise.

Usage:
  endpoint.py show                       current endpoint, or exit 3 if none is set
  endpoint.py list                       all saved endpoints
  endpoint.py add NAME --url URL [--model M] [--key-env VAR] [--use] [--force]
  endpoint.py use NAME                   make NAME the current endpoint
  endpoint.py remove NAME
  endpoint.py test [NAME]                send a one-line translation to check it works

URL is the full OpenAI-compatible chat completions URL, e.g.
  Open WebUI   http://host:3000/api/chat/completions   (needs an API key)
  Ollama       http://host:11434/v1/chat/completions   (no key)
  LM Studio    http://host:1234/v1/chat/completions    (no key)

--key-env names the environment variable that holds the API key. The key itself
is never saved. If the variable isn't set, it is read from your zsh/bash startup files.

Config file: $TRANSLATE_CONFIG, else $XDG_CONFIG_HOME/swiftdialog-docs/translate.json,
else ~/.config/swiftdialog-docs/translate.json.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request
from pathlib import Path

DEFAULT_MODEL = "translategemma:12b"
NOT_CONFIGURED = 3  # exit code when no endpoint is set up yet


class EndpointError(Exception):
    pass


def config_path():
    if os.environ.get("TRANSLATE_CONFIG"):
        return Path(os.environ["TRANSLATE_CONFIG"]).expanduser()
    base = Path(os.environ.get("XDG_CONFIG_HOME") or Path.home() / ".config")
    return base / "swiftdialog-docs" / "translate.json"


def load():
    p = config_path()
    if not p.exists():
        return {"current": None, "endpoints": {}}
    cfg = json.loads(p.read_text(encoding="utf-8"))
    cfg.setdefault("current", None)
    cfg.setdefault("endpoints", {})
    return cfg


def save(cfg):
    p = config_path()
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(cfg, indent=2) + "\n", encoding="utf-8")


def resolve(name=None):
    """Return the endpoint to use as a dict with name, url, model, key_env.

    Order: the named endpoint, else the current one. TRANSLATE_API_URL and
    TRANSLATE_MODEL override the saved values (handy for one-off runs).
    """
    cfg = load()
    name = name or cfg["current"]
    ep = {}
    if name:
        if name not in cfg["endpoints"]:
            raise EndpointError("no saved endpoint named %r (saved: %s)"
                                % (name, ", ".join(cfg["endpoints"]) or "none"))
        ep = dict(cfg["endpoints"][name], name=name)
    if os.environ.get("TRANSLATE_API_URL"):
        ep["url"] = os.environ["TRANSLATE_API_URL"]
        ep.setdefault("name", "(TRANSLATE_API_URL)")
    if os.environ.get("TRANSLATE_MODEL"):
        ep["model"] = os.environ["TRANSLATE_MODEL"]
    if not ep.get("url"):
        raise EndpointError("no translation endpoint is set up. Add one with:\n"
                            "  endpoint.py add NAME --url URL [--key-env VAR] --use")
    ep.setdefault("model", DEFAULT_MODEL)
    ep.setdefault("key_env", None)
    return ep


def api_key(ep):
    """Return the key from ep's key_env variable, or from the user's shell startup files. '' if none."""
    var = ep.get("key_env")
    if not var:
        return ""
    if os.environ.get(var):
        return os.environ[var]
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", var):
        raise EndpointError("key_env %r is not a valid environment variable name" % var)
    # Agents often run in a shell that hasn't loaded ~/.zshrc, so ask an interactive
    # login shell. Markers separate the value from anything the startup files print.
    shell = os.environ.get("SHELL", "/bin/zsh")
    if os.path.basename(shell) not in ("zsh", "bash"):
        shell = "/bin/zsh"
    try:
        r = subprocess.run([shell, "-ilc", 'printf "\\n@@KEY@@%%s@@END@@\\n" "${%s}"' % var],
                           stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.TimeoutExpired):
        return ""
    m = re.search(r"@@KEY@@(.*?)@@END@@", r.stdout)
    return m.group(1) if m else ""


def post_json(url, payload, key, timeout=300):
    """POST payload as JSON and return the decoded response.

    Tries urllib first, then falls back to curl. On macOS, Local Network privacy
    (and some sandboxes) can block LAN connections from python3 while allowing
    /usr/bin/curl, so the fallback keeps things working in those environments.
    """
    body = json.dumps(payload).encode()
    headers = {"Content-Type": "application/json"}
    if key:
        headers["Authorization"] = "Bearer " + key
    try:
        with urllib.request.urlopen(urllib.request.Request(url, data=body, headers=headers),
                                    timeout=timeout) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        # The server answered, so the network is fine; curl won't do better.
        raise EndpointError("HTTP %s from %s: %s" % (e.code, url, e.read()[:200].decode(errors="replace")))
    except (urllib.error.URLError, OSError) as first:
        py_err = first
    # Headers go through a config file on stdin so the key never appears in `ps`.
    conf = "".join('header = "%s: %s"\n' % kv for kv in headers.items())
    with tempfile.NamedTemporaryFile(suffix=".json") as f:
        f.write(body)
        f.flush()
        try:
            r = subprocess.run(["curl", "-sS", "--fail-with-body", "--connect-timeout", "10",
                                "-m", str(timeout), "-K", "-",
                                "--data-binary", "@" + f.name, url],
                               input=conf, capture_output=True, text=True, timeout=timeout + 10)
        except (OSError, subprocess.TimeoutExpired) as e:
            raise EndpointError("cannot reach %s (python: %s; curl: %s)" % (url, py_err, e))
    if r.returncode != 0:
        raise EndpointError("cannot reach %s (python: %s; curl: %s %s)"
                            % (url, py_err, r.stderr.strip()[:200], r.stdout[:200]))
    return json.loads(r.stdout)


def chat(ep, key, prompt, timeout=300, temperature=0):
    data = post_json(ep["url"], {"model": ep["model"], "temperature": temperature,
                                 "messages": [{"role": "user", "content": prompt}]}, key, timeout)
    try:
        return data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError):
        raise EndpointError("unexpected response from %s: %s" % (ep["url"], json.dumps(data)[:300]))


def describe(name, ep, current):
    key = ep.get("key_env") or "no key"
    return "%s %s  %s  model=%s  key=%s" % ("*" if name == current else " ", name, ep["url"],
                                           ep.get("model", DEFAULT_MODEL), key)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("show")
    sub.add_parser("list")
    a_add = sub.add_parser("add")
    a_add.add_argument("name")
    a_add.add_argument("--url", required=True)
    a_add.add_argument("--model", default=DEFAULT_MODEL)
    a_add.add_argument("--key-env", help="name of the env var holding the API key (omit if none)")
    a_add.add_argument("--use", action="store_true", help="also make it the current endpoint")
    a_add.add_argument("--force", action="store_true", help="replace an existing endpoint with this name")
    sub.add_parser("use").add_argument("name")
    sub.add_parser("remove").add_argument("name")
    sub.add_parser("test").add_argument("name", nargs="?")
    a = ap.parse_args()

    cfg = load()
    try:
        if a.cmd == "show":
            if not cfg["current"] and not os.environ.get("TRANSLATE_API_URL"):
                print("no translation endpoint is set up (config: %s)" % config_path(), file=sys.stderr)
                sys.exit(NOT_CONFIGURED)
            ep = resolve()
            print(describe(ep["name"], ep, ep["name"]))
        elif a.cmd == "list":
            if not cfg["endpoints"]:
                print("no saved endpoints (config: %s)" % config_path(), file=sys.stderr)
                sys.exit(NOT_CONFIGURED)
            for n, ep in cfg["endpoints"].items():
                print(describe(n, ep, cfg["current"]))
        elif a.cmd == "add":
            if not re.match(r"https?://", a.url):
                sys.exit("--url must start with http:// or https://")
            if a.name in cfg["endpoints"] and not a.force:
                sys.exit("an endpoint named %r already exists; pass --force to replace it" % a.name)
            cfg["endpoints"][a.name] = {"url": a.url, "model": a.model, "key_env": a.key_env}
            if a.use or not cfg["current"]:
                cfg["current"] = a.name
            save(cfg)
            print(describe(a.name, cfg["endpoints"][a.name], cfg["current"]))
        elif a.cmd == "use":
            if a.name not in cfg["endpoints"]:
                sys.exit("no saved endpoint named %r (saved: %s)" % (a.name, ", ".join(cfg["endpoints"]) or "none"))
            cfg["current"] = a.name
            save(cfg)
            print(describe(a.name, cfg["endpoints"][a.name], a.name))
        elif a.cmd == "remove":
            if cfg["endpoints"].pop(a.name, None) is None:
                sys.exit("no saved endpoint named %r" % a.name)
            if cfg["current"] == a.name:
                cfg["current"] = None
            save(cfg)
            print("removed %s%s" % (a.name, "; no current endpoint now" if not cfg["current"] else ""))
        elif a.cmd == "test":
            ep = resolve(a.name)
            key = api_key(ep)
            if ep.get("key_env") and not key:
                sys.exit("%s is not set in the environment or your shell startup files" % ep["key_env"])
            out = chat(ep, key, "Translate into German. Reply with the translation only:\n\nThe dialog has two buttons.",
                       timeout=120)
            print("OK %s (%s): %s" % (ep["name"], ep["model"], out.strip()))
    except EndpointError as e:
        sys.exit(str(e))


if __name__ == "__main__":
    main()
