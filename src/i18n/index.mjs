// Per-language site settings, used by astro.config.mjs.
//
// Each src/i18n/<lang>.json adds one language:
//   {
//     "label": "Deutsch",            // name shown in the language picker
//     "lang": "de",                  // BCP-47 tag for <html lang>
//     "groups": { "Basic Use": "Grundlagen" },        // sidebar group label -> translation
//     "pages":  { "basic-use/title": "Titel" }        // sidebar page slug   -> translation
//   }
// The file name (without .json) is the URL prefix: de.json -> /de/.
// Missing labels fall back to English.

import { readdirSync, readFileSync } from 'node:fs';

const dir = new URL('./', import.meta.url);

/** Load every src/i18n/<lang>.json, sorted by code. */
export function loadLanguages() {
  return readdirSync(dir)
    .filter((f) => f.endsWith('.json'))
    .sort()
    .map((f) => ({ code: f.slice(0, -5), ...JSON.parse(readFileSync(new URL(f, dir), 'utf8')) }));
}

/** Starlight `locales` option: English at the root plus one entry per language file. */
export function buildLocales(languages) {
  const locales = { root: { label: 'English', lang: 'en' } };
  for (const { code, label, lang } of languages) locales[code] = { label, lang: lang ?? code };
  return locales;
}

/**
 * Return a copy of the sidebar with `translations` filled in from the language files.
 * Logs a warning for any key that matches no sidebar entry (a typo, or a renamed slug or group).
 */
export function localizeSidebar(sidebar, languages) {
  const used = new Set();

  const walk = (entries) =>
    entries.map((entry) => {
      if (typeof entry === 'string' || !entry.label) return entry;
      const isGroup = Array.isArray(entry.items);
      const key = isGroup ? entry.label : entry.slug;
      const translations = { ...entry.translations };
      for (const { code, groups = {}, pages = {} } of languages) {
        const label = (isGroup ? groups : pages)[key];
        if (label) {
          translations[code] = label;
          used.add(`${code}:${isGroup ? 'groups' : 'pages'}:${key}`);
        }
      }
      const out = { ...entry };
      if (Object.keys(translations).length) out.translations = translations;
      if (isGroup) out.items = walk(entry.items);
      return out;
    });

  const result = walk(sidebar);

  for (const { code, groups = {}, pages = {} } of languages) {
    for (const [kind, map] of [['groups', groups], ['pages', pages]]) {
      for (const key of Object.keys(map)) {
        if (!used.has(`${code}:${kind}:${key}`)) {
          console.warn(`[i18n] src/i18n/${code}.json: "${kind}.${key}" matches no sidebar entry`);
        }
      }
    }
  }
  return result;
}
