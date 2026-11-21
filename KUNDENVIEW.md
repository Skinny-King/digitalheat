# Kundenview: Serverheizung für Hauseigentümer in der Nordwestschweiz

Stand 21.11.2026 · Säule «Kunde» des DigitalHeat-Case (Hackathon) · Die Säulen «Firma» und «Pharma» werden separat erarbeitet.

---

## 0. Kurzfassung

**Das Angebot:** DigitalHeat stellt eine Serverheizung kostenlos neben die bestehende Öl- oder Gasheizung. DigitalHeat zahlt Anlage, Einbau, Server-Strom und Unterhalt. Der Haushalt bekommt 93–100 % seiner Wärme von den Servern und braucht kaum noch Heizöl oder Gas.

**Was der Haushalt gewinnt (Gratiswärme, Durchschnitts-Einfamilienhaus mit 17'000 kWh Wärme pro Jahr):**

| Heute heizt der Haushalt mit | Ersparnis pro Jahr | CO2 pro Jahr |
|---|---|---|
| **Öl** | **3'317 CHF** (Referenzhaus: 5'686 CHF) | 5,3 t → 0,0 t |
| **Gas** | **2'636 CHF** (Referenzhaus: 4'520 CHF) | 3,7 t → 0,0 t |
| Wärmepumpe | 2'252 CHF (Referenzhaus: 3'861 CHF) | – |

Eigene Investition: **0 CHF**. Keine Sanierung nötig, weil die Serverheizung 50–70 °C liefert und zu alten Radiatoren passt.

**Strategie:** Einstieg mit **Ölheizungen in Basel-Stadt** (Pilot mit 5–10 Häusern), danach Öl in **Basel-Landschaft und Aargau** (rund 19'300 Öl-Wohngebäude allein in BL), dann **Gas** (Basler Gasnetz wird bis 2037 stillgelegt), zuletzt alle Haushalte.

**Bedingungen, damit es für den Kunden aufgeht:**
1. Die Wärme kostet den Haushalt höchstens rund **7 Rp./kWh** (Gratiswärme ist am stärksten). Gegenüber Öl lohnt sich der Wechsel bis 19,6 Rp., gegenüber Gas bis 15,6 Rp., gegenüber einer Wärmepumpe bis 13,3 Rp.
2. Es gibt das ganze Jahr **genug flexible Rechenaufträge**. Sonst sinkt die Deckung auf 52–63 % und die Ersparnis fast auf die Hälfte.
3. Die Kantone akzeptieren die Lösung (erneuerbarer Heizungsersatz, Heizstab als Notheizung). Das ist noch offen.

---

## 1. Ausgangslage und Auftrag

Der Case wird in drei Säulen bearbeitet:

| Säule | Frage | Wer |
|---|---|---|
| **Kunde** (dieses Dokument) | Warum stellt sich ein Hauseigentümer eine Serverheizung in den Keller, und was gewinnt er? | Joël |
| Firma | Wie verdient DigitalHeat Geld, und ist das Modell nachhaltig profitabel? | Kollegen |
| Pharma | Warum kaufen Pharmakonzerne diese Rechenleistung (Sicherheit, Preis)? | Kollegen |

Ziel ist eine Win-Win-Win-Situation. Dieses Dokument behandelt nur den Kunden. Wo das Kundenangebot von den anderen Säulen abhängt, steht das in Abschnitt 11 als Schnittstelle.

**Vorgehen:**
1. Zielkunde festlegen
2. Heutige Heizkosten kennen
3. Angebot und Bezahlmodell festlegen
4. Ersparnis rechnen, auch für schlechtere Fälle
5. Markt und Regeln in der Region prüfen
6. Einwände beantworten
7. Kunden-Dashboard ableiten
8. Schnittstellen mit den Kollegen klären

---

## 2. Zielkunde und Einstiegsstrategie

**Zielkunde im Pilot:** Eigentümer eines Einfamilienhauses mit **Ölheizung**, der aus dem Öl aussteigen will, ohne gleich eine teure Wärmepumpe samt Sanierung zu finanzieren.

**Warum Öl zuerst:**
- Höchste Heizkosten: 19,6 Rp. pro kWh Wärme (Gas 15,6, Wärmepumpe 13,3)
- Politischer Druck: Basel-Stadt will bis 2037 fossilfrei heizen, neue Öl- und Gasheizungen sind seit 2017 verboten
- Oft alte Häuser mit Radiatoren, in denen eine Wärmepumpe schlecht arbeitet
- Der Öltank im Keller macht die Wirkung sichtbar: Er leert sich kaum noch.

Öl ist der Einstieg, nicht das Ziel. Diese Kunden wechseln am schnellsten und werden zu Referenzen. Danach folgen die anderen:

| Phase | Wo und wer | Argument |
|---|---|---|
| **1 Pilot** | Ölheizungen in Basel-Stadt ausserhalb der Fernwärme (Bruderholz, Riehen, Bettingen), 5–10 Einfamilienhäuser | −93 bis −100 % Heizöl, 0 CHF Investition, Referenzen schaffen |
| **2 Öl ausrollen** | Basel-Landschaft (≈ 19'300 Öl-Wohngebäude), dann Aargau (135'574 Öl-Wohnungen) | gleiche Ersparnis, über zehnmal grösserer Markt |
| **3 Gas** | Basel-Stadt (Netz geht bis 2037 zu), dann Basel-Landschaft (≈ 20'500 Gas-Wohngebäude) | Ausstieg aus Gas ohne eigene Investition, Termindruck in BS |
| **4 Alle Haushalte** | Häuser mit Wärmepumpe, Neubauten, Mehrfamilienhäuser | Gratiswärme statt Strom für die Wärmepumpe |

---

## 3. Das Angebot

### 3.1 Wer zahlt was?
**DigitalHeat zahlt und besitzt alles:** Server, Einbau, Server-Strom (eigener Zähler) und Unterhalt. So beschreibt es auch DigitalHeat selbst («kein Hardwarekauf durch den Wärmeabnehmer»), und so arbeiten Heata und Deep Green in Grossbritannien.

Warum der Haushalt die Anlage nicht selbst kauft: Eine 8-kW-Einheit kostet geschätzt rund 162'000 CHF (Hardware ≈ 142'000, Einbau ≈ 20'000). Eine Wärmepumpe kostet in Basel 31'500–63'000 CHF. Die Serverheizung ist vor allem ein Rechenzentrum, das sich über verkaufte Rechenzeit bezahlt, nicht über die Wärme. Wie sich das für DigitalHeat rechnet, klärt die Säule Firma.

| Modell | Haushalt zahlt | Bewertung aus Kundensicht |
|---|---|---|
| **A Gratiswärme** (empfohlen für den Pilot) | nichts, stellt Platz und Anschluss | stärkstes Verkaufsargument |
| **B Wärmeabo** | Preis pro kWh, legt die Säule Firma fest | lohnt sich bis zur Schwelle in Abschnitt 4.3 |
| C Kunde kauft die Anlage | ≈ 162'000 CHF | nicht sinnvoll: zu teuer, zu riskant |

### 3.2 Die bestehende Heizung bleibt als Backup
Die Serverheizung kommt **neben** die bestehende Heizung. Für die kältesten Stunden und bei Ausfällen springt das Backup ein.

| Heute | Backup | Bemerkung |
|---|---|---|
| Öl | bestehender Ölkessel | kostet nichts, Tank bleibt; in BS spätestens 2037 durch erneuerbares Backup ersetzen |
| Gas (ausserhalb BS) | bestehender Gaskessel | Grundgebühr ≈ 195 CHF/Jahr bleibt |
| Gas (Basel-Stadt) | **Heizstab im Speicher** (≈ 2'000 CHF, Annahme) | nötig, weil das Gasnetz bis 2037 abgestellt wird; Erlaubnis als Notheizung offen |

### 3.3 Pilot-Aufbau (Vorschlag)
| | |
|---|---|
| Teilnehmende | 5–10 Einfamilienhäuser mit Ölheizung in Basel-Stadt, ausserhalb des Fernwärmegebiets |
| Voraussetzungen | Platz im Keller oder Heizraum (der Raum des Öltanks wird oft frei), Wasser-Heizsystem, Starkstromanschluss, Glasfaser |
| Dauer | 1 Jahr, damit Winter und Sommer drin sind |
| Kosten für den Haushalt | keine, auch nicht für den Rückbau |
| Was gemessen wird | Heizöl in Litern vorher und nachher, Wärme vom Server, Raumtemperatur und Komfort, Lärm, Ausfälle, Zufriedenheit |
| Nach dem Pilot | Gratiswärme weiter, Wärmeabo oder Rückbau ohne Kosten |

---

## 4. Was der Haushalt spart

Zwei Häuser:
- **Referenzhaus** des Case: 31'231 kWh Wärme pro Jahr, 8-kW-Einheit
- **Durchschnitts-EFH:** 17'000 kWh Wärme pro Jahr, 5-kW-Einheit (die kleinste DigitalHeat-Einheit)

Die Deckung kommt aus der Jahressimulation mit dem Wetter Basel 2025: **92,9 % bzw. 99,6 %**, wenn genug flexible Rechenaufträge da sind.

### 4.1 Was kostet heute 1 kWh Wärme?
| Heizung | Rp. pro kWh Wärme | Grundlage |
|---|---|---|
| Öl | **19,6** | 1,665 CHF/l, 10 kWh/l, Kessel 85 % |
| Gas | **15,6** + ≈ 195 CHF/Jahr Grundgebühr | IWB 2026, Stufe M, inkl. MwSt., Kessel 90 % |
| Wärmepumpe | **13,3** (BS) / 12,1 (BL, AG) | Strompreis ÷ Jahresarbeitszahl 2,5 |
| **Serverheizung, Gratiswärme** | **0** | DigitalHeat zahlt Strom und Anlage |

### 4.2 Ersparnis pro Jahr (Gratiswärme, Basel-Stadt)
| | Referenzhaus | Durchschnitts-EFH |
|---|---|---|
| **Öl:** heute → nachher | 6'118 → 432 CHF, **spart 5'686** | 3'330 → 13 CHF, **spart 3'317** |
| Heizöl in Litern | 3'674 → 259 l (−93 %) | 2'000 → 8 l (−100 %) |
| **Gas mit Gas-Backup:** heute → nachher | 5'057 → 538 CHF, **spart 4'520** | 2'841 → 205 CHF, **spart 2'636** |
| **Gas mit Heizstab-Backup** (kein Gasanschluss mehr) | **spart 4'325** | **spart 2'819** |
| **Wärmepumpe:** heute → nachher | 4'154 → 293 CHF, **spart 3'861** | 2'261 → 9 CHF, **spart 2'252** |
| CO2 Öl | 9,7 → 0,7 t | 5,3 → 0,0 t |
| CO2 Gas | 6,9 → 0,5 t | 3,7 → 0,0 t |

Muss ein Öl-Haushalt ohnehin ersetzen und entfällt dank der Serverheizung die neue Wärmepumpe (45'000 CHF − 10'500 CHF Förderung, über 18 Jahre), kommen **rund 1'900 CHF pro Jahr** dazu. Das gilt nur, wenn der Kanton die Serverheizung als Heizungsersatz akzeptiert (offen).

### 4.3 Ersparnis je nach Wärmepreis (Modell B)
Ersparnis pro Jahr, Referenzhaus / Durchschnitts-EFH:

| Wärmepreis | vs. Öl | vs. Gas | vs. Wärmepumpe |
|---|---|---|---|
| 0 Rp./kWh (gratis) | 5'686 / 3'317 | 4'520 / 2'636 | 3'861 / 2'252 |
| 3 Rp./kWh | 4'815 / 2'809 | 3'649 / 2'128 | 2'990 / 1'744 |
| 5 Rp./kWh | 4'235 / 2'470 | 3'069 / 1'789 | 2'410 / 1'405 |
| 8 Rp./kWh | 3'364 / 1'962 | 2'198 / 1'281 | 1'539 / 897 |
| 10 Rp./kWh | 2'783 / 1'624 | 1'617 / 943 | 958 / 559 |
| 13,3 Rp./kWh | 1'825 / 1'065 | 659 / 384 | 0 / 0 |

**Schwellen:** Öl 19,6 Rp., Gas 15,6 Rp., Wärmepumpe 13,3 Rp. pro kWh Wärme. Damit der Wechsel für einen Öl-Haushalt deutlich attraktiv bleibt (über 2'000 CHF im Durchschnitts-EFH), sollte die Wärme **höchstens rund 7 Rp./kWh** kosten.

### 4.4 Schlechterer Fall: zu wenig flexible Aufträge
Kommen nur Aufträge mit Frist (Nachfrage wie im Alibaba-Rechenzentrum), deckt die Serverheizung nur 52 % (Referenzhaus) bzw. 63 % (Durchschnitt).

| Gratiswärme | Referenzhaus | Durchschnitts-EFH |
|---|---|---|
| spart vs. Öl | 3'164 CHF | 2'104 CHF |
| spart vs. Gas (Gas-Backup) | 2'515 CHF | 1'673 CHF |
| spart vs. Gas (Heizstab) | 44 CHF | 761 CHF |
| spart vs. Wärmepumpe | 2'148 CHF | 1'429 CHF |

Der Heizstab-Backup lohnt sich also nur, wenn genug Aufträge da sind. Diese Frage geht an die Säule Pharma.

---

## 5. Warum es technisch passt

- **Temperatur:** DigitalHeat nennt 50–70 °C Vorlauf. Das reicht für alte Radiatoren und Warmwasser ohne Wärmepumpe. Eine Wärmepumpe braucht in solchen Häusern oft zuerst Dämmung und neue Heizkörper.
- **Sicher getrennt:** Direkte Flüssigkeitskühlung an den Prozessoren, eigener Kühlkreis, Wärmetauscher zum Heizwasser. Das Heizwasser kommt nie an die Server.
- **Speicher:** Ein Wassertank (im Modell 35 kWh) gleicht aus, wann die Server rechnen und wann das Haus Wärme braucht.
- **Grösse:** DigitalHeat baut Einheiten mit 5–20 kW. Unsere 8 kW (Referenzhaus) und 5 kW (Durchschnitt) liegen darin.
- **Jahresverlauf:** Im Winter laufen die Server fast pausenlos. Im Sommer liefern sie nur Warmwasser, und der Haushalt merkt keinen Unterschied.

---

## 6. Markt Nordwestschweiz

Nordwestschweiz = Grossregion des BFS: Basel-Stadt, Basel-Landschaft, Aargau.

| Kanton | Öl | Gas | Bezug |
|---|---|---|---|
| **Basel-Stadt** | 1'677 Ölfeuerungen (Juni 2026), 8 % der Wohngebäude | knapp 11'000 Gas-Liegenschaften (2024) | Anlagen bzw. Liegenschaften |
| **Basel-Landschaft** | ≈ 19'300 Wohngebäude (28,9 % von 66'780) | ≈ 20'500 Wohngebäude (30,7 %) | Wohngebäude 2024 |
| **Aargau** | 135'574 Wohnungen (39 %) | 58'620 Wohnungen (17 %) | Wohnungen 2024, nicht Gebäude |

**Ersparnis Durchschnitts-EFH pro Kanton (Gratiswärme):**

| | Basel-Stadt | Basel-Landschaft | Aargau |
|---|---|---|---|
| Strompreis 2026 | 33,25 Rp. (IWB) | 30,20 Rp. (EBL) | 30,15 Rp. (AEW) |
| spart vs. Öl | 3'317 CHF | 3'317 CHF | 3'317 CHF |
| spart vs. Gas | 2'636 CHF | ≈ 2'636 CHF | ≈ 2'636 CHF (Gaspreis angenommen) |
| spart vs. Wärmepumpe | 2'252 CHF | 2'045 CHF | 2'042 CHF |

**Basel-Stadt im Detail:**
- **Ölheizungen** nehmen schnell ab: 2'631 (2018) → 1'847 (2024) → 1'677 (Juni 2026).
- **Gasnetz:** Der Grosse Rat hat 2023 die Stilllegung bis 2037 beschlossen. Ab 2028 nimmt IWB rund 1'000 Anschlüsse pro Jahr vom Netz. Gas-Haushalte müssen also wechseln.
- **Fernwärme:** Wo Fernwärme kommt, ist sie die naheliegende Lösung, und die kantonale Förderung für dezentrale Heizungen ist dort halbiert. Die Serverheizung zielt deshalb auf die **Gebiete ohne Fernwärme**: laut Energierichtplan rund **5,3 km²**, vor allem **Bruderholz, Riehen, Bettingen** und Teile am Westrand von Basel. Karte: `dashboard/karte_fernwaerme.html`.

**Grössenordnung:** Wechseln 1 % der Öl-Wohngebäude in Basel-Landschaft (≈ 190 Häuser), sparen diese Haushalte zusammen rund **0,6 Mio. CHF und 1'000 t CO2 pro Jahr**.

---

## 7. Förderung und Regeln

| | Basel-Stadt | Basel-Landschaft | Aargau |
|---|---|---|---|
| Förderung Wärmepumpe (zum Vergleich) | 8'000 + 250 CHF/kWth, max. 40 %, halbiert im Fernwärmegebiet | Energiepaket BL, Beträge für Ölersatz 2026 nicht gefunden | Programm ab 1.5.2026; ältere Broschüre 6'000 + 180 CHF/kWth; keine Förderung im Verbundgebiet |
| Bund | Impulsprogramm (2025–2034, 200 Mio. CHF/Jahr): Ersatz von Elektroheizungen, Einbau einer Wärmeverteilung | gleich | gleich |
| Druck zum Wechsel | sehr hoch (Gasnetz zu bis 2037, fossile Neuanlagen verboten) | nicht im Detail geprüft | nicht im Detail geprüft |

- Für die Serverheizung gibt es **in keinem Kanton eine eigene Förderkategorie**.
- Ob sie als **erneuerbarer Heizungsersatz** zählt und ob ein **Heizstab als Notheizung** erlaubt ist, muss jeder Kanton beantworten. In Basel-Stadt ist das Amt für Umwelt und Energie, Abteilung Energie, zuständig.
- Im Pilot wird der Ölkessel nicht ersetzt, sondern ergänzt. Die Ersatzpflicht greift deshalb vermutlich noch nicht (Annahme).

---

## 8. Partner aus Kundensicht

| Partner | Was der Kunde davon hat |
|---|---|
| **IWB** bzw. **EBL / AEW** | bekannter regionaler Absender, Strom und Glasfaser aus einer Hand, Vertrauen |
| **Lokaler Heizungsinstallateur** | Einbau, Service und Backup aus der Region |
| **Smart-Home-Anbieter** (Loxone, Home Assistant, Homey, Matter) | Steuerung in der App, die er schon hat |
| **Versicherung** (z. B. Baloise) | Schäden an der Anlage sind nicht sein Risiko |
| **Bank** (grüne Hypothek, z. B. BKB) | günstigere Hypothek für ein Haus mit erneuerbarer Wärme |

---

## 9. Einwände und Antworten

| Einwand | Antwort |
|---|---|
| «Was, wenn der Server ausfällt?» | Das Backup springt automatisch ein, der Speicher überbrückt Stunden. |
| «Ist das laut?» | Flüssigkeitskühlung ohne grosse Lüfter, im Keller hinter einer Tür (Annahme, im Pilot messen). |
| «Wer haftet bei Schäden?» | DigitalHeat, über eine Versicherung. |
| «Kommt jemand an meine Daten oder ich an fremde?» | Getrennte Netze, verplombtes Gehäuse, der Haushalt hat keinen Zugang. |
| «Was, wenn ich umziehe?» | Der Vertrag geht auf den neuen Eigentümer über, oder die Anlage wird kostenlos zurückgebaut. |
| «Brauche ich trotzdem eine neue Wärmepumpe?» | Offen, hängt vom Kanton ab. Im Pilot bleibt die bestehende Heizung. |
| «Was, wenn DigitalHeat Konkurs geht?» | Die bisherige Heizung bleibt immer funktionsfähig. |

---

## 10. Kunden-Dashboard

**In der Smart-Home-App (nur das Wichtigste):**
- **Ersparnis in CHF** diesen Monat und seit Start
- Wärme vom Server heute und diesen Monat (kWh, Anteil am Bedarf)
- Heizöl bzw. Gas gespart (Liter bzw. kWh) und CO2 gespart
- Speicher-Füllstand in %
- Status: läuft / pausiert / Störung
- Knöpfe «Komfort» (wärmer) und «Abwesend» (Ferien)

**Im eigenen Dashboard (Details):**
- Verlauf Wärme, Backup und abgeführte Wärme pro Tag und Monat
- Vergleich mit der alten Heizung (CHF, CO2), auch für die ganze Vertragsdauer
- Rechenleistung: Stunden und Bereich (z. B. «Medikamentenforschung»), ohne Kundennamen
- Prognose der nächsten Tage (Wetter, erwartete Wärme)
- Wartung, Vertrag, Förderung, Kontakte

---

## 11. Schnittstellen zu den anderen Säulen

| Was die Kundenperspektive braucht | Von wem | Warum | Arbeitsannahme |
|---|---|---|---|
| Wer zahlt Hardware, Einbau und Server-Strom? | Firma | Gratiswärme nur möglich, wenn DigitalHeat zahlt | DigitalHeat zahlt alles |
| Gratiswärme oder Wärmeabo, zu welchem Preis? | Firma | bestimmt die Ersparnis (Abschnitt 4.3) | Gratiswärme im Pilot, sonst ≤ 7 Rp./kWh |
| Gibt es das ganze Jahr genug flexible Aufträge? | Pharma | Deckung 93–100 % statt 52–63 % | ja |
| Einheitengrösse pro Haus | Firma | Platz, Lärm, Anschluss | 8 kW / 5 kW |
| Sicherheitsauflagen im Haus | Pharma | was der Haushalt dulden muss | kein Zugang, verplombt |
| Vertrag, Kündigung, Konkurs | Firma | Vertrauen | Backup bleibt immer |

---

## 12. Risiken und offene Punkte
- **Zu wenig flexible Aufträge:** grösstes Risiko für die Ersparnis (Abschnitt 4.4)
- **Regeln der Kantone:** Serverheizung als Heizungsersatz? Heizstab als Notheizung?
- **Gas in Basel-Stadt:** Backup muss ersetzt werden, Fernwärme ist starke Konkurrenz
- **Lärm und Platz** von 5–8 kW Servern im Keller (im Pilot messen)
- **Preise:** Gaspreise in BL und AG ausserhalb des IWB-Gebiets, Förderbeträge BL 2026, MwSt. beim EBL-Strompreis
- **Wetter:** Gerechnet mit Basel 2025, im Aargau etwas kühler

---

## 13. Methode und Reproduzierbarkeit

| Was | Wo |
|---|---|
| Jahressimulation (Deckung, Backup, Speicher) | `src/scheduler/jahr.py`, `src/scheduler/kern.py` |
| Kundenrechnung (Öl, Gas, Wärmepumpe, Heizstab, Wärmepreise) | `src/kunde/wirtschaftlichkeit.py` → `daten/ergebnisse/win_win_win.json` |
| Karte Gebiete ohne Fernwärme | `src/kunde/karte_fernwaerme.py` → `dashboard/karte_fernwaerme.html` |
| Wetter | offizielles Case-CSV, identisch mit Open-Meteo Basel 2025 |
| Rohdaten | `daten/roh/` (ElCom, Geoportal BS, EBL) |

Neu rechnen:
```
python3 src/kunde/wirtschaftlichkeit.py
python3 src/kunde/karte_fernwaerme.py
```

---

## 14. Alle Annahmen mit Quellen

Status:
- **Case** = Vorgabe von DigitalHeat im Hackathon
- **Belegt** = aus einer öffentlichen Quelle übernommen
- **Abgeleitet** = aus belegten Werten gerechnet
- **Annahme** = selbst gesetzt, ohne Quelle. Vor einer Entscheidung prüfen.

Rechnung: `src/kunde/wirtschaftlichkeit.py` (alle Werte stehen dort in `P` mit Quelle), Physik aus `src/scheduler/jahr.py`.

### 14.1 Haus und Wärmebedarf
| Annahme | Wert | Status | Quelle |
|---|---|---|---|
| Wetter Basel 2025, stündlich | Open-Meteo, 47.56 N 7.55 E | Case, Belegt | offizielles Case-CSV, identisch mit [Open-Meteo Archiv](https://open-meteo.com/en/docs/historical-weather-api) |
| Heizbedarf Referenzhaus | max(0, 10 kW × (20 − T) ÷ 25,6) an Heiztagen = 26'851 kWh | Case | Case-Formel |
| Warmwasser | 12 kWh/Tag = 4'380 kWh/Jahr, gleichmässig über den Tag | Case | Case; Verteilung über den Tag = Annahme |
| Durchschnitts-EFH | 17'000 kWh/Jahr Wärme | Annahme | abgeleitet aus [Raiffeisen](https://www.raiffeisen.ch/rch/de/wissen/wohnen/energiesparen-erneuerbare-heizung.html): EFH mit 2'000 l Heizöl/Jahr × 10 kWh/l × 85 % |
| Speicher | 35 kWh, verlustfrei | Case | Case |

### 14.2 Serverheizung
| Annahme | Wert | Status | Quelle |
|---|---|---|---|
| Wärme pro Server | 1 kW Strom → 0,8 kW nutzbare Wärme | Case | Case |
| Einheitengrösse | 8 kW Referenzhaus, 5 kW Durchschnitts-EFH | Abgeleitet | Jahressimulation; DigitalHeat nennt 5–20 kW pro Einheit ([digitalheat.ch](https://digitalheat.ch)) |
| Vorlauftemperatur | 50–70 °C, passt zu alten Radiatoren | Belegt | [digitalheat.ch](https://digitalheat.ch) |
| Kühlung | direkte Flüssigkeitskühlung, Wärmetauscher trennt Kühlkreis und Heizwasser | Belegt | [digitalheat.ch](https://digitalheat.ch) |
| Deckungsgrad | 93 % (Referenz) / 99,6 % (Durchschnitt) | Abgeleitet | Jahressimulation, **setzt genug flexible Rechenaufträge voraus** (Säule Pharma) |
| Deckung ohne genug Aufträge | 52 % / 63 % | Abgeleitet | Jahressimulation mit Nachfrage aus dem Alibaba-Trace |
| Server-Strom zahlt nicht der Haushalt | eigener Zähler | Annahme | so bei [Heata](https://www.techradar.com/news/this-company-will-pay-for-your-heating-if-you-let-it-install-a-server-in-your-house) und [Deep Green](https://techradar.com/news/this-startup-is-recycling-energy-to-heat-swimming-pools-for-free); von Säule Firma zu bestätigen |
| Haushalt kauft keine Hardware | 0 CHF | Belegt (Absicht) | [digitalheat.ch](https://digitalheat.ch): «kein Hardwarekauf durch den Wärmeabnehmer» |
| Wärmepreis für den Haushalt | 0–13,3 Rp./kWh (Varianten) | offen | legt Säule Firma fest; Kundenperspektive empfiehlt ≤ 7 Rp./kWh |

### 14.3 Energiepreise
| Annahme | Wert | Status | Quelle |
|---|---|---|---|
| Strom | 33,25 Rp./kWh (Total, IWB, H4, 2026) | Belegt | [ElCom](https://www.strompreis.elcom.admin.ch) (API-Abruf, `daten/roh/elcom/`) |
| Heizöl | 1,665 CHF/l (3'000 l, Anfang Nov. 2026) | Belegt | [weekend.at](https://www.weekend.at/chronik/heizoelpreise-fallen-gruende-marktuebersicht-und-kaufempfehlung); Preis schwankt stark |
| Heizwert Heizöl | 10 kWh/l | Annahme | Standardwert Heizöl EL |
| Gas Arbeitspreis | 11,57 Rp./kWh (Stufe M, inkl. MwSt.) | Belegt | [IWB Gastarife 2026](https://www.iwb.ch/servicecenter/gastarife/aktuelle-tarife) |
| CO2-Abgabe Gas | 2,333 Rp./kWh (inkl. MwSt.) | Belegt | [IWB Gastarife 2026](https://www.iwb.ch/servicecenter/gastarife/aktuelle-tarife) |
| Konzessionsabgabe Gas BS | 0,11 Rp./kWh | Belegt | [IWB Gastarife 2026](https://www.iwb.ch/servicecenter/gastarife/aktuelle-tarife) |
| Gas Leistungspreis | 12,43 CHF/kW/Jahr, min. 194,58 CHF | Belegt | [IWB Gastarife 2026](https://www.iwb.ch/servicecenter/gastarife/aktuelle-tarife) |
| Tarifstufe M für das Referenzhaus | ≈ 35'000 kWh Gas | Abgeleitet | IWB-Beispiel EFH 20'000 kWh = Stufe M; Grenze der Stufen nicht publiziert |
| Gas-Anschlussleistung | 15 kW Referenz / 12 kW Durchschnitt | Annahme / Belegt | 12 kW aus IWB-Beispiel Typ II; 15 kW Annahme |

### 14.4 Heute verwendete Heizung
| Annahme | Wert | Status | Quelle |
|---|---|---|---|
| Wärmepumpe Jahresarbeitszahl | 2,5 | Case | Case («Wärme ersetzt Wärmepumpe, JAZ 2,5») |
| Ölkessel Wirkungsgrad | 85 % | Annahme | älterer Kessel |
| Gaskessel Wirkungsgrad | 90 % | Annahme | |
| CO2 Heizöl | 2,65 kg/l | Annahme | gängiger Emissionsfaktor Heizöl EL |
| CO2 Erdgas | 0,198 kg/kWh | Annahme | gängiger Emissionsfaktor Erdgas |
| Wärme kostet heute | Öl 19,6 / Gas 15,6 / WP 13,3 Rp. pro kWh Wärme | Abgeleitet | aus den Zeilen oben |

### 14.5 Investitionen und Förderung beim Haushalt
| Annahme | Wert | Status | Quelle |
|---|---|---|---|
| Neue Wärmepumpe in Basel | 31'500–63'000 CHF, gerechnet 45'000 | Belegt (Spanne) | [handwerker-kosten.ch](https://www.handwerker-kosten.ch/waermepumpe/basel/) |
| Förderung Wärmepumpe BS 2026 | 8'000 + 250 CHF/kWth (Luft/Wasser, ausserhalb Fernwärme), max. 40 %; Beispiel 8 kW = 10'500 | Belegt (nicht amtlich) | [ion-e.ch](https://www.ion-e.ch/de/waermepumpe-basel), [Stiebel Eltron](https://www.stiebel-eltron.ch/de/home/ratgeber/uebersicht/foerderung/basel-stadt.html); amtliche Broschüre 2026 war nicht abrufbar |
| Förderung halbiert im Fernwärmegebiet | ja | Belegt | [bs.ch](https://www.bs.ch/medienmitteilungen/2025-teilrevision-energieverordnung-mehr-foerderbeitraege-fuer-gesamtsanierungen-und-anpassung-beim-heizungsersatz) |
| Lebensdauer Wärmepumpe | 18 Jahre | Annahme | übliche 15–20 Jahre |
| Heizstab im Speicher (Backup ohne Gas) | 2'000 CHF einmalig | Annahme | grobe Schätzung, keine Offerte |
| Heizstab erlaubt? | als Notheizung | **offen** | Elektro-Widerstandsheizungen sind in der Schweiz eingeschränkt; beim AUE BS klären |
| Serverheizung gilt als erneuerbarer Heizungsersatz? | — | **offen** | beim AUE BS klären |
| Impulsprogramm Bund | 2025–2034, 200 Mio. CHF/Jahr, Elektroheizungen, Wärmeverteilung | Belegt | [admin.ch](https://www.admin.ch/de/newnsb/qGTPQ1ZqqKag), [BAFU](https://www.bafu.admin.ch/de/foerderungen-im-gebaeudebereich) |

### 14.6 Markt Basel-Stadt
| Annahme | Wert | Status | Quelle |
|---|---|---|---|
| Ölfeuerungen | 1'677 (Juni 2026), alle Gebäudetypen | Belegt | [bs.ch, Open Data AUE](https://www.bs.ch/wsu/aue/abteilung-energie/meldung-fossilbefeuerte-heizungen) |
| Ölanteil Wohngebäude | 8 % BS, 25–40 % in den meisten Kantonen | Belegt | [BFS](https://www.bfs.admin.ch/bfs/de/home/statistiken/bau-wohnungswesen/gebaeude/energiebereich.html) |
| Gas-Liegenschaften | knapp 11'000 (2024) | Belegt | Presse über IWB, siehe [bz Basel](https://www.bzbasel.ch/basel/basel-stadt/netto-null-bis-2037-trotz-fernwaerme-ausbau-stilllegung-des-gasnetzes-wird-zum-mammutprojekt-ld.2531385) |
| Gasnetz stillgelegt | bis 2037, ab 2028 ≈ 1'000 Anschlüsse/Jahr | Belegt | [IWB](https://www.iwb.ch/klimadreh/ratgeber/heizung-ersetzen/gasstilllegung-basel-stadt), [bs.ch](https://www.bs.ch/medienmitteilungen/wsu/2023-die-waermeversorgung-basel-stadt-wird-bis-2037-erneuerbar) |
| Neue Öl-/Gasheizungen verboten | seit 2017 | Belegt | [BKB](https://www.bkb.ch/de/privatkunden/magazin/2024/heizsysteme-basel-stadt-verzicht-auf-gas-und-oel-bis-2037-lohnt-sich-auch-finanziell) |
| Gebiete ohne Fernwärme | 5,3 km² mit dezentraler Lösung vorgesehen (Fernwärme 12,2 km²) | Belegt + Abgeleitet | Geoportal BS, Teilrichtplan Energie (WFS `ms:EP_Energierichtplan_*`), Flächen eigene Berechnung, `dashboard/karte_fernwaerme.html` |

### 14.7 Nordwestschweiz (siehe KUNDE_NORDWESTSCHWEIZ.md)
| Annahme | Wert | Status | Quelle |
|---|---|---|---|
| Region | BS, BL, AG (BFS-Grossregion) | Belegt | BFS |
| Strom BL | 30,20 Rp./kWh (EBL, N-Basis, 2026; MwSt. nicht angegeben) | Belegt | [EBL Mitteilung 2026](https://www.ebl.ch/hubfs/EBL/_EBL%20Website/Preisbl%C3%A4tter%202026/Mitteilung%20zu%20den%20Tarif%C3%A4nderungen%202026.pdf), Kopie in `daten/roh/elcom/` |
| Strom AG | 30,15 Rp./kWh (AEW, H4, 2026, inkl. MwSt.) | Belegt | [AEW info August 2025](https://www.aew.ch/sites/default/files/2025-11/AEW_info_August_2025_Mitteilungen_zu_Tarifaenderungen_im_Jahr_2026_neu3.pdf) |
| Gas BL/AG | wie IWB 2026 | Annahme | für AG ohne Quelle |
| Öl- und Gas-Wohngebäude BL | 28,9 % / 30,7 % von 66'780 (2024) | Belegt | [Energiestatistik BL 2024](https://www.baselland.ch/politik-und-behorden/direktionen/finanz-und-kirchendirektion/daten-statistik/abteilung-statistik/publikationen-und-statistiken/energie/webartikel-vom-07-07-2026-energiestatistik-2024) |
| Öl- und Gas-Wohnungen AG | 135'574 / 58'620 von 348'656 (2024) | Belegt | [Statistisches Jahrbuch AG 2025](https://www.ag.ch/app/staag/statistisches_jahrbuch/chapters/09_bau.html) |
| Wetter | Basel 2025 für die ganze Region | Annahme | Aargau etwas kühler |

### 14.8 Was die Kundenperspektive nicht annimmt
- Gewinn und Preise von DigitalHeat: Säule Firma (anderer Chat)
- Rechenpreise, Aufträge und Sicherheit: Säule Pharma
- Hardwarekosten: nur als Begründung, warum der Haushalt nicht selbst kauft
