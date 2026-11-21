"""Karte: Wo in Basel-Stadt kommt keine Fernwärme hin?

Quelle: Geoportal Basel-Stadt (WFS https://wfs.geo.bs.ch), Teilrichtplan Energie (Energierichtplan):
- ms:EP_Energierichtplan_Fernwaerme   Fernwärme bestehend / geplant (Verbunds- und Eignungsgebiete)
- ms:EP_Energierichtplan_Verbunde     andere Wärmeverbünde (Holz, Grundwasser)
- ms:EP_Energierichtplan_Eignungsgebiet  Gebiete für dezentrale Lösungen (Erdwärme, Umgebungsluft/Sonne)
- ms:BS_Hoheitsgrenzen_Gemeindegrenze Gemeindegrenzen
Abruf in EPSG:4326, gespeichert in daten/roh/geobs/.

Aufruf: python3 src/kunde/karte_fernwaerme.py  -> dashboard/karte_fernwaerme.html
"""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GEO = ROOT / "daten" / "roh" / "geobs"
AUS = ROOT / "dashboard" / "karte_fernwaerme.html"
W, H = 900.0, 760.0
LAT0 = 47.56
KX = 111320 * math.cos(math.radians(LAT0))  # Meter pro Grad Länge
KY = 110540                                 # Meter pro Grad Breite

KLASSEN = {
    "fw_bestehend": ("Fernwärme vorhanden", "var(--fw)"),
    "fw_geplant": ("Fernwärme geplant", "var(--fwp)"),
    "verbund": ("Anderer Wärmeverbund (Holz, Grundwasser)", "var(--vb)"),
    "dezentral": ("Keine Fernwärme: dezentrale Lösung vorgesehen", "var(--ziel)"),
}


def lade(name):
    return json.loads((GEO / f"{name}.geojson").read_text())["features"]


def klasse(p):
    t = p.get("ep_energietraeger", "")
    if t.startswith("Fernwärme bestehend"):
        return "fw_bestehend"
    if t.startswith("Fernwärme geplant"):
        return "fw_geplant"
    if p.get("ep_typ") == "Verbundsgebiet":
        return "verbund"
    return "dezentral"


def ringe(geom):
    if geom["type"] == "Polygon":
        return [geom["coordinates"]]
    if geom["type"] == "MultiPolygon":
        return geom["coordinates"]
    return []


def flaeche_m2(poly):
    """Planare Fläche eines Polygons (äusserer Ring minus Löcher), lokal in Meter projiziert."""
    def ring(r):
        s = 0.0
        for (x1, y1), (x2, y2) in zip(r, r[1:]):
            s += (x1 * KX) * (y2 * KY) - (x2 * KX) * (y1 * KY)
        return abs(s) / 2
    return ring(poly[0]) - sum(ring(r) for r in poly[1:])


def main():
    flaechen = []
    for name in ("EP_Energierichtplan_Eignungsgebiet", "EP_Energierichtplan_Verbunde", "EP_Energierichtplan_Fernwaerme"):
        for f in lade(name):
            flaechen.append((klasse(f["properties"]), f["properties"], ringe(f["geometry"])))
    grenzen = [f["geometry"] for f in lade("BS_Hoheitsgrenzen_Gemeindegrenze")]

    xs = [c[0] for _, _, polys in flaechen for p in polys for r in p for c in r]
    ys = [c[1] for _, _, polys in flaechen for p in polys for r in p for c in r]
    for g in grenzen:
        for c in (g["coordinates"] if g["type"] == "LineString" else [c for l in g["coordinates"] for c in l]):
            xs.append(c[0]); ys.append(c[1])
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    s = min((W - 20) / ((x1 - x0) * KX), (H - 20) / ((y1 - y0) * KY))

    def pt(c):
        return f"{10 + (c[0] - x0) * KX * s:.1f},{10 + (y1 - c[1]) * KY * s:.1f}"

    def pfad(polys):
        return " ".join("M" + " L".join(pt(c) for c in r) + "Z" for p in polys for r in p)

    summe = {k: 0.0 for k in KLASSEN}
    teile = []
    reihenfolge = {"dezentral": 0, "verbund": 1, "fw_geplant": 2, "fw_bestehend": 3}
    for k, p, polys in sorted(flaechen, key=lambda t: reihenfolge[t[0]]):
        a = sum(flaeche_m2(poly) for poly in polys) / 1e6
        summe[k] += a
        name = p.get("ep_gebiet") if p.get("ep_gebiet") not in (None, "-") else p.get("ep_energietraeger")
        tip = f"{name} · {p.get('ep_energietraeger')} · {a:.2f} km²"
        teile.append(f'<path class="f {k}" d="{pfad(polys)}" fill-rule="evenodd"><title>{tip}</title></path>')
    linien = []
    for g in grenzen:
        ls = [g["coordinates"]] if g["type"] == "LineString" else g["coordinates"]
        for l in ls:
            linien.append(f'<path class="grenze" d="M{" L".join(pt(c) for c in l)}"/>')

    # Ortsnamen (ungefähre Lage, nur Beschriftung)
    orte = [("Basel", 7.588, 47.556), ("Riehen", 7.651, 47.583), ("Bettingen", 7.668, 47.569), ("Bruderholz", 7.597, 47.532)]
    labels = "".join(f'<text class="ort" x="{pt((lo, la)).split(",")[0]}" y="{pt((lo, la)).split(",")[1]}">{n}</text>'
                     for n, lo, la in orte)

    kanton_km2 = 37.0
    zeilen = "".join(f'<tr><td><i style="background:{farbe}"></i>{text}</td><td class="num">{summe[k]:.1f} km²</td></tr>'
                     for k, (text, farbe) in KLASSEN.items())
    html = f"""<!doctype html>
<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Basel ohne Fernwärme</title>
<style>
:root {{ color-scheme: light; --bg:#f9f9f7; --surface:#fcfcfb; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781; --ring:rgba(11,11,11,.1);
  --fw:#b7c2cf; --fwp:#dde3ea; --vb:#c9c2dd; --ziel:#eb6834; --grenze:#52514e; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ color-scheme: dark; --bg:#0d0d0d; --surface:#1a1a19; --ink:#f0efec; --ink2:#c3c2b7; --muted:#898781; --ring:rgba(255,255,255,.1);
  --fw:#4b5867; --fwp:#2f3842; --vb:#4a4560; --ziel:#d95926; --grenze:#c3c2b7; }} }}
:root[data-theme="dark"] {{ color-scheme: dark; --bg:#0d0d0d; --surface:#1a1a19; --ink:#f0efec; --ink2:#c3c2b7; --muted:#898781; --ring:rgba(255,255,255,.1);
  --fw:#4b5867; --fwp:#2f3842; --vb:#4a4560; --ziel:#d95926; --grenze:#c3c2b7; }}
body {{ margin:0; background:var(--bg); color:var(--ink); font:15px/1.45 system-ui,-apple-system,"Segoe UI",sans-serif; }}
main {{ max-width:1000px; margin:0 auto; padding-block:24px 48px; padding-left:max(16px, env(safe-area-inset-left,0px)); padding-right:max(16px, env(safe-area-inset-right,0px)); }}
h1 {{ font-size:24px; margin:0 0 4px; }} .sub {{ color:var(--ink2); margin:0 0 16px; max-width:70ch; }}
.card {{ background:var(--surface); border:1px solid var(--ring); border-radius:12px; padding:16px; }}
.grid {{ display:grid; grid-template-columns: 1fr 300px; gap:16px; align-items:start; }}
@media (max-width:800px) {{ .grid {{ grid-template-columns:1fr; }} }}
svg {{ width:100%; height:auto; display:block; }}
.f {{ stroke: var(--surface); stroke-width:.6; }}
.fw_bestehend {{ fill:var(--fw); }} .fw_geplant {{ fill:var(--fwp); }} .verbund {{ fill:var(--vb); }} .dezentral {{ fill:var(--ziel); fill-opacity:.85; }}
.f:hover {{ stroke: var(--ink); stroke-width:1.5; }}
.grenze {{ fill:none; stroke:var(--grenze); stroke-width:1.2; stroke-dasharray:none; }}
.ort {{ fill:var(--ink); font-size:15px; font-weight:650; paint-order:stroke; stroke:var(--surface); stroke-width:3px; text-anchor:middle; }}
table {{ border-collapse:collapse; width:100%; font-size:14px; }} td {{ padding:5px 4px; border-bottom:1px solid var(--ring); }}
td.num {{ text-align:right; font-variant-numeric:tabular-nums; }} td i {{ display:inline-block; width:11px; height:11px; border-radius:3px; margin-right:8px; vertical-align:-1px; }}
.note {{ color:var(--muted); font-size:13px; }} ul {{ padding-left:18px; margin:8px 0; color:var(--ink2); font-size:14px; }}
</style></head><body><main>
<h1>Wo kommt in Basel keine Fernwärme hin?</h1>
<p class="sub">Energierichtplan Basel-Stadt: Orange sind Gebiete, in denen der Kanton keine Fernwärme vorsieht. Dort müssen Gas- und Ölheizungen durch dezentrale Lösungen ersetzt werden, und dort passt die Serverheizung.</p>
<div class="grid">
<div class="card"><svg viewBox="0 0 {W:.0f} {H:.0f}" role="img" aria-label="Karte Basel-Stadt mit Fernwärmegebieten">
{''.join(teile)}{''.join(linien)}{labels}</svg>
<div class="note">Fahre mit der Maus über eine Fläche für Name, Energieträger und Fläche.</div></div>
<div class="card"><table>{zeilen}<tr><td>Kanton Basel-Stadt total</td><td class="num">≈ {kanton_km2:.0f} km²</td></tr></table>
<ul>
<li><b>Zielgebiete</b> für die Serverheizung sind die orangen Flächen: vor allem das <b>Bruderholz</b> im Süden, <b>Riehen</b>, <b>Bettingen</b> und Teile am Westrand von Basel. Dort stehen viele Einfamilienhäuser.</li>
<li>In den grauen Gebieten ist Fernwärme die naheliegende Lösung. Die kantonale Förderung für dezentrale Heizungen ist dort halbiert.</li>
<li>Weisse Flächen sind im Energierichtplan keiner Kategorie zugeordnet (z. B. Rhein, Wald, Gewerbe).</li><li>Flächen können sich überlagern. Die Summe ist deshalb eine Näherung.</li>
</ul>
<p class="note">Quelle: Geoportal Basel-Stadt, Teilrichtplan Energie (WFS ms:EP_Energierichtplan_Fernwaerme, _Verbunde, _Eignungsgebiet, BS_Hoheitsgrenzen_Gemeindegrenze), abgerufen 21.11.2026. Flächen eigene Berechnung. Ortsnamen ungefähr platziert.</p></div>
</div></main></body></html>"""
    AUS.write_text(html)
    print(AUS.relative_to(ROOT), f"{AUS.stat().st_size / 1e3:.0f} kB")
    for k, (t, _) in KLASSEN.items():
        print(f"  {t}: {summe[k]:.2f} km²")


if __name__ == "__main__":
    main()
