---
title: Rythme cadencé contrôlé dans un déploiement MDM
description: Utilisez le type de pas "à cadence contrôlée" pour créer une interface de déploiement pilotée par des attributs, qui s'adapte en fonction de l'état réel du système. Cette solution est idéale pour les déploiements MDM utilisant des outils tels que Fleet, Jamf, Intune, et bien d'autres.
translationSynced: 2026-11-23T04:29:02+00:00
---

La fonction de pas à cadence contrôlée transforme un écran de déploiement en une séquence pilotée par des **attributs** : chaque message est affiché jusqu'à ce qu'une **condition réelle** soit remplie, puis il passe à l'étape suivante. Les conditions sont lues à partir de l'état réel du système, de sorte que l'écran n'affiche jamais le message "terminé" avant que ce ne soit réellement le cas.

Ceci est **indépendant de toute solution MDM (Mobile Device Management).** Les informations qu'il lit – les applications installées, les confirmations d'installation de paquets, et les **préférences gérées via mobileconfig sous `/Library/Managed Preferences/`** – sont générées de la même manière par **Fleet, Jamf, Intune, Mosyle, Kandji, Munki, Installomator**, et d'autres. Les exemples ci-dessous utilisent **Fleet** comme cas d'étude, mais rien n'est spécifique à Fleet.

## Comment cela s'intègre dans un plan de déploiement

Le système MDM effectue les tâches (installation de logiciels, déploiement de profils) ; swiftDialog les **surveille**.

| Tâche de déploiement | Attribut de cadence | Ce que cela dit |
|---|---|---|
| Application installée | `app` (`bundleId`) | `NSWorkspace.urlForApplication(withBundleIdentifier:)` |
| Paquet installé | `file` | reçu à `/var/db/receipts/<pkgid>.bom` |
| **Le fichier de configuration "profile" / "mobileconfig" a été intégré.** | **`managedpref`** (`domain`+`key`) | `/Library/Managed Preferences/<domain>.plist` (appareil) ou `…/<user>/<domain>.plist` |
| Configuration basée sur des scripts | `file` | un fichier de marque que le script modifie |
| Vérification non observable | `source:"ipc"` | Un script MDM utilise `cadence:satisfy:<id>` (osquery, les journaux d'Installomator, l'API MDM). |

**Entraînement hybride :** la plupart des entrées sont interrogées nativement (pas d'orchestrateur, fonctionne hors ligne ou à l'écran de connexion) ; quelques entrées `source:"ipc"` sont avancées par un script MDM pour ce qui ne peut pas être observé directement. Le verbe IPC est `cadence:satisfy:<id>` (aussi `advance` et `goto`).

`timeout` Dans le cas où une tâche ne se termine jamais, le système avance automatiquement à l'étape suivante, ce qui empêche une politique défaillante de bloquer l'interface utilisateur.

## Deux phases

Étant donné que la phase de connexion/l'assistant de configuration ne dispose **d'aucune session utilisateur** (aucune application utilisateur, seulement des paramètres gérés au niveau de l'appareil), utilisez deux configurations, sélectionnées par le lanceur en fonction de la session.

### Phase A : fenêtre de connexion / Assistant de configuration (uniquement au niveau de l'appareil).
```json
{
  "preset": "5", "stepType-note": "device phase",
  "introSteps": [{
    "id": "deploy", "stepType": "cadence", "title": "Setting up your Mac",
    "cadenceInterval": 1.0, "cadenceMinDwell": 0.6, "autoAdvance": true,
    "cadence": [
      { "id": "mdm",      "message": "Confirming management…", "sfSymbol": "checkmark.shield.fill",
        "attribute": { "type": "managedpref", "domain": "com.apple.mdm", "key": "AccessRights", "evaluation": "exists", "scope": "device" }, "timeout": 600 },
      { "id": "filevault","message": "Enabling disk encryption…", "sfSymbol": "lock.fill",
        "attribute": { "type": "managedpref", "domain": "com.apple.MCX.FileVault2", "key": "Enable", "evaluation": "equals", "expectedValue": "On", "scope": "device" }, "timeout": 900 },
      { "id": "rosetta",  "message": "Installing base packages…", "sfSymbol": "shippingbox.fill",
        "attribute": { "type": "file", "path": "/var/db/receipts/com.company.baseline.bom" }, "timeout": 900 }
    ]
  }]
}
```

### Phase B : environnement de bureau après la connexion (signaux complets).
```json
{
  "preset": "5",
  "introSteps": [{
    "id": "deploy", "stepType": "cadence", "title": "Installing your apps",
    "cadenceInterval": 0.5, "cadenceMinDwell": 0.6, "autoAdvance": true,
    "cadence": [
      { "id": "edge",    "message": "Installing Microsoft Edge…", "sfSymbol": "globe",
        "attribute": { "type": "app", "bundleId": "com.microsoft.edgemac" }, "timeout": 600 },
      { "id": "office",  "message": "Installing Office…", "sfSymbol": "doc.fill",
        "attribute": { "type": "app", "bundleId": "com.microsoft.Word" }, "timeout": 1200 },
      { "id": "vpn",     "message": "Applying VPN profile…", "sfSymbol": "network",
        "attribute": { "type": "managedpref", "domain": "com.company.vpn", "key": "Enabled", "evaluation": "boolean", "expectedValue": "true", "scope": "device" }, "timeout": 600 },
      { "id": "compliance","message": "Running compliance check…", "sfSymbol": "checkmark.seal.fill",
        "attribute": { "source": "ipc" }, "timeout": 600 }
    ]
  }]
}
```
L'entrée `compliance` est `source:"ipc"` : un script MDM effectue la vérification (via l'API osquery ou celle du fournisseur), puis `… ipc send "cadence:satisfy:compliance"`.

## Livraison (exemple de Fleet : même forme pour tout MDM).
1. **Contenu du paquet :** swiftDialog, le lanceur, et les deux fichiers JSON de Cadence.
2. **Profil (mobileconfig)** : configuration du lanceur, notamment les paramètres de configuration par session et les options de la fenêtre de connexion.
   (Le lanceur lit ses propres préférences gérées de la même manière — sous `/Library/Managed Preferences/`.)
3. **LaunchAgents** (appareil + fenêtre de connexion) pour démarrer swiftDialog dans la session appropriée.
4. **GitOps / politiques :** les profils et les logiciels que les passerelles de validation contrôlent, ainsi que le petit script qui...
   émet `cadence:satisfy` pour toute `source:"ipc"` entrée.

Générez les fichiers de configuration mobile (mobileconfig) et les éléments liés à GitOps à l'aide des outils `contour` / `fleet-gitops`, qui valident le profil par rapport au schéma d'Apple.

## Marque et revendications personnalisées pour chaque locataire, basées sur les préférences définies

Pour les déploiements multi-locataires, les **revendications de cadence** et la **couleur de la marque/de la teinte** peuvent être lues à partir d'un profil de préférences géré, plutôt que d'être codées en dur. Ainsi, chaque profil MDM de chaque locataire fournit ses propres valeurs, sans modifier la configuration livrée. Les deux utilisent un(e) `ManagedValueRef`:

| Clé | Type | Description |
|---|---|---|
| `domain` | Chaîne | Domaine de préférences géré, par exemple : `nl.root3.support` |
| `key` | Chaîne | La clé réside dans ce domaine (la valeur de luminosité pour les couleurs). |
| `darkKey` | Chaîne | Option de variation de couleur pour le mode sombre (couleurs uniquement). |

- `cadenceRef` — lit le tableau des paramètres de cadence (les `CadenceEntry` dictionnaires) à partir d'une préférence gérée, au lieu d'un `cadence` tableau intégré.
- `brandColorRef` — Lit la couleur de la marque/de la teinte (clair, avec l'option "foncé" facultative) à partir d'une préférence gérée.

```json
{
  "cadenceRef":    { "domain": "nl.root3.support", "key": "claims" },
  "brandColorRef": { "domain": "nl.root3.support", "key": "brandColor", "darkKey": "brandColorDark" }
}
```

Étant donné que les valeurs sont calculées à partir de `/Library/Managed Preferences/<domain>.plist`, elles présentent le même comportement que les attributs `managedpref` mentionnés ci-dessus, à savoir qu'elles sont mises à jour "instantanément dès que le profil est chargé".

<!-- REVIEW: cadenceRef / brandColorRef are documented as top-level keys (alongside the inline `cadence` array). Confirm this matches how they're consumed for all presets. -->

## Notes
- `managedpref` lit directement le fichier, ce qui signifie qu'il commence à fonctionner dès que le profil est chargé (aucune attente)
(pas de délai de mise en cache CFPreferences). `evaluation:"exists"` = "le profil est présent" ; `equals`/`boolean` = "une valeur spécifique est imposée".
- À l'étape de la fenêtre de connexion, seule la portée de l'appareil existe ; les préférences gérées au niveau utilisateur et les vérifications `app` relèvent de la phase B.
- En revenant à une séquence terminée (Retour), le système rejoue rapidement à `cadenceMinDwell` et s'arrête — il ne réévalue pas les conditions et ne se bloque pas.
