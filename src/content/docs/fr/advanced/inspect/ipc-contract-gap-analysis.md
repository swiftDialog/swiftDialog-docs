---
title: Analyse des écarts du contrat IPC
description: Une analyse comparative du contrat IPC entre swiftDialog et ignitecli, visant à identifier les lacunes constatées, les risques potentiels et les clauses contractuelles proposées afin de garantir une communication efficace entre les deux composants.
translationSynced: 2026-11-23T05:04:17+00:00
---

**Statut :** Projet soumis à révision. **Date :** 2026-06-17. **Portée :** Communication interprocessus (IPC) en temps réel entre `swiftDialog` (mode d'inspection, préréglages 1 à 6) et `ignitecli`, qui le lance et le contrôle. **Dépôts :**
- swiftDialog — `/Users/henry/Projects/GitHub/swiftDialog`
- ignitecli — `/Users/henry/Projects/GitHub/ignitecli-swift-private`

Ce document décrit l'accord IPC tel qu'il existe aujourd'hui, puis énumère les points où les deux parties sont d'accord par simple coïncidence, ou les points où une garantie est supposée mais n'est pas appliquée. Chaque affirmation est liée à une référence `file:line` afin qu'elle puisse être vérifiée à nouveau.

---

## 1. Aperçu des transports

Trois systèmes de transport sont en jeu. Le contrat englobe les trois systèmes ; une mise en œuvre efficace ne doit pas présumer que l'un d'entre eux est fiable.

| Transport | Direction | Canal / Parcours | Charge utile | Fiabilité |
|---|---|---|---|---|
| Notification (commande) distribuée. | ignitecli → dialogue | `com.swiftdialog.command` **et** `com.ignitecli.command` | `userInfo` dictionnaire, converti en chaîne de caractères | Envoi non garanti, sans ordre de priorité, **les messages sont perdus si ils sont envoyés avant que l'observateur ne s'enregistre** |
| Notification distribuée (événement). | swiftDialog → ignitecli | `com.swiftdialog.event` | `userInfo` dictionnaire comprenant `event` et `pid` | Effort maximal |
| Notification distribuée (accusé de réception). | swiftDialog → ignitecli | `com.swiftdialog.ack` | `userInfo` dictionnaire incluant `command`, `stepId`, `status`, `pid` | Effort maximal, **rarement utilisé** |
| Fichier de déclenchement / fichier de commande | ignitecli → swiftDialog | `--status-log-file` / `.command` par PID | Délimité par des sauts de ligne, avec des champs séparés par des deux-points | Robuste, avec suivi par décalage d'octets |
| Fichier de disponibilité | swiftDialog → ignitecli | `<trigger>.ready` ou configuration `readinessFile` | JSON | Robuste, interrogé par présence |
| Fichier d'événement | swiftDialog → ignitecli | configuration `eventFile` ou dérivé `.events` | JSONL | Robuste, lu en fin de fichier |
| Fichier de résultats | dialog → ignitecli | config `resultFile` / par processus `.result.json` | JSON | Durable |
| Répertoire des sessions publiées | swiftDialog → *(personne)* | `--published-sessions-dir` (par défaut `/private/tmp/swiftdialog/sessions/<pid>.json`) | JSON | Durable, **non consommé** — voir l'écart 1 |
| État de la communication interprocessus (IPC) de ignitecli | ignitecli → ignitecli | `/private/tmp/.ignitecli-ipc-<pid>.json` | JSON | Durable |

**Points d'ancrage**
- Canaux : `dialog/Views/Inspect/Core Framework/DistributedNotifications.swift:36` ;
  ignitecli `Sources/Dialog/ActionDispatcher.swift:9`.
- Publication sur les deux canaux : utilisez la commande `ignitecli` `Sources/Commands/IpcCommand.swift:414`.
- Routage des fichiers de commandes : `dialog/Views/Inspect/Core Framework/CommandRouter.swift:76`.
- Répertoire des sessions publiées : `dialog/Command Line/CommandLineArguments.swift:167`,
  `dialog/Views/Inspect/Core Framework/PresetCommonHelpers.swift:1134`.
- ignitecli état : `Sources/Dialog/IpcState.swift:11`.

---

## 2. Vocabulaire lié aux événements (le contrat de fourniture).

swiftDialog émet les types d'événements suivants (`DistributedNotifications.swift:36`, valeurs brutes verrouillées) :

| Type d'événement | Donnée brute | Émis(e) lorsque | Domaines clés |
|---|---|---|---|
| `ready` | `ready` | L'interface utilisateur est prête à recevoir les commandes | `triggerFile`, `preset?`, `itemCount?`, `items?`, `ackChannel` |
| `exit` | `exit` | Sur le point de se terminer | `triggerFile`, `exitCode?`, `completedCount?`, `failedCount?`, `resultFile?` |
| `deferred` | `defer` | Utilisateur en attente | `duration`, `seconds`, `exitCode`, `resultFile` |
| `button` | `button` | Clic de bouton | `stepId`, `button`, `action` |
| `step` | `step` | Transition d'étape | `stepId`, `action` (e.g. `completed`, `all_complete`) |
| `selection` | `selection` | Validation/vérification par sélection et regroupement | `key`, `values` |

Le préréglage 6 a confirmé l'émission de `step`, `button`, `selection` (`Preset6.swift:1251`, `:1116`, `:1638`).

Commandes acceptées (depuis ignitecli vers la boîte de dialogue), acheminées vers : `CommandRouter.swift:76–163`, `success`, `failure`, `warning`, `complete`, `navigate`/`goto`, `next`/`prev`/`back`, `reset`, `progress`, `update_guidance`, `update_message`, `batch_update`, `display_data`, `recheck`, `set`, `item`, `listitem`, `select`. Les raccourcis `userInfo` se développent en ces éléments (`DistributedNotifications.swift:177`).

---

## 3. Lacunes

Classés par ordre de gravité. Chaque point décrit la **réalité constatée**, le **risque** associé et une **clause contractuelle proposée** (formulation normative pour une future spécification commune).

### Gap 1 : Le répertoire des sessions publiées est configuré en mode écriture seule ; l'outil ignitecli ne peut jamais le lire. **URGENCE ÉLEVÉE**

**Observation.** swiftDialog crée un fichier de découverte par PID dans le répertoire `/private/tmp/swiftdialog/sessions/<pid>.json` (via l'interface graphique `PresetCommonHelpers.swift:1134` ou l'interface en ligne de commande `CommandLineArguments.swift:167`). Une recherche avec la commande "grep" dans tous les fichiers de `ignitecli` `Sources/` ne révèle **aucun lecteur** pour ce répertoire. `ignitecli` découvre les sessions uniquement via ses propres fichiers de configuration `/private/tmp/.ignitecli-ipc-<pid>.json` (`IpcState.swift:11`), qu'il a créés au démarrage.

Deux registres parallèles décrivent le même fait (indiquant quel dialogue est actif pour quel fichier déclencheur) et ne sont jamais synchronisés.

| Registre | swiftDialog rédige | ignitecli lit |
|---|---|---|
| `…/swiftdialog/sessions/<pid>.json` | swiftDialog écrit | ignitecli ne lit pas |
| `…/.ignitecli-ipc-<pid>.json` | ignitecli n'écrit pas | ignitecli lit |

**Risque.** L'outil ignitecli ne peut se connecter qu'à une fenêtre de dialogue qu'il a lui-même lancée. Si ignitecli perd son propre fichier de configuration (plantage, redémarrage, exécution séparée), la fenêtre de dialogue en cours ne peut pas être récupérée, même si swiftDialog l'annonce. La fonctionnalité de découverte récemment intégrée ne présente aucune valeur pour son seul utilisateur interne.

**Article proposé.**
> swiftDialog publiera un enregistrement de découverte par session en direct. ignitecli traitera le répertoire des sessions publiées comme la source d'information faisant autorité et pourra adopter une session trouvée dans ce répertoire (lire `triggerFile`, `resultFile`, `readinessFile`, `ackChannel`, `pid`) sans l'avoir lancée. Le fichier d'état privé de ignitecli peut rester un cache utilisé au lancement, mais ne doit pas être la seule source de vérité.

**Décision ouverte (propriétaire : ignitecli).** Le répertoire des sessions est-il destiné à la récupération par ignitecli, ou à des outils *externes* (surveillance/MDM) ? Ce choix détermine si ignitecli intègre une fonctionnalité de "découverte et adoption", ou si cela reste intentionnellement indépendant.

### Lacune 2 : Le chemin d'accès au fichier d'événement est déterminé par deux règles différentes. · **MODÉRÉ**

**Observé.** swiftDialog résout le chemin d'événement comme `config.eventFile ?? readinessFile(.ready → .events)` (`Preset5.swift:4834`, identique dans `Preset1.swift:460`, `Preset2.swift:533` et le préréglage 6). Les modèles ignitecli définissent toujours `eventFile` explicitement (`Sources/Resources/templates/*/config.json` → `/tmp/__WORKFLOW_NAME__.events`). Ils convergent uniquement parce que la configuration définit toujours cette clé.

**Risque.** Une configuration qui définit un chemin personnalisé et omet certains éléments fait que swiftDialog dérive un chemin que l'outil ignitecli ne surveille pas. `readinessFile` personnalisé et omet `eventFile`, swiftDialog dérive un chemin que ignitecli ne surveille pas. `wait-step` (interrogation toutes les 2 secondes) se bloque alors jusqu'à son expiration, sans indiquer le désaccord de chemin.

**Article proposé.**
> Le chemin d'accès au fichier d'événement DOIT être dérivé selon une seule et même règle, partagée par les deux parties. Si les deux extrémités dérivent le chemin (plutôt que d'exiger un `eventFile` explicite), l'algorithme de dérivation DOIT être spécifié ici textuellement et couvert par un test de chaque côté. Un délai d'attente de `wait-step` DOIT inclure le chemin d'accès au fichier d'événement résolu dans son erreur.

### Écart 3 : Les fonctions d'attente ne vérifient pas la vitalité du processus. · **SÉVÉRITÉ : MODÉRÉE**

**Observation.** `wait-exit` vérifie `kill(pid, 0)` (`IpcState.swift:58`) et constate un dialogue interrompu. `wait-ready` et `wait-step` attendent une notification ou une modification de fichier ; `wait-step` ne détecte un PID interrompu que si sa vérification initiale se déclenche, sinon, il attend le délai complet (`IpcCommand.swift` Étapes d'attente, `:376`).

**Risque.** Un dialogue qui se bloque au milieu de l'exécution transforme une erreur rapide et explicite en un délai d'attente générique de 2 à 600 secondes, sans indication de la cause.

**Article proposé.**
> Chaque serveur (`wait-ready`, `wait-step`, `wait-exit`) DOIT participer à un sondage sur `kill(pid,0)`
> la même fréquence que sa vérification de fichiers/notifications, et DOIT signaler rapidement toute erreur
> `dialog PID <n> exited before <condition>` plutôt qu'un délai d'attente générique.

### Lacune 4 : Un canal d'accusé de réception existe aux deux extrémités, mais il n'est pas utilisé comme une barrière. **MODÉRÉ**

**Observé.** swiftDialog publie des messages dans `com.swiftdialog.ack` après chaque commande exécutée (`CommandRouter.swift:351`). ignitecli possède `waitAck()` (`Sources/Dialog/DialogOrchestrator.swift:151`), mais la plupart des flux de travail ne l'utilisent jamais ; le mode de transmission par défaut est un envoi simple sans confirmation, en utilisant un mécanisme de transport optimisé au maximum.

**Risque.** Une notification `navigate` qui ne parvient pas et qui bloque une opération ultérieure de traitement par lots peut entraîner un dysfonctionnement silencieux de l'ensemble du processus. Les éléments d'interface utilisateur idempotents peuvent tolérer une perte de données, mais les commandes critiques pour l'ordre ne le peuvent pas.

**Article proposé.**
> Les commandes dont l'effet bloque l'exécution de commandes ultérieures (`navigate`, `goto`, `reset`, `batch_update` qui précède une navigation) DOIVENT être envoyées avec l'attente d'accusé de réception activée. ignitecli DOIT réessayer ou signaler une erreur si aucun accusé de réception pour une telle commande n'arrive dans le délai d'attente de l'ACK. Le mode « fire-and-forget » reste autorisé pour les peintures idempotentes (`progress`, `update_message`, `display_data`).

### Écart 5 : Correction de deux problèmes liés à la relecture de fichiers déclencheurs, non attribués à une équipe particulière. **FAIBLE à MOYENNE.**

**Observé.** L'outil ignitecli supprime les fichiers de communication interprocessus (IPC) avant le lancement (`DialogLauncher.swift:199`) afin d'empêcher la relecture de lignes obsolètes (`success:`) par swiftDialog (l'affichage rapide "preset-5"). swiftDialog enregistre indépendamment le décalage initial des octets pour ignorer le contenu existant (`CommandRouter.swift:79`). Deux corrections indépendantes protègent contre un même risque.

**Risque.** Si l'une de ces conditions se produit – soit swiftDialog relit les données à partir du décalage 0, soit ignitecli omet la phase de nettoyage sur un nouveau chemin – l'erreur se reproduit silencieusement.

**Article proposé.**
> swiftDialog ignorera tout le contenu du fichier de déclenchement présent avant qu'il ne publie `ready`. Cette garantie DOIT être détenue et testée côté swiftDialog ; le nettoyage avant lancement de ignitecli est une mesure de défense en profondeur, et non la garantie principale.

### Écart 6 : Aucune authentification sur aucun protocole de communication (acceptée, mais non explicitement mentionnée). · **FAIBLE**

**Observations.** Aucune validation de l'expéditeur pour les notifications distribuées (l'API ne fournit aucune information à ce sujet) ; le fichier de commande/déclencheur est accessible en écriture par tous les utilisateurs ; le répertoire des sessions est accessible en lecture et permet de lister son contenu. Tout processus local peut contrôler ou usurper la session, et peut lister les processus en cours ainsi que les chemins d'accès aux déclencheurs. Le nouveau répertoire des sessions *augmente* la surface de vulnérabilité.

**Risque.** Acceptable dans un modèle de confiance local utilisant un seul utilisateur ; dangereux si cette hypothèse est violée (serveur partagé, utilisateur secondaire avec des privilèges réduits).

**Article proposé.**
> La limite de confiance de l'IPC est définie comme étant "même utilisateur, même hôte, local". Tous les transports supposent un expéditeur local coopérant. Il s'agit d'une hypothèse délibérée et documentée ; aucun transport ne fournit d'authentification ni d'intégrité. Tout déploiement en dehors de cette limite est hors du champ d'application et non pris en charge.

---

## 4. Résumé de la gravité et ordonnancement

| # | Écart | Gravité | Emplacement de la correction |
|---|---|---|---|
| 1 | Sessions en écriture seule | ÉLEVÉ | ignitecli (lecteur) |
| 2 | Deux règles concernant les chemins d'événements | MOYEN | les deux (règle commune) |
| 3 | Fonctions d'attente sans vérification de vitalité | MOYEN | ignitecli |
| 4 | Accusé de réception non utilisé comme barrière | MOYEN | ignitecli (politique) |
| 5 | Relecture corrigée deux fois | FAIBLE–MOYEN | swiftDialog (détient la garantie) |
| 6 | Aucune authentification, non précisée | BAS | Documentation uniquement |

**Ordre de réalisation recommandé.** Commencez par implémenter ce contrat (les sections 5 et 6 ne concernent que la documentation et peuvent être réalisées immédiatement). Ensuite, intégrez **les sections 1 et 2 ensemble** : configurez l'outil ignitecli pour qu'il utilise le répertoire des sessions publiées comme source d'information principale et simplifiez la dérivation des chemins d'événements en une seule règle. Cela permettra d'intégrer les modifications récentes apportées à swiftDialog dans le fonctionnement réel de l'outil ignitecli. Les sections 3 et 4 sont des améliorations indépendantes de la robustesse de l'outil ignitecli qui peuvent être implémentées par la suite.

---

## 5. Journal de vérification

Les affirmations contenues dans ce document ont été vérifiées par rapport à la source le 17 juin 2026 :

- Les fichiers de configuration de Sessions ne sont pas lus par ignitecli — recherche de `Sources/` pour
  `swiftdialog/sessions` / `publishedSessions` : aucun consommateur.
- Le préréglage 6 émet un signal pour les boutons, les sélections et les étapes — `Preset6.swift:1116,1152,1251,1638`.
- Dérivation duale du chemin d'événement — `Preset1.swift:460`, `Preset2.swift:533`,
  `Preset5.swift:4834` ; L'outil `ignitecli` est utilisé explicitement `eventFile` dans `Sources/Resources/templates/*/config.json`.
- Confirmation envoyée, mais optionnelle. `CommandRouter.swift:351`
  ignitecli `DialogOrchestrator.swift:151`.
- La vitalité est présente uniquement dans `wait-exit` — `IpcState.swift:58`.
- Nettoyage préliminaire avant le lancement par rapport au saut d'octet — `DialogLauncher.swift:199`,
  `CommandRouter.swift:79`.
