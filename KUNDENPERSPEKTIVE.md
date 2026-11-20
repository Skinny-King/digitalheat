# Kundenperspektive (Haushalt) – Stand 21.11.2026

Rechnung: `python3 src/kunde/wirtschaftlichkeit.py` → `daten/ergebnisse/win_win_win.json`. Die Physik (Deckung, Strom, Auslastung) kommt aus derselben Jahressimulation wie die Bilanz. «ANNAHME» = selbst gesetzt, noch zu prüfen.

## 1. Vorgehen für die Kundenperspektive
1. **Kunde festlegen:** Eigentümer eines Einfamilienhauses in Basel **mit Ölheizung**, der aus dem Öl aussteigen will, ohne gleich eine teure Wärmepumpe und Sanierung zu finanzieren (Pilot, Abschnitt 3b).
2. **Heutige Kosten kennen:** Was zahlt der Haushalt heute für Wärme (Öl, Gas, Wärmepumpe) und was würde ein Heizungsersatz kosten?
3. **Angebot rechnen:** Wer zahlt was (Server, Strom, Installation, Wärme)? Mehrere Modelle vergleichen.
4. **Einwände sammeln:** Lärm, Platz, Sicherheit, Haftung, Internet, was passiert beim Ausfall, beim Umzug, nach Vertragsende?
5. **Schnittstellen klären:** Was das Kundenangebot von der Firma und vom Pharmakunden braucht (Abschnitt 4), mit den Kollegen abstimmen.
6. **Dashboard ableiten:** Was will der Kunde jeden Tag sehen (Smart-Home-App), was nur ab und zu (eigenes Dashboard)?

## 2. Wer zahlt den Server?
**Empfehlung: DigitalHeat zahlt und besitzt alles** (Server, Installation, Strom der Server). Das ist auch das Modell auf digitalheat.ch («kein Hardwarekauf durch den Wärmeabnehmer») und bei Heata (UK) und Deep Green (UK).

Gründe:
- Eine 8-kW-Einheit kostet rund **142'000 CHF Hardware + 20'000 CHF Installation**. Das kann und will kein Haushalt tragen.
- Die Hardware ist nach rund 5 Jahren abgeschrieben, das Risiko (Preis der Rechenzeit, Auslastung, Defekte) gehört zu dem, der die Rechenzeit verkauft.
- Der Server hat einen eigenen Stromzähler. Der Haushalt zahlt keinen Server-Strom.

| Modell | Haushalt zahlt | Haushalt bekommt | Bewertung |
|---|---|---|---|
| **A Gratiswärme** (empfohlen für den Pilot) | nichts, stellt Platz und Anschluss | Wärme gratis | sehr einfach zu verkaufen |
| **B Wärmeabo** | 9,3 Rp./kWh (30 % unter Wärmepumpe) | günstigere Wärme | mehr Erlös für DigitalHeat, schwächeres Argument |
| C Kunde kauft die Anlage | ≈ 162'000 CHF | Anteil am Rechenerlös | nicht sinnvoll: zu teuer, zu riskant |

## 3. Was spart der Haushalt? (Modell A, Gratiswärme)

| | Referenzhaus (Case) | Durchschnitts-EFH |
|---|---|---|
| Wärmebedarf (Heizung + Warmwasser) | 31'231 kWh | 17'000 kWh |
| Einheit | 8 kW | 5 kW (kleinste DigitalHeat-Einheit) |
| Wärme vom Server | **92,9 %** | **99,6 %** |
| Heizkosten heute mit **Wärmepumpe** | 4'154 CHF/Jahr | 2'261 CHF/Jahr |
| Heizkosten heute mit **Ölheizung** | 6'118 CHF/Jahr | 3'330 CHF/Jahr |
| **Ersparnis vs. Wärmepumpe** | **3'861 CHF/Jahr** | **2'252 CHF/Jahr** |
| **Ersparnis vs. Ölheizung** | **5'686 CHF/Jahr** | **3'317 CHF/Jahr** |
| Vermiedener Heizungsersatz (Wärmepumpe 45'000 − 10'500 Förderung, 18 Jahre) | + 1'917 CHF/Jahr | + 1'917 CHF/Jahr |
| **Total für Ölheizungs-Besitzer, der ersetzen muss** | **≈ 7'600 CHF/Jahr** | **≈ 5'200 CHF/Jahr** |

Mit Modell B (Wärmeabo) spart der Haushalt noch 1'158 bzw. 676 CHF/Jahr gegenüber einer Wärmepumpe, gegenüber Öl 2'984 bzw. 1'740 CHF/Jahr.

Grundlagen: Strom 33,25 Rp./kWh (ElCom 2026, IWB), Wärmepumpe JAZ 2,5 (Case) → 13,3 Rp./kWh Wärme. Heizöl 1,665 CHF/l (Anfang Nov. 2026), Kessel 85 % → 19,6 Rp./kWh Wärme. Wärmepumpe Basel 31'500–63'000 CHF (handwerker-kosten.ch), Förderung BS 2026 ≈ 10'500 CHF für 8 kW (ion-e.ch, nicht amtlich bestätigt).

**Wichtigster Vorbehalt:** Ob die Serverheizung in Basel als erneuerbarer Heizungsersatz gilt (Energiegesetz BS), ist offen. Nur dann entfällt die neue Wärmepumpe. Klärung beim Amt für Umwelt und Energie, Abteilung Energie.

## 3b. Pilot: Umstieg für Ölheizungs-Besitzer
**Idee:** Die Serverheizung ersetzt keine Wärmepumpe. Sie wird **neben die bestehende Ölheizung** gebaut. Die Ölheizung bleibt als Backup für die kältesten Stunden. So steigt der Haushalt ohne eigene Investition sofort fast ganz aus dem Öl aus und kann später in Ruhe entscheiden, was nach dem Ende des Ölkessels kommt.

**Was sich für den Haushalt ändert** (Gratiswärme, flexible Aufträge vorausgesetzt):

| | Referenzhaus (31'231 kWh) | Durchschnitts-EFH (17'000 kWh) |
|---|---|---|
| Heizöl heute | 3'674 l/Jahr | 2'000 l/Jahr |
| Heizöl mit Serverheizung | **259 l/Jahr (−93 %)** | **8 l/Jahr (−100 %)** |
| Heizkosten heute | 6'118 CHF/Jahr | 3'330 CHF/Jahr |
| Heizkosten mit Serverheizung | **432 CHF/Jahr** | **13 CHF/Jahr** |
| **Ersparnis** | **5'686 CHF/Jahr** | **3'317 CHF/Jahr** |
| CO2 heute → nachher | 9,7 t → **0,7 t** | 5,3 t → **0,0 t** |
| Eigene Investition | **0 CHF** | **0 CHF** |

Gibt es zu wenig flexible Aufträge (Szenario «Nur Jobs mit Frist»), sinkt der Ölverbrauch nur um 52 % bzw. 63 % (Ersparnis 3'164 bzw. 2'104 CHF/Jahr). Die Antwort der Säule Pharma dazu ist deshalb für den Pilot entscheidend.

Grundlagen: Heizöl 1,665 CHF/l (Anfang Nov. 2026), 10 kWh/l, Ölkessel 85 % (ANNAHME), 2,65 kg CO2 pro Liter Heizöl EL. Die CO2-Abgabe steckt im Ölpreis.

**Warum das gerade für Ölheizungs-Häuser passt**
- **Keine Sanierung nötig:** Alte Häuser mit Ölheizung haben oft Radiatoren, die 55–70 °C brauchen. Eine Wärmepumpe arbeitet dort schlecht oder braucht zuerst Dämmung und neue Heizkörper. Die Serverheizung liefert laut DigitalHeat 50–70 °C Vorlauf und passt an die bestehenden Radiatoren.
- **Keine Investition, kein Zeitdruck:** Der Ölkessel läuft weiter als Backup. Der Heizungsersatz wird um Jahre verschoben, und bis dahin sind kaum noch Öl und CO2 im Spiel.
- **Sofort sichtbar:** Der Öltank leert sich kaum noch. Das sieht der Kunde direkt, auch ohne App.
- **Rechtlich einfacher (ANNAHME, zu prüfen):** Weil der Ölkessel nicht ersetzt, sondern ergänzt wird, greift die Ersatzpflicht für erneuerbare Heizungen in Basel-Stadt im Pilot vermutlich noch nicht. Beim späteren Ersatz des Kessels stellt sich die Frage wieder.

**Pilot-Aufbau (Vorschlag)**
| | |
|---|---|
| Teilnehmende | 5–10 Einfamilienhäuser in Basel mit Ölheizung |
| Voraussetzungen | Platz im Keller oder Heizraum (Öltank-Raum wird oft frei), Wasser-Heizsystem, Starkstromanschluss, Glasfaser oder gutes Internet |
| Dauer | 1 Jahr, damit Winter und Sommer drin sind |
| Kosten für den Haushalt | keine. Einbau, Server, Strom und Rückbau zahlt DigitalHeat |
| Was gemessen wird | Heizöl in Litern (vorher/nachher), Wärme vom Server, Raumtemperatur und Komfort, Lärm, Ausfälle, Zufriedenheit |
| Nach dem Pilot | Kunde wählt: weiter mit Gratiswärme oder Wärmeabo, oder Rückbau ohne Kosten |

## 4. Schnittstellen zu den anderen Säulen (von Kollegen zu bestätigen)
Diese Werte rechnet nicht die Kundenperspektive. Sie sind nur so weit drin, wie das Kundenangebot von ihnen abhängt.

| Was ich brauche | Von wem | Warum es für den Kunden zählt | Arbeitsannahme bis zur Bestätigung |
|---|---|---|---|
| Wer zahlt Hardware, Installation und Server-Strom? | Säule Firma | Davon hängt ab, ob Gratiswärme möglich ist | DigitalHeat zahlt alles |
| Kann sich die Firma Gratiswärme leisten, oder braucht es ein Wärmeabo? | Säule Firma | Bestimmt die Ersparnis (3'861 vs. 1'158 CHF/Jahr gegenüber WP) | Gratiswärme im Pilot |
| Wie viele flexible Aufträge gibt es das ganze Jahr? | Säule Pharma | Davon hängt ab, ob im Winter genug Wärme kommt (93 % vs. 52 % Deckung) | genug flexible Aufträge |
| Welche Einheitengrösse (kW) pro Haus? | Säule Firma | Lärm, Platz, Anschluss | 8 kW Referenzhaus, 5 kW Durchschnitt |
| Sicherheitsauflagen der Pharmakunden im Haus (Zugang, Plombe, Kamera?) | Säule Pharma | Was der Haushalt dulden muss | kein Zugang, verplombtes Gehäuse |
| Vertragslaufzeit, Kündigung, was bei Konkurs | Säule Firma | Vertrauen des Kunden | Backup-Heizung bleibt immer |

Eine erste Rechnung der Firmenseite (zur Kontrolle, nicht mein Teil) liegt in `daten/ergebnisse/win_win_win.json`.

## 5. Förderungen
| Programm | Für wen | Relevanz | Stand |
|---|---|---|---|
| **Förderbeiträge Energie Basel-Stadt** (Gesuch über dasgebaeudeprogramm.ch/bs) | Haushalt | Wärmepumpe 2026: 8'000 CHF + 250 CHF/kWth (Luft/Wasser), max. 40 % der Investition, halbiert im Fernwärmegebiet. **Serverheizung ist keine genannte Kategorie** | klären mit AUE BS |
| **Impulsprogramm Bund** (Klima- und Innovationsgesetz, 2025–2034, 200 Mio. CHF/Jahr, Vollzug durch Kantone) | Haushalt | fördert Ersatz von Elektroheizungen und den Einbau einer Wärmeverteilung (bis 100 %) | prüfen, ob anwendbar |
| **Gebäudeprogramm** (CO2-Abgabe) | Haushalt | Dämmung, erneuerbare Heizungen | über Kanton |
Förderungen sind im Rechenbeispiel nicht eingerechnet (ausser der vermiedenen Wärmepumpenförderung). Sie sind ein Zusatzvorteil.

Hinweis für die Säule Firma (nicht Teil der Kundenperspektive): BFE-Pilot- und Demonstrationsprojekte, Innosuisse und CO2-Bescheinigungen (z. B. Stiftung KliK, 5–10 t CO2 pro Haus und Jahr, wenn Öl verdrängt wird) könnten für DigitalHeat selbst in Frage kommen.

## 6. Partner, die der Kunde spürt
| Partner | Was der Kunde davon hat |
|---|---|
| **IWB** | bekannter Absender, Strom und Glasfaser aus einer Hand, Vertrauen |
| **Lokaler Heizungsinstallateur** | Einbau, Service und Backup-Heizung von jemandem aus der Region |
| **Smart-Home-Anbieter** (Loxone, Home Assistant, Homey, Matter) | Steuerung in der App, die er schon hat |
| **Versicherung** (z. B. Baloise) | Schäden an der Anlage sind nicht sein Risiko |
| **Bank** (grüne Hypothek, z. B. BKB) | günstigere Hypothek für ein Haus mit erneuerbarer Wärme |

## 7. Das Angebot an den Kunden in einem Satz
**DigitalHeat stellt eine Serverheizung kostenlos neben die Ölheizung, zahlt deren Strom und Unterhalt, und der Haushalt braucht über 90 % weniger Heizöl. Das spart 3'300–5'700 CHF pro Jahr, ohne eigene Investition und ohne Sanierung.**

Einwände und Antworten:
| Einwand | Antwort |
|---|---|
| «Was, wenn der Server ausfällt?» | Die Backup-Heizung bleibt und springt automatisch ein, der Speicher überbrückt Stunden |
| «Ist das laut?» | ANNAHME: Flüssigkeitskühlung ohne grosse Lüfter, im Keller hinter einer Tür; vor dem Pilot messen |
| «Wer haftet bei Schäden?» | DigitalHeat, über eine Versicherung |
| «Kommt jemand an meine Daten oder ich an fremde?» | Getrennte Netze, verplombtes Gehäuse, der Haushalt hat keinen Zugang |
| «Was, wenn ich umziehe?» | Vertrag geht auf den neuen Eigentümer über oder die Anlage wird zurückgebaut |
| «Brauche ich trotzdem eine neue Wärmepumpe?» | Offen, hängt vom Kanton ab (siehe Abschnitt 3) |

## 8. Was der Kunde sehen will (Grundlage fürs Dashboard)
**Smart-Home-App (nur das Wichtigste):**
- Wärme heute und diesen Monat vom Server (kWh, Anteil am Bedarf)
- **Ersparnis in CHF** diesen Monat und seit Start
- Speicher (Füllstand in %)
- Status: läuft / pausiert / Störung
- Ein Knopf: «Komfort» (wärmer) und «Abwesend» (Ferien)

**Eigenes Dashboard (Details):**
- Verlauf Wärme, Backup, abgeführte Wärme pro Tag und Monat
- Vergleich mit der alten Heizung (CHF, CO2)
- Rechenleistung: Stunden, für welchen Bereich (z. B. «Medikamentenforschung»), ohne Kundennamen
- Wartung, Vertrag, Förderung, Kontakte
- Prognose der nächsten Tage (Wetter, erwartete Wärme)

## 9. Offene Punkte
- Gilt die Serverheizung im Kanton Basel-Stadt als erneuerbarer Heizungsersatz?
- Lärm und Platzbedarf von 8 kW Servern im Keller
- Vertragslaufzeit, Umzug, was passiert bei Konkurs von DigitalHeat (Backup-Heizung muss bleiben)
- Antworten der anderen Säulen auf die Schnittstellen in Abschnitt 4
