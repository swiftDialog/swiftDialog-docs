---
title: Baukastenmodus – Schaltflächen
description: Bearbeiten Sie die Eigenschaften und das Aussehen eines Dialogfensters und geben Sie die Ergebnisse als JSON-Konfigurationsdatei aus
translationSynced: 2026-11-23T08:35:52+00:00
---

Ermöglicht die Einstellung von Eigenschaften für den Schaltflächenbereich

<img width="500" alt="image" src="/builder/builder buttons.png" />

#### Schaltflächengröße

Legen Sie eine der vier möglichen Schaltflächengrößen fest (diese Einstellung gilt für alle Schaltflächen).

 - Mini
 - klein
 - regelmäßig (Standardeinstellung)
 - groß

#### Schaltfläche 1

Legt den Text fest, der auf Schaltfläche 1 angezeigt wird – auch bekannt als Standard-Schaltfläche

Standardeinstellung `"OK"`

Die Einstellung "Deaktiviert" setzt den Zustand von Schaltfläche 1 auf deaktiviert (wobei die Aktivierung wiederhergestellt werden kann über den Befehl in der `button1: enable`-Konfigurationsdatei).

#### Schaltfläche 2

Legen Sie den Text fest, der auf Schaltfläche 2 angezeigt werden soll

Standardeinstellung `"Cancel"`

#### Info-Schaltfläche

Legen Sie den Text fest, der auf der Info-Schaltfläche angezeigt werden soll

Aktivieren Sie die Option "Beenden bei Info", sodass das Dialogfenster geschlossen wird, wenn auf die Info-Schaltfläche geklickt wird

Legen Sie für die Aktion der Info-Schaltfläche eine URL fest, die geöffnet wird, wenn die Schaltfläche angeklickt wird.

#### Symbol

Die Schaltfläche 1, Schaltfläche 2 und die Info-Schaltfläche können jeweils ein SF-Symbol zusammen mit ihrer Beschriftung anzeigen. Der Symbol-Editor stellt die Eigenschaften des Symbols als einzelne Steuerelemente bereit:

 - **Symbolname für die SF-Bibliothek**
 - **Position** – führend, nachfolgend, oben oder unten
 - **Darstellungsmodus:** hierarchisch, monochrom, mehrfarbig oder Palettenmodus
 - **Farbe:** Eine einzelne Farbe oder 2–3 Farben aus der Farbpalette, wenn der Modus "Farbpalette" ausgewählt ist
 - **Maßanfertigung**

Eine Live-Vorschau des erstellten Symbols wird angezeigt, und die Schaltfläche im Dialogfenster wird während der Bearbeitung aktualisiert.

[Zurück](/de/builder/builder/)