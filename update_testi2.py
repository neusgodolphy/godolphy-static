#!/usr/bin/env python3
"""Replace dashboard-ia testimonials with home-style cards."""
import re

TESTIMONIOS = [
    ("Tenía un 35% de clientas que habían dejado de venir sin que yo me diera cuenta.",
     "Laura M.", "Centro de estética, Madrid",
     "LauraM", "ffd5dc"),
    ("Mi servicio más popular era el menos rentable por hora. Lo tenía mal precio desde el principio.",
     "Silvia G.", "Peluquera autónoma, Barcelona",
     "SilviaG", "c0aede"),
    ("Estaba dejando ir casi 3.000€ al mes en capacidad sin usar. No lo veía.",
     "Ismael R.", "Barbería, Valencia",
     "IsmaelR", "b6e3f4"),
    ("Cuando vi cuánto me costaba cada no-show de verdad, activar los depósitos fue urgente.",
     "Marta L.", "Salón de uñas, Bilbao",
     "MartaL", "d1fae5"),
    ("Subí el precio de mi servicio estrella un 15% y no perdí ni una clienta.",
     "Ana P.", "Esteticista, Zaragoza",
     "AnaP", "fef3c7"),
    ("Recuperé 23 clientas perdidas en dos semanas con una campaña sencilla.",
     "Roberto S.", "Centro de belleza, Málaga",
     "RobertoS", "fee2e2"),
    ("Dos servicios consumían el 40% de mi tiempo y generaban el 18% de mis ingresos.",
     "Patricia V.", "Peluquera, Alicante",
     "PatriciaV", "e0f2fe"),
    ("Mis clientas VIP eran las que más riesgo tenían de no volver. Nadie lo veía.",
     "Elena C.", "Centro de masajes, San Sebastián",
     "ElenaC", "f0fdf4"),
    ("En 20 años de barbería nunca había tenido datos así de claros.",
     "Javier M.", "Barbero, Madrid",
     "JavierM", "f3f4f6"),
    ("Los martes por la tarde perdía dinero cada semana sin saber por qué.",
     "Carmen T.", "Spa, Sevilla",
     "CarmenT", "fdf4ff"),
]

STARS = '<div style="margin-bottom:18px;font-size:18px;color:#EEFE3A;background:linear-gradient(90deg,#9B4FE8,#631cff);display:inline-block;padding:4px 10px;border-radius:8px;">★★★★★</div>'

def card(text, name, role, seed, bg):
    avatar_url = f"https://api.dicebear.com/9.x/lorelei/svg?seed={seed}&backgroundColor={bg}"
    return f"""      <div style="background:#f8f7ff;border-radius:20px;padding:36px 32px;border:1.5px solid rgba(99,28,255,.08);">
        {STARS}
        <p style="color:rgba(2,2,30,.75);font-size:16px;line-height:1.7;margin:0 0 28px;">&ldquo;{text}&rdquo;</p>
        <div style="display:flex;align-items:center;gap:14px;">
          <img src="{avatar_url}" width="44" height="44" style="border-radius:50%;flex-shrink:0;background:#f0ebff;" alt="{name}" loading="lazy">
          <div>
            <div style="color:#02021e;font-size:15px;font-weight:600;">{name}</div>
            <div style="color:rgba(2,2,30,.5);font-size:13px;">{role}</div>
          </div>
        </div>
      </div>"""

cards_html = "\n".join(card(t, n, r, s, b) for (t, n, r, s, b) in TESTIMONIOS)

NEW_SECTION = f"""<!-- TESTIMONIOS -->
<section style="background:#fff;padding:95px 40px 100px;">
  <div style="max-width:1320px;margin:0 auto;">
    <div style="text-align:center;margin-bottom:60px;">
      <h2 class="font-gabarito" style="background:linear-gradient(90deg,#9B4FE8,#631cff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;font-size:clamp(36px,5vw,60px);line-height:1.15;font-weight:600;margin:0;">La confianza de nuestros<br>clientes</h2>
    </div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:32px;">
{cards_html}
    </div>
  </div>
</section>

"""

path = "/Users/neusfigueres/godolphy-static/dashboard-ia/index.html"
with open(path) as f:
    html = f.read()

# Remove old testi-new-grid CSS if present
html = re.sub(r'\s*/\* TESTI NEW GRID \*/.*?\.testi-new-grid \{ grid-template-columns: 1fr; \}\s*', '\n', html, flags=re.DOTALL)

# Replace testimonios section
html = re.sub(
    r'<!-- TESTIMONIOS -->.*?(?=<!-- CTA FINAL -->)',
    NEW_SECTION,
    html, count=1, flags=re.DOTALL
)

with open(path, 'w') as f:
    f.write(html)

print("✓ Done")
