# Kundenperspektive: Win-Win-Win (Stand 21.11.2026)

Rechnung: `python3 src/kunde/wirtschaftlichkeit.py` → `daten/ergebnisse/win_win_win.json`. Die Physik (Deckung, Strom, Auslastung) kommt aus derselben Jahressimulation wie die Bilanz. «ANNAHME» = selbst gesetzt, noch zu prüfen.

## 1. Vorgehen für die Kundenperspektive
1. **Kunde festlegen:** Eigentümer eines Einfamilienhauses in Basel, der die Heizung ersetzen muss oder will (alte Öl- oder Gasheizung, Basel verlangt beim Ersatz erneuerbare Wärme).
2. **Heutige Kosten kennen:** Was zahlt der Haushalt heute für Wärme (Öl, Gas, Wärmepumpe) und was würde ein Heizungsersatz kosten?
3. **Angebot rechnen:** Wer zahlt was (Server, Strom, Installation, Wärme)? Mehrere Modelle vergleichen.
4. **Einwände sammeln:** Lärm, Platz, Sicherheit, Haftung, Internet, was passiert beim Ausfall, beim Umzug, nach Vertragsende?
5. **Gegen die anderen zwei Säulen prüfen:** Das Angebot muss auch für DigitalHeat und den Pharmakunden aufgehen, sonst ist es kein Win-Win-Win.
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

## 4. Lohnt es sich für DigitalHeat?
Hardware: L40S-Klasse, 8 GPUs ≈ 70'000 $ (Thinkmate, Lambda), ≈ 3,8 kW, + 15 % Flüssigkeitskühlung → **17'800 CHF pro kW**, 2,1 GPUs pro kW. Abschreibung 5 Jahre, Unterhalt 5 %/Jahr.

| Referenzhaus, 8 kW, Modell A | Rechenpreis tief (0,86 $/GPU-h) | **Pharma-Preis (1,40 $/GPU-h)** |
|---|---|---|
| Rechenerlös | 55'100 CHF | **89'500 CHF** |
| Strom | − 12'100 | − 12'100 |
| Hardware (Abschreibung + Unterhalt) | − 35'600 | − 35'600 |
| Installation, Netz, Betrieb | − 2'600 | − 2'600 |
| **Gewinn pro Haus und Jahr** | **5'000 CHF** | **39'300 CHF** |
| Rendite auf 162'000 CHF Investition | 3 % | **24 %** |
| Amortisation | 4,7 Jahre | **2,3 Jahre** |
| Break-even-Rechenpreis | 0,78 $/GPU-h | 0,78 $/GPU-h |

**Wann es nicht aufgeht:**
- Fällt der Preis unter **0,78 $ pro GPU-Stunde**, macht DigitalHeat Verlust. Der tiefste Marktpreis liegt heute bei 0,38–0,86 $.
- Kommen nur Aufträge mit Frist (Alibaba-Szenario), sinkt die Deckung auf 52 %, und bei tiefem Preis entsteht Verlust (−3'000 CHF/Jahr). DigitalHeat braucht deshalb **feste, flexible Aufträge**, und genau die liefert der Pharmakunde.
- Die Amortisation muss klar unter 5 Jahren liegen, sonst ist die Hardware abgeschrieben, bevor sie sich bezahlt hat.

## 5. Lohnt es sich für den Pharmakunden?
- Preis **1,40 $ pro GPU-Stunde**: 25 % unter AWS (1,86 $, g6e) und 11 % unter dem Marktmedian (1,57 $).
- **Rechenort Schweiz**, keine Daten in einer US-Cloud.
- **Gute Aufträge** für Serverheizungen, weil sie lang laufen, warten können und sich pausieren lassen: Molekül-Docking, Virtual Screening, Proteinstrukturen, Embeddings von Fachliteratur.
- **Sicherheit:** Server in Privathäusern brauchen verschlüsselte Datenträger, verplombte Gehäuse, keinen Zugang für den Haushalt und eine Fernsperre. **Keine Patientendaten** in Privathäusern, nur Daten ohne Personenbezug (Moleküle, Strukturen). Für vertrauliche Modelle wären GPUs mit «Confidential Computing» nötig, etwa H100. Die sind teurer und rechnen sich nur bei höheren Preisen.
- Pro Referenzhaus rund **76'000 GPU-Stunden pro Jahr**.

## 6. Förderungen
| Programm | Für wen | Relevanz | Stand |
|---|---|---|---|
| **Förderbeiträge Energie Basel-Stadt** (Gesuch über dasgebaeudeprogramm.ch/bs) | Haushalt | Wärmepumpe 2026: 8'000 CHF + 250 CHF/kWth (Luft/Wasser), max. 40 % der Investition, halbiert im Fernwärmegebiet. **Serverheizung ist keine genannte Kategorie** | klären mit AUE BS |
| **Impulsprogramm Bund** (Klima- und Innovationsgesetz, 2025–2034, 200 Mio. CHF/Jahr, Vollzug durch Kantone) | Haushalt | fördert Ersatz von Elektroheizungen und den Einbau einer Wärmeverteilung (bis 100 %) | prüfen, ob anwendbar |
| **Gebäudeprogramm** (CO2-Abgabe) | Haushalt | Dämmung, erneuerbare Heizungen | über Kanton |
| BFE: Pilot- und Demonstrationsprojekte, EnergieSchweiz | DigitalHeat | Pilotanlagen und Abwärmenutzung (BFE-Bericht «Abwärmenutzung von Rechenzentren», 2023) | aus eigener Kenntnis, Bedingungen prüfen |
| Innosuisse (Innovationsprojekte, Start-up-Coaching) | DigitalHeat | Entwicklung mit einer Hochschule, z. B. FHNW | prüfen |
| CO2-Kompensation (z. B. Stiftung KliK) | DigitalHeat | Ersetzt die Serverheizung eine Ölheizung, spart sie rund 8 t CO2 pro Jahr und Haus, das wäre bescheinigbar | prüfen |

Förderungen sind im Rechenbeispiel nicht eingerechnet (ausser der vermiedenen Wärmepumpenförderung). Sie sind ein Zusatzvorteil.

## 7. Mögliche Partner
| Partner | Rolle | Nutzen |
|---|---|---|
| **IWB** (Basler Energieversorger) | Strom, Glasfaser, Energie-Contracting, Kundenzugang | Vertrauen, bestehende Heizungskunden, evtl. Spezialtarif |
| **Pharma Basel** (Roche, Novartis, Lonza, Biotech-Start-ups) | Rechenkunde | lokal, Schweizer Rechenort, Nachhaltigkeitsziele |
| **Heizungsinstallateure** | Einbau, Service, Backup-Heizung | Netz von Fachleuten vor Ort |
| **Smart-Home** (Loxone, Home Assistant, Homey, Matter) | App-Integration | Kunde steuert alles in seiner gewohnten App |
| **Versicherung** (z. B. Baloise, Basel) | Hardware im Privathaus, Haftung | nimmt dem Haushalt die Sorge vor Schäden |
| **Banken** (grüne Hypothek, z. B. BKB) | Finanzierung | günstige Hypothek für Häuser mit Serverheizung |
| **Hardware** (Supermicro, Dell über Schweizer Integratoren) | Server, Flüssigkeitskühlung | Mengenrabatt, Garantie |
| Hochschule (FHNW, Uni Basel) | Messung, Innosuisse-Projekt | Glaubwürdigkeit, Fördergeld |

## 8. Win-Win-Win auf einen Blick (Referenzhaus, Modell A, Pharma-Preis)
| Haushalt | DigitalHeat | Pharma |
|---|---|---|
| spart **3'900–5'700 CHF/Jahr** Heizkosten, + ≈ 1'900 CHF/Jahr, wenn kein Heizungsersatz nötig ist | **39'000 CHF Gewinn pro Haus und Jahr**, 24 % Rendite, Amortisation 2,3 Jahre | **25 % günstiger als AWS**, Rechenort Schweiz, flexible Batch-Aufträge |
| kein Kauf, kein Server-Strom, kein Risiko | Risiko: Preis unter 0,78 $/GPU-h oder zu wenig flexible Aufträge | Risiko: Sicherheit im Privathaus, nur Daten ohne Personenbezug |

## 9. Was der Kunde sehen will (Grundlage fürs Dashboard)
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

## 10. Offene Punkte
- Gilt die Serverheizung im Kanton Basel-Stadt als erneuerbarer Heizungsersatz?
- Echte Hardware- und Installationspreise (Offerten), Kosten der Flüssigkeitskühlung
- Lärm und Platzbedarf von 8 kW Servern im Keller
- Vertragslaufzeit, Umzug, was passiert bei Konkurs von DigitalHeat (Backup-Heizung muss bleiben)
- Pharma: welche Aufträge, welche Sicherheitsstufe, welcher Mindestumfang
