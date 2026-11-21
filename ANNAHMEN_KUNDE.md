# Annahmen der Kundenperspektive mit Quellen (Stand 21.11.2026)

Status:
- **Case** = Vorgabe von DigitalHeat im Hackathon
- **Belegt** = aus einer öffentlichen Quelle übernommen
- **Abgeleitet** = aus belegten Werten gerechnet
- **Annahme** = selbst gesetzt, ohne Quelle. Vor einer Entscheidung prüfen.

Rechnung: `src/kunde/wirtschaftlichkeit.py` (alle Werte stehen dort in `P` mit Quelle), Physik aus `src/scheduler/jahr.py`.

## 1. Haus und Wärmebedarf
| Annahme | Wert | Status | Quelle |
|---|---|---|---|
| Wetter Basel 2025, stündlich | Open-Meteo, 47.56 N 7.55 E | Case, Belegt | offizielles Case-CSV, identisch mit [Open-Meteo Archiv](https://open-meteo.com/en/docs/historical-weather-api) |
| Heizbedarf Referenzhaus | max(0, 10 kW × (20 − T) ÷ 25,6) an Heiztagen = 26'851 kWh | Case | Case-Formel |
| Warmwasser | 12 kWh/Tag = 4'380 kWh/Jahr, gleichmässig über den Tag | Case | Case; Verteilung über den Tag = Annahme |
| Durchschnitts-EFH | 17'000 kWh/Jahr Wärme | Annahme | abgeleitet aus [Raiffeisen](https://www.raiffeisen.ch/rch/de/wissen/wohnen/energiesparen-erneuerbare-heizung.html): EFH mit 2'000 l Heizöl/Jahr × 10 kWh/l × 85 % |
| Speicher | 35 kWh, verlustfrei | Case | Case |

## 2. Serverheizung
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

## 3. Energiepreise
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

## 4. Heute verwendete Heizung
| Annahme | Wert | Status | Quelle |
|---|---|---|---|
| Wärmepumpe Jahresarbeitszahl | 2,5 | Case | Case («Wärme ersetzt Wärmepumpe, JAZ 2,5») |
| Ölkessel Wirkungsgrad | 85 % | Annahme | älterer Kessel |
| Gaskessel Wirkungsgrad | 90 % | Annahme | |
| CO2 Heizöl | 2,65 kg/l | Annahme | gängiger Emissionsfaktor Heizöl EL |
| CO2 Erdgas | 0,198 kg/kWh | Annahme | gängiger Emissionsfaktor Erdgas |
| Wärme kostet heute | Öl 19,6 / Gas 15,6 / WP 13,3 Rp. pro kWh Wärme | Abgeleitet | aus den Zeilen oben |

## 5. Investitionen und Förderung beim Haushalt
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

## 6. Markt Basel-Stadt
| Annahme | Wert | Status | Quelle |
|---|---|---|---|
| Ölfeuerungen | 1'677 (Juni 2026), alle Gebäudetypen | Belegt | [bs.ch, Open Data AUE](https://www.bs.ch/wsu/aue/abteilung-energie/meldung-fossilbefeuerte-heizungen) |
| Ölanteil Wohngebäude | 8 % BS, 25–40 % in den meisten Kantonen | Belegt | [BFS](https://www.bfs.admin.ch/bfs/de/home/statistiken/bau-wohnungswesen/gebaeude/energiebereich.html) |
| Gas-Liegenschaften | knapp 11'000 (2024) | Belegt | Presse über IWB, siehe [bz Basel](https://www.bzbasel.ch/basel/basel-stadt/netto-null-bis-2037-trotz-fernwaerme-ausbau-stilllegung-des-gasnetzes-wird-zum-mammutprojekt-ld.2531385) |
| Gasnetz stillgelegt | bis 2037, ab 2028 ≈ 1'000 Anschlüsse/Jahr | Belegt | [IWB](https://www.iwb.ch/klimadreh/ratgeber/heizung-ersetzen/gasstilllegung-basel-stadt), [bs.ch](https://www.bs.ch/medienmitteilungen/wsu/2023-die-waermeversorgung-basel-stadt-wird-bis-2037-erneuerbar) |
| Neue Öl-/Gasheizungen verboten | seit 2017 | Belegt | [BKB](https://www.bkb.ch/de/privatkunden/magazin/2024/heizsysteme-basel-stadt-verzicht-auf-gas-und-oel-bis-2037-lohnt-sich-auch-finanziell) |
| Gebiete ohne Fernwärme | 5,3 km² mit dezentraler Lösung vorgesehen (Fernwärme 12,2 km²) | Belegt + Abgeleitet | Geoportal BS, Teilrichtplan Energie (WFS `ms:EP_Energierichtplan_*`), Flächen eigene Berechnung, `dashboard/karte_fernwaerme.html` |

## 7. Was die Kundenperspektive nicht annimmt
- Gewinn und Preise von DigitalHeat: Säule Firma (anderer Chat)
- Rechenpreise, Aufträge und Sicherheit: Säule Pharma
- Hardwarekosten: nur als Begründung, warum der Haushalt nicht selbst kauft
