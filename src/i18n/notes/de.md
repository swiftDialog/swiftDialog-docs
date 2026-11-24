# German (de) translation notes

## Style decisions

- **Register:** formal "Sie" throughout (as translated in November 2026). A reviewer has asked for informal "du"; see feedback below. Until that's decided, keep new pages consistent with the existing ones.
- Default button labels follow the app's German strings (`de.lproj`): "OK", "Abbrechen", "Mehr Informationen".
- Numbers users type keep the decimal point (`15.7`, never `15,7`): swiftDialog parameters are comma-separated.

### Apple reference (2026-11-25, partial)

Read: https://support.apple.com/de-de/guide/deployment/welcome/web, https://support.apple.com/de-de/guide/deployment/dep873c25ac4/web, https://support.apple.com/de-de/guide/terminal/welcome/mac, https://support.apple.com/de-de/guide/terminal/apdd100908f-06b3-4e63-8a87-32e71241bab4/mac, https://support.apple.com/de-de/guide/terminal/apdb66b5242-0d18-49fc-9c47-a2498b7c91d5/mac. Not yet read: the deployment glossary (https://support.apple.com/de-de/guide/deployment/depcfc7eb894cd/web) and a Terminal settings page, which should cover buttons, checkboxes, menus and Apple silicon.

Findings. These are proposals, not decisions yet:
- **du, lowercase**, on admin and end-user pages alike: "in deine Organisation integrieren", "Weitere Informationen findest du unter". "Sie" appears only in the site's feedback form.
- **Short active imperatives:** "Öffne die App „Terminal“", "Gib den Befehl *chmod* ein", "Drücke die Tastenkombination „Control-C“". Explanations use "Du kannst …, indem du …".
- **„…“ quotes** around UI and app names ("die Payload „Mitteilungen“"), not bold.
- **Hyphen after a brand or loanword** ("Mac-Computer", "Apple-Geräte", "Shell-Skripts", "Paket-ID"); purely German compounds are closed ("Geräteverwaltungsdienst").
- **Terms:** Richtlinie, Konfigurationsprofil, Paket (.pkg), Geräteregistrierung, Mitteilungen, Befehlszeile, Fenster. Return key: "Zeilenschalter". Apple writes "Geräteverwaltung" rather than "MDM"; we keep MDM, which is what admins say.
- Not observed: on-screen button, icon, checkbox, menu, Apple silicon, administrator.

## Notes for reviewers

None recorded. The German pages were translated before this file existed.

## Reviewer feedback

### 2026-11-25: native-speaker reviewer

> The first thing I notice is the use of the formal form of address ("Sie"). I prefer a more informal form of address ("Du"). Apple uses that, too. Otherwise, the text comes across as a bit "stiff." Still, it's better than nothing!

- Register "Sie" → "du": **open.** Apple's German documentation and UI do use "du". Switching means rewriting every German page (imperatives, pronouns, possessives), not a search-and-replace.
