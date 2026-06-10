#!/usr/bin/env python3
"""Replace dashboard-ia testimonials section with new illustrated card style."""

import re

# ── SVG AVATARS ───────────────────────────────────────────────────────────────
# Each avatar: 48×48px, viewBox 0 0 60 60, inline SVG

def avatar(bg, skin, hair, hair_shape, shirt, beard_color=None):
    """Build an SVG cartoon avatar."""
    # Common elements
    body = f'<ellipse cx="30" cy="66" rx="22" ry="14" fill="{shirt}"/>'
    neck = f'<rect x="24" y="39" width="12" height="9" rx="2" fill="{skin}"/>'
    face = f'<ellipse cx="30" cy="27" rx="13" ry="14" fill="{skin}"/>'
    eyes = (f'<circle cx="25" cy="26" r="1.8" fill="#1a1a1a"/>'
            f'<circle cx="35" cy="26" r="1.8" fill="#1a1a1a"/>')
    smile = '<path d="M25 32 Q30 36.5 35 32" stroke="#1a1a1a" stroke-width="1.4" fill="none" stroke-linecap="round"/>'

    if hair_shape == "long":
        # long hair: back curtain + top
        hair_svg = (
            f'<rect x="13" y="16" width="34" height="38" rx="5" fill="{hair}"/>'
            f'{neck}{face}'
            f'<ellipse cx="30" cy="14" rx="13" ry="7" fill="{hair}"/>'
        )
    elif hair_shape == "bob":
        # bob: sides reach chin level
        hair_svg = (
            f'<rect x="15" y="18" width="30" height="22" rx="4" fill="{hair}"/>'
            f'{neck}{face}'
            f'<ellipse cx="30" cy="14" rx="13" ry="7" fill="{hair}"/>'
            f'<rect x="15" y="24" width="5" height="14" rx="3" fill="{hair}"/>'
            f'<rect x="40" y="24" width="5" height="14" rx="3" fill="{hair}"/>'
        )
    elif hair_shape == "curly":
        # curly/voluminous: blob around head
        hair_svg = (
            f'<ellipse cx="30" cy="20" rx="17" ry="16" fill="{hair}"/>'
            f'<circle cx="14" cy="24" r="7" fill="{hair}"/>'
            f'<circle cx="46" cy="24" r="7" fill="{hair}"/>'
            f'{neck}{face}'
        )
    elif hair_shape == "bun":
        # hair recogido: small bun on top + sides
        hair_svg = (
            f'<ellipse cx="30" cy="15" rx="12" ry="6" fill="{hair}"/>'
            f'<circle cx="30" cy="10" r="6" fill="{hair}"/>'
            f'{neck}{face}'
        )
    elif hair_shape == "short_man":
        # short male hair
        hair_svg = (
            f'{neck}{face}'
            f'<ellipse cx="30" cy="14" rx="13" ry="6" fill="{hair}"/>'
            f'<rect x="17" y="14" width="26" height="6" fill="{hair}"/>'
        )
    elif hair_shape == "short_man_dark":
        hair_svg = (
            f'{neck}{face}'
            f'<ellipse cx="30" cy="14" rx="13.5" ry="7" fill="{hair}"/>'
            f'<rect x="16" y="14" width="28" height="7" fill="{hair}"/>'
        )
    elif hair_shape == "gray_receding":
        # older man: slight recession
        hair_svg = (
            f'{neck}{face}'
            f'<ellipse cx="30" cy="15" rx="13" ry="6" fill="{hair}"/>'
            f'<ellipse cx="22" cy="15" rx="5" ry="5" fill="{hair}"/>'
            f'<ellipse cx="38" cy="15" rx="5" ry="5" fill="{hair}"/>'
        )
    else:
        hair_svg = f'{neck}{face}'

    beard_svg = ""
    if beard_color:
        beard_svg = (f'<ellipse cx="30" cy="36" rx="8" ry="5" fill="{beard_color}" opacity="0.85"/>'
                     f'<rect x="22" y="31" width="16" height="5" fill="{beard_color}" opacity="0.85"/>')

    return (
        f'<svg width="48" height="48" viewBox="0 0 60 60" fill="none" xmlns="http://www.w3.org/2000/svg">'
        f'<circle cx="30" cy="30" r="30" fill="{bg}"/>'
        f'{body}'
        f'{hair_svg}'
        f'{eyes}'
        f'{beard_svg}'
        f'{smile}'
        f'</svg>'
    )


AVATARS = [
    # 1 Laura - pelo largo oscuro
    avatar("#EDE9FE", "#F5CBA7", "#2D1505", "long",        "#8B5CF6"),
    # 2 Silvia - pelo corto castaño
    avatar("#FCE7F3", "#F5CBA7", "#7B4B2A", "bob",         "#EC4899"),
    # 3 Ismael - barba corta
    avatar("#D1FAE5", "#C68642", "#1A1209", "short_man",   "#059669", beard_color="#6B3A1F"),
    # 4 Marta - pelo rizado
    avatar("#FEF3C7", "#C68642", "#4A2C0A", "curly",       "#F59E0B"),
    # 5 Ana - pelo liso rubio
    avatar("#DBEAFE", "#FFE0B2", "#E8C547", "long",        "#3B82F6"),
    # 6 Roberto - moreno sin barba
    avatar("#FEE2E2", "#8B5E3C", "#1A1A1A", "short_man_dark", "#EF4444"),
    # 7 Patricia - pelo recogido
    avatar("#E0F2FE", "#F5CBA7", "#4A3728", "bun",         "#0EA5E9"),
    # 8 Elena - pelo largo rubio
    avatar("#F0FDF4", "#FFE0B2", "#D4A017", "long",        "#10B981"),
    # 9 Javier - mayor pelo canoso
    avatar("#F3F4F6", "#D4956A", "#9CA3AF", "gray_receding", "#6B7280"),
    # 10 Carmen - pelo negro liso
    avatar("#FDF4FF", "#C68642", "#0A0A0A", "long",        "#A855F7"),
]

TESTIMONIOS = [
    ("Tenía un 35% de clientas que habían dejado de venir sin que yo me diera cuenta.", "Laura", "Centro de estética, Madrid"),
    ("Mi servicio más popular era el menos rentable por hora. Lo tenía mal precio desde el principio.", "Silvia", "Peluquera autónoma, Barcelona"),
    ("Estaba dejando ir casi 3.000€ al mes en capacidad sin usar. No lo veía.", "Ismael", "Barbería, Valencia"),
    ("Cuando vi cuánto me costaba cada no-show de verdad, activar los depósitos fue urgente.", "Marta", "Salón de uñas, Bilbao"),
    ("Subí el precio de mi servicio estrella un 15% y no perdí ni una clienta.", "Ana", "Esteticista, Zaragoza"),
    ("Recuperé 23 clientas perdidas en dos semanas con una campaña sencilla.", "Roberto", "Centro de belleza, Málaga"),
    ("Dos servicios consumían el 40% de mi tiempo y generaban el 18% de mis ingresos.", "Patricia", "Peluquera, Alicante"),
    ("Mis clientas VIP eran las que más riesgo tenían de no volver. Nadie lo veía.", "Elena", "Centro de masajes, San Sebastián"),
    ("En 20 años de barbería nunca había tenido datos así de claros.", "Javier", "Barbero, Madrid"),
    ("Los martes por la tarde perdía dinero cada semana sin saber por qué.", "Carmen", "Spa, Sevilla"),
]

STARS = '<span style="color:#FACC15;font-size:13px;letter-spacing:2px;">★★★★★</span>'

def card(text, name, role, svg):
    return f"""      <div style="background:#fff;border-radius:20px;padding:28px;box-shadow:0 4px 20px rgba(98,28,255,0.07);display:flex;flex-direction:column;gap:18px;">
        <div style="display:inline-flex;align-items:center;gap:6px;background:#621CFF;padding:5px 12px;border-radius:20px;width:fit-content;">{STARS}</div>
        <p style="font-family:'Poppins',sans-serif;font-size:15px;color:#1a0033;line-height:1.7;margin:0;">&ldquo;{text}&rdquo;</p>
        <div style="display:flex;align-items:center;gap:12px;">
          {svg}
          <div>
            <div style="font-weight:700;font-size:14px;color:#111827;">{name}</div>
            <div style="font-size:12px;color:#9CA3AF;margin-top:2px;">{role}</div>
          </div>
        </div>
      </div>"""

cards_html = "\n".join(card(t, n, r, svg) for (t, n, r), svg in zip(TESTIMONIOS, AVATARS))

NEW_SECTION = f"""<!-- TESTIMONIOS -->
<section style="padding:80px 24px;background:linear-gradient(135deg,#f5f0ff 0%,#fdf9ff 55%,#ede9fe 100%);">
  <div style="max-width:1060px;margin:0 auto;">
    <h2 style="font-family:'Gabarito',sans-serif;font-size:clamp(26px,3vw,36px);font-weight:700;color:#621CFF;text-align:center;margin:0 0 48px;">La confianza de nuestros clientes</h2>
    <div class="testi-new-grid">
{cards_html}
    </div>
  </div>
</section>"""

# CSS for the responsive grid
GRID_CSS = """
    /* TESTI NEW GRID */
    .testi-new-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
    }
    @media(max-width: 900px) { .testi-new-grid { grid-template-columns: repeat(2, 1fr); } }
    @media(max-width: 580px) { .testi-new-grid { grid-template-columns: 1fr; } }
"""

path = "/Users/neusfigueres/godolphy-static/dashboard-ia/index.html"
with open(path) as f:
    html = f.read()

# 1. Inject grid CSS before </style>
if '.testi-new-grid' not in html:
    html = html.replace('</style>', GRID_CSS + '\n  </style>', 1)

# 2. Replace testimonios section
html = re.sub(
    r'<!-- TESTIMONIOS -->.*?(?=<!-- CTA FINAL -->)',
    NEW_SECTION + '\n\n',
    html, count=1, flags=re.DOTALL
)

with open(path, 'w') as f:
    f.write(html)

print("✓ Done")
