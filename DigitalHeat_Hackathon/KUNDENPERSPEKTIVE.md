# Kundenperspektive (Haushalt) – Stand 21.11.2026

> Zusammengeführt in **KUNDENVIEW.md** (Gesamtdokument). Diese Datei bleibt als Arbeitsstand.

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
| **B Wärmeabo** | Preis pro kWh, legt die Säule Firma fest (Beispiel 9,3 Rp. = 30 % unter Wärmepumpe) | günstigere Wärme | schwächeres Argument, Ersparnis siehe 3d |
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

**Markt in Basel-Stadt**
- **1'677 Ölfeuerungen (Juni 2026)**, nach 1'729 (Dez. 2025), 1'847 (Ende 2024) und 2'631 (Ende 2018). Quelle: Open Data des Amts für Umwelt und Energie BS, gemeldete Anlagen, alle Gebäudetypen, nicht nur Einfamilienhäuser.
- Öl heizt in BS nur noch 8 % der Wohngebäude (BFS). In den meisten anderen Kantonen sind es 25–40 %.
- Neue Öl- und Gasheizungen sind in BS seit 2017 grundsätzlich verboten. Ziel des Kantons: fossilfreie Wärme bis 2037.
- **Folge für den Pilot:** Basel-Stadt eignet sich als Testgebiet, der grosse Markt liegt aber in den Nachbarkantonen (z. B. Basel-Landschaft) und in der übrigen Schweiz. Spätestens 2037 muss der Öl-Backup in BS durch ein erneuerbares Backup ersetzt werden.

**Gas in Basel-Stadt**
- IWB liefert Gas an **knapp 11'000 Liegenschaften** in Basel, Riehen und Bettingen (Bericht 2024, Liegenschaften, nicht Heizungen). Das sind rund sechsmal mehr als Ölfeuerungen.
- Der Grosse Rat hat im Januar 2023 beschlossen: **Das Gasnetz wird bis 2037 stillgelegt.** Erste Stilllegungen 2026/2027, **ab 2028 nimmt IWB rund 1'000 Gasanschlüsse pro Jahr vom Netz.**
- Rund die Hälfte der Gasheizungen ist älter als 15 Jahre (IWB-CEO, laut Presse).
- Wo möglich, ersetzt IWB das Gas durch **Fernwärme**. Wo Fernwärme noch fehlt, kann der Regierungsrat die Gasversorgung befristet verlängern.

**Was das für die Kundenperspektive heisst**
- **Gas-Haushalte müssen wechseln, ob sie wollen oder nicht**, mit festem Datum. Das ist ein grösserer und dringenderer Markt als Öl.
- **Aber:** Der Gas-Backup läuft mit der Stilllegung aus. Ein Gas-Haushalt braucht beim Umstieg auf die Serverheizung ein anderes Backup (z. B. eine kleine Wärmepumpe oder einen Elektroeinsatz im Speicher).
- **Konkurrenz Fernwärme:** Im Fernwärmegebiet ist der Anschluss an die Fernwärme die naheliegende Lösung, und kantonale Förderung für dezentrale Heizungen ist dort halbiert. Die Serverheizung zielt deshalb auf **Gas-Haushalte ausserhalb des Fernwärmegebiets** (z. B. in Riehen und Bettingen).
- **Folge für die Reihenfolge:** Öl bleibt der beste Einstieg für den Pilot (Backup bleibt, höchste Ersparnis). Gas ist danach der grösste Markt in Basel-Stadt, mit klarem Termindruck bis 2037.

**Backup für Gas-Haushalte: Heizstab statt Gas**
Wird der Gasanschluss aufgegeben, übernimmt ein Heizstab im Wärmespeicher die letzten Prozente (einmalig ≈ 2'000 CHF, ANNAHME).

| Gratiswärme | Referenzhaus | Durchschnitts-EFH |
|---|---|---|
| Strom für den Heizstab | 2'203 kWh = 733 CHF/Jahr | 68 kWh = 23 CHF/Jahr |
| Ersparnis vs. Gas mit Gas-Backup | 4'520 CHF/Jahr | 2'636 CHF/Jahr |
| **Ersparnis vs. Gas mit Heizstab** (keine Grundgebühr mehr) | **4'325 CHF/Jahr** | **2'819 CHF/Jahr** |

**Wichtig:** Der Heizstab lohnt sich nur, wenn die Serverheizung fast alles deckt. Gibt es zu wenig flexible Aufträge, müsste der Heizstab 6'000–15'000 kWh liefern, und die Ersparnis fällt fast auf null (Referenzhaus 44 CHF/Jahr). Ob ein Heizstab als Notheizung erlaubt ist, muss das AUE BS bestätigen.

**Karte:** `dashboard/karte_fernwaerme.html` zeigt die Gebiete ohne Fernwärme (Energierichtplan BS): vor allem Bruderholz, Riehen, Bettingen und Teile am Westrand von Basel, zusammen rund 5,3 km².

**Ganze Nordwestschweiz (BS, BL, AG):** siehe `KUNDE_NORDWESTSCHWEIZ.md`.

**Warum mit Öl anfangen (Einstiegsstrategie)**
Ölheizungs-Besitzer in Basel-Stadt sind die Gruppe mit dem grössten Druck und dem grössten Gewinn: höchste Heizkosten (19,6 Rp./kWh Wärme), politisches Ziel «fossilfrei bis 2037», oft alte Häuser, in denen eine Wärmepumpe schlecht passt. Sie wechseln am schnellsten und werden zu sichtbaren Referenzen. Danach folgen die anderen:

| Phase | Zielgruppe | Argument |
|---|---|---|
| **1 Pilot** | Ölheizungen in Basel-Stadt (5–10 EFH) | −93 bis −100 % Heizöl, 0 CHF Investition, Referenzen schaffen |
| **2 Ausrollen Öl** | Ölheizungen in Basel-Landschaft und weiteren Kantonen (25–40 % Ölanteil) | gleiches Angebot, grosser Markt |
| **3 Gas** | Gasheizungen (BS: Gasnetz wird bis 2037 stillgelegt, siehe unten) | Ausstieg aus Gas ohne eigene Investition |
| **4 Alle Haushalte** | Häuser mit Wärmepumpe oder Neubauten, Mehrfamilienhäuser | Gratiswärme statt Strom für die Wärmepumpe, Warmwasser im Sommer |

**Pilot-Aufbau (Vorschlag)**
| | |
|---|---|
| Teilnehmende | 5–10 Einfamilienhäuser in Basel mit Ölheizung |
| Voraussetzungen | Platz im Keller oder Heizraum (Öltank-Raum wird oft frei), Wasser-Heizsystem, Starkstromanschluss, Glasfaser oder gutes Internet |
| Dauer | 1 Jahr, damit Winter und Sommer drin sind |
| Kosten für den Haushalt | keine. Einbau, Server, Strom und Rückbau zahlt DigitalHeat |
| Was gemessen wird | Heizöl in Litern (vorher/nachher), Wärme vom Server, Raumtemperatur und Komfort, Lärm, Ausfälle, Zufriedenheit |
| Nach dem Pilot | Kunde wählt: weiter mit Gratiswärme oder Wärmeabo, oder Rückbau ohne Kosten |

## 3c. Vergleich: Serverheizung gegen Öl, Gas und Wärmepumpe
**Was kostet 1 kWh Wärme?**

| Heizung | Rp. pro kWh Wärme | Grundlage |
|---|---|---|
| Ölheizung | **19,6** | 1,665 CHF/l, 10 kWh/l, Kessel 85 % |
| Gasheizung | **15,6** + 195 CHF/Jahr Grundgebühr | IWB 2026, Stufe M, inkl. MwSt.: 11,57 + CO2-Abgabe 2,33 + Konzession 0,11 Rp./kWh Gas, Kessel 90 % |
| Wärmepumpe | **13,3** | Strom 33,25 Rp./kWh, JAZ 2,5 |
| Serverheizung, Wärmeabo | 9,3 | 30 % unter Wärmepumpe |
| **Serverheizung, Gratiswärme** | **0** | DigitalHeat zahlt Strom und Anlage |

**Ersparnis pro Jahr, wenn die Serverheizung neben die bestehende Heizung kommt** (Gratiswärme, flexible Aufträge)

| | Referenzhaus (31'231 kWh) | Durchschnitts-EFH (17'000 kWh) |
|---|---|---|
| **Öl:** heute → nachher | 6'118 → 432 CHF, **spart 5'686** | 3'330 → 13 CHF, **spart 3'317** |
| **Gas:** heute → nachher | 5'057 → 538 CHF, **spart 4'520** | 2'841 → 205 CHF, **spart 2'636** |
| **Wärmepumpe:** heute → nachher | 4'154 → 293 CHF, **spart 3'861** | 2'261 → 9 CHF, **spart 2'252** |
| CO2 Öl: heute → nachher | 9,7 → 0,7 t | 5,3 → 0,0 t |
| CO2 Gas: heute → nachher | 6,9 → 0,5 t | 3,7 → 0,0 t |

- Bei Gas bleibt die **Grundgebühr von rund 195 CHF/Jahr**, solange der Gasanschluss als Backup bleibt. Wird er später aufgegeben, fällt auch sie weg.
- Ohne genug flexible Aufträge (Szenario «Nur Jobs mit Frist») spart der Gas-Haushalt nur 2'515 bzw. 1'673 CHF/Jahr.
- Mit Wärmeabo statt Gratiswärme: Gas spart 1'817 bzw. 1'060 CHF/Jahr.
- **Reihenfolge der Attraktivität:** Öl vor Gas vor Wärmepumpe. Das bestätigt die Einstiegsstrategie mit Öl, Gas ist der logische zweite Schritt.

Vorbehalte: Die Stufe M gilt laut IWB-Beispiel für ein Einfamilienhaus mit 20'000 kWh. Für das Referenzhaus (≈ 35'000 kWh Gas) ist die Stufe abgeleitet, nicht bestätigt. Anschlussleistung 15 kW (Referenzhaus) ist eine Annahme, 12 kW (Durchschnitt) aus dem IWB-Beispiel. Kesselwirkungsgrade und CO2-Faktoren sind Annahmen.

## 3d. Ersparnis je nach Wärmepreis
Den Wärmepreis legt die Säule Firma fest (anderer Chat). Für den Haushalt zählt nur: **Bis zu welchem Preis lohnt sich der Wechsel?**

Ersparnis pro Jahr gegenüber der heutigen Heizung, Referenzhaus (29'027 kWh Serverwärme) / Durchschnitts-EFH (16'932 kWh):

| Wärmepreis | vs. Öl | vs. Gas | vs. Wärmepumpe |
|---|---|---|---|
| 0 Rp./kWh (gratis) | 5'686 / 3'317 | 4'520 / 2'636 | 3'861 / 2'252 |
| 3 Rp./kWh | 4'815 / 2'809 | 3'649 / 2'128 | 2'990 / 1'744 |
| 5 Rp./kWh | 4'235 / 2'470 | 3'069 / 1'789 | 2'410 / 1'405 |
| 8 Rp./kWh | 3'364 / 1'962 | 2'198 / 1'281 | 1'539 / 897 |
| 10 Rp./kWh | 2'783 / 1'624 | 1'617 / 943 | 958 / 559 |
| 13,3 Rp./kWh | 1'825 / 1'065 | 659 / 384 | 0 / 0 |

**Schwelle, ab der sich der Wechsel nicht mehr lohnt:** Öl 19,6 Rp., Gas 15,6 Rp., Wärmepumpe 13,3 Rp. pro kWh Wärme.

Damit der Wechsel für einen Öl-Haushalt **deutlich** attraktiv ist (über 2'000 CHF Ersparnis im Durchschnitts-EFH), darf die Wärme höchstens rund **7 Rp./kWh** kosten. Diese Zahl ist die Bitte der Kundenperspektive an die Säule Firma.

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
