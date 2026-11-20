"""Win-Win-Win-Rechnung: Haushalt, DigitalHeat (Betreiber) und Pharma (Rechenkunde).

Physik kommt aus derselben Jahressimulation wie die Bilanz (src/scheduler/jahr.py, Haus).
Neu sind Preise und Kosten für Hardware, Installation, Wärme und Rechenzeit.
Jede Annahme steht in P mit Quelle. «ANNAHME» = selbst gesetzt, prüfen.

Aufruf: python3 src/kunde/wirtschaftlichkeit.py  -> daten/ergebnisse/win_win_win.json + Tabelle
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from src.scheduler.jahr import Haus, profil_laden  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
CHF = 0.84  # CHF pro USD (Angabe Joël, 20.11.2026)

P = {
    # --- Energiepreise ---
    "strom_chf_kwh": (0.3325, "ElCom 2026, IWB Basel, H4"),
    "jaz_waermepumpe": (2.5, "Case"),
    "heizoel_chf_l": (1.665, "weekend.at, Schweiz Anfang Nov. 2026, 3'000 l (1,66–1,67 CHF/l)"),
    "heizoel_kwh_l": (10.0, "Heizwert Heizöl EL ≈ 10 kWh/l"),
    "wirkungsgrad_oelkessel": (0.85, "ANNAHME, älterer Ölkessel"),
    # --- Haushalt ---
    "ww_kwh_tag": (12.0, "Case"),
    "durchschnitt_waerme_kwh": (17000.0, "ANNAHME aus Raiffeisen-Beispiel: EFH mit 2'000 l Heizöl/Jahr ≈ 20'000 kWh Brennstoff × 0,85"),
    "wp_neu_chf": (45000.0, "handwerker-kosten.ch: Wärmepumpe Basel 31'500–63'000 CHF (2026), Mitte"),
    "wp_foerderung_chf": (10500.0, "ion-e.ch: BS 2026 Luft/Wasser 8'000 + 250/kWth, Beispiel 8 kW = 10'500 (nicht amtlich geprüft)"),
    "wp_lebensdauer_j": (18.0, "ANNAHME, übliche Nutzungsdauer Wärmepumpe 15–20 Jahre"),
    # --- Hardware (L40S-Klasse, PCIe, flüssigkeitsgekühlt) ---
    "server_usd_8xl40s": (70000.0, "Thinkmate 56'100–82'000 $, Lambda 79'999–82'999 $ (8× L40S, 4U, luftgekühlt), Mitte"),
    "kw_8xl40s": (3.8, "ANNAHME: 8 × 350 W GPU + ≈ 1 kW Host"),
    "aufpreis_fluessigkuehlung": (0.15, "ANNAHME: +15 % für direkte Flüssigkeitskühlung (DigitalHeat-Bauweise)"),
    "hw_abschreibung_j": (5.0, "ANNAHME, übliche Nutzungsdauer GPU-Server"),
    "hw_unterhalt_anteil": (0.05, "ANNAHME: 5 % der Hardware pro Jahr (Ersatzteile, Service)"),
    "installation_chf": (20000.0, "ANNAHME: Wärmetauscher, Hydraulik, Elektro, Glasfaser, Gehäuse; zum Vergleich WP-Einbau 31'500–63'000"),
    "installation_abschreibung_j": (15.0, "ANNAHME"),
    "netz_chf_jahr": (720.0, "ANNAHME: Geschäfts-Glasfaser ≈ 60 CHF/Monat"),
    "betrieb_chf_jahr": (500.0, "ANNAHME: Fernwartung, Versicherung, Abrechnung pro Haus"),
    # --- Rechenzeit (L40S) ---
    "l40s_usd_h_tief": (0.86, "RunPod Juni 2026 ≈ 0,86 $/GPU-h (gpuperhour / DeployBase)"),
    "l40s_usd_h_median": (1.57, "GetDeploying: Median on-demand, 35 Anbieter, 12.11.2026"),
    "l40s_usd_h_aws": (1.86, "AWS g6e.xlarge on-demand (Beam, Devzero)"),
    "pharma_rabatt_vs_aws": (0.25, "ANNAHME: DigitalHeat verkauft 25 % unter AWS (Schweizer Standort, gleiche GPU)"),
    # --- Modelle Haushalt ---
    "waermeabo_rabatt": (0.30, "ANNAHME: Wärmeabo 30 % unter den Energiekosten einer Wärmepumpe"),
}


def w(k):
    return P[k][0]


def gpus_pro_kw():
    return 8 / w("kw_8xl40s")


def hw_chf_pro_kw():
    return w("server_usd_8xl40s") * CHF * (1 + w("aufpreis_fluessigkuehlung")) / w("kw_8xl40s")


def profil_skaliert(ziel_kwh):
    """Heizbedarf so skalieren, dass Heizung + Warmwasser = ziel_kwh (Warmwasser bleibt 12 kWh/Tag)."""
    p = profil_laden()
    ww = sum(z["ww"] for z in p)
    heiz = sum(z["heizung"] for z in p)
    f = (ziel_kwh - ww) / heiz
    return [{**z, "heizung": z["heizung"] * f} for z in p], f


def physik(n, profil, szenario):
    h = Haus(n, szenario, "rechnen", profil)
    for i in range(8760):
        h.schritt(i)
    z = h.z
    return {"n": n, "bedarf": z["bedarf"], "genutzt": z["genutzt"], "backup": z["backup"],
            "strom": z["strom"], "abgefuehrt": z["abgefuehrt"], "server_h": z["strom"] / 1.0,
            "auslastung": z["strom"] / (n * 8760)}


def rechne(ph, haus_name, preis_usd_gpu_h, waermepreis_modell):
    strom = w("strom_chf_kwh")
    waerme_wp = strom / w("jaz_waermepumpe")                                   # CHF/kWh Wärme
    waerme_oel = w("heizoel_chf_l") / (w("heizoel_kwh_l") * w("wirkungsgrad_oelkessel"))
    # --- Haushalt: Heizkosten ohne und mit Serverheizung ---
    vorher_wp = ph["bedarf"] * waerme_wp
    vorher_oel = ph["bedarf"] * waerme_oel
    if waermepreis_modell == "gratis":
        p_waerme = 0.0
    else:  # Wärmeabo
        p_waerme = waerme_wp * (1 - w("waermeabo_rabatt"))
    nachher_wp = ph["backup"] * waerme_wp + ph["genutzt"] * p_waerme
    nachher_oel = ph["backup"] * waerme_oel + ph["genutzt"] * p_waerme
    # vermiedene Wärmepumpe (wenn die Serverheizung den Heizungsersatz ersetzt)
    wp_jahr = (w("wp_neu_chf") - w("wp_foerderung_chf")) / w("wp_lebensdauer_j")
    # --- DigitalHeat ---
    kw = ph["n"]
    hw = kw * hw_chf_pro_kw()
    preis_kwh = preis_usd_gpu_h * CHF * gpus_pro_kw()                       # CHF pro Server-h (1 kW)
    erloes_rechnen = ph["server_h"] * preis_kwh
    erloes_waerme = ph["genutzt"] * p_waerme
    kosten = {
        "strom": ph["strom"] * strom,
        "hardware_abschreibung": hw / w("hw_abschreibung_j"),
        "hardware_unterhalt": hw * w("hw_unterhalt_anteil"),
        "installation_abschreibung": w("installation_chf") / w("installation_abschreibung_j"),
        "netz": w("netz_chf_jahr"),
        "betrieb": w("betrieb_chf_jahr"),
    }
    gewinn = erloes_rechnen + erloes_waerme - sum(kosten.values())
    kosten_ohne_rechnen = sum(kosten.values()) - erloes_waerme
    break_even_gpu_h = kosten_ohne_rechnen / ph["server_h"] / gpus_pro_kw() / CHF
    capex = hw + w("installation_chf")
    return {
        "haus": haus_name, "kw": kw, "waermemodell": waermepreis_modell,
        "rechenpreis_usd_gpu_h": preis_usd_gpu_h,
        "physik": {k: round(v, 3 if k == "auslastung" else 0) for k, v in ph.items()},
        "haushalt": {
            "waermepreis_rp_kwh": round(p_waerme * 100, 2),
            "vorher_wp_chf": round(vorher_wp), "nachher_wp_chf": round(nachher_wp),
            "ersparnis_vs_wp_chf": round(vorher_wp - nachher_wp),
            "vorher_oel_chf": round(vorher_oel), "nachher_oel_chf": round(nachher_oel),
            "ersparnis_vs_oel_chf": round(vorher_oel - nachher_oel),
            "vermiedene_wp_chf_jahr": round(wp_jahr),
            "ersparnis_vs_oel_plus_wp_ersatz_chf": round(vorher_oel - nachher_oel + wp_jahr),
        },
        "digitalheat": {
            "capex_chf": round(capex), "hardware_chf": round(hw),
            "erloes_rechnen_chf": round(erloes_rechnen), "erloes_waerme_chf": round(erloes_waerme),
            "kosten_chf": {k: round(v) for k, v in kosten.items()},
            "gewinn_chf_jahr": round(gewinn),
            "rendite_auf_capex": round(gewinn / capex, 3),
            "amortisation_jahre": round(capex / (gewinn + kosten["hardware_abschreibung"]
                                                 + kosten["installation_abschreibung"]), 1)
            if gewinn + kosten["hardware_abschreibung"] + kosten["installation_abschreibung"] > 0 else None,
            "break_even_usd_gpu_h": round(break_even_gpu_h, 3),
        },
        "pharma": {
            "preis_usd_gpu_h": preis_usd_gpu_h,
            "vs_aws_l40s": round(1 - preis_usd_gpu_h / w("l40s_usd_h_aws"), 3),
            "vs_median": round(1 - preis_usd_gpu_h / w("l40s_usd_h_median"), 3),
            "gpu_h_pro_jahr": round(ph["server_h"] * gpus_pro_kw()),
        },
    }


def main():
    pharma_preis = round(w("l40s_usd_h_aws") * (1 - w("pharma_rabatt_vs_aws")), 3)
    ref = profil_laden()
    durch, f = profil_skaliert(w("durchschnitt_waerme_kwh"))
    fall = []
    for name, profil, n in (("Referenzhaus 31'231 kWh", ref, 8), ("Durchschnitts-EFH 17'000 kWh", durch, 5)):
        for sz in ("spot", "alibaba"):
            ph = physik(n, profil, sz)
            for modell in ("gratis", "waermeabo"):
                for preis in (w("l40s_usd_h_tief"), pharma_preis):
                    r = rechne(ph, name, preis, modell)
                    r["szenario"] = sz
                    fall.append(r)
    aus = ROOT / "daten" / "ergebnisse" / "win_win_win.json"
    aus.write_text(json.dumps({
        "annahmen": {k: {"wert": v, "quelle": q} for k, (v, q) in P.items()},
        "abgeleitet": {"chf_usd": CHF, "gpus_pro_kw": round(gpus_pro_kw(), 2),
                       "hardware_chf_pro_kw": round(hw_chf_pro_kw()),
                       "pharma_preis_usd_gpu_h": pharma_preis, "skalierung_heizung_durchschnitt": round(f, 3)},
        "faelle": fall}, indent=1, ensure_ascii=False))
    print(f"GPUs pro kW {gpus_pro_kw():.2f}, Hardware {hw_chf_pro_kw():,.0f} CHF/kW, Pharma-Preis {pharma_preis} $/GPU-h")
    print("Haus | Szenario | Wärme | $/GPU-h | Deckung | Haushalt spart vs WP / vs Öl | DH Gewinn/J | CAPEX | Amort. J | Break-even $/GPU-h")
    for r in fall:
        ph, hh, dh = r["physik"], r["haushalt"], r["digitalheat"]
        print(f"{r['haus'][:14]:14s} {r['szenario']:7s} {r['waermemodell']:9s} {r['rechenpreis_usd_gpu_h']:5.2f} "
              f"{ph['genutzt'] / ph['bedarf']:6.1%}  {hh['ersparnis_vs_wp_chf']:6,d} / {hh['ersparnis_vs_oel_chf']:6,d}"
              f"   {dh['gewinn_chf_jahr']:8,d}  {dh['capex_chf']:8,d}  {str(dh['amortisation_jahre']):>5s}   {dh['break_even_usd_gpu_h']:.2f}")


if __name__ == "__main__":
    main()
