#!/usr/bin/env python3
"""Patch mobile CSS for hero, CTA and DIF sections across key pages."""
import os, glob

BASE = '/Users/neusfigueres/godolphy-static'

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()
def write(p, c):
    with open(p, 'w', encoding='utf-8') as f: f.write(c)

# ─────────────────────────────────────────────────────────────────────────────
# 1. Funcionalidades inner pages
#    All share the same @media(max-width:768px) block ending with `.feat-text h2{font-size:28px;}}
#    We extend it with hero + CTA rules.
# ─────────────────────────────────────────────────────────────────────────────

FUNC_OLD = '.feat-text h2{font-size:28px;}}'
FUNC_ADD = (
    '.feat-text h2{font-size:28px;}'
    'section.hero-bg{padding:80px 20px 60px!important;}'
    'section.hero-bg h1{font-size:32px!important;line-height:1.15!important;}'
    'section.hero-bg p{font-size:15px!important;}'
    'div[style*="padding:80px 60px"]{padding:40px 24px!important;}'
    'h2[style*="font-size:46px"]{font-size:28px!important;}'
    '.faq-btn span{font-size:15px!important;}'
    '}'
)

func_pages = [
    'funcionalidades/reservas-online/index.html',
    'funcionalidades/servicios-a-domicilio/index.html',
    'funcionalidades/pagos-y-depositos/index.html',
    'funcionalidades/equipo-y-horarios/index.html',
    'funcionalidades/calendario/index.html',
    'funcionalidades/chat-y-notificaciones/index.html',
    'funcionalidades/cupones-y-tarjetas-regalo/index.html',
    'funcionalidades/facturacion-y-reporte/index.html',
    'funcionalidades/fidelizacion-ai/index.html',
    'funcionalidades/geolocalizacion-equipo/index.html',
    'funcionalidades/gestion-de-clientes/index.html',
    'funcionalidades/multiples-ubicaciones/index.html',
]

for rel in func_pages:
    path = os.path.join(BASE, rel)
    c = read(path)
    if FUNC_OLD in c:
        c = c.replace(FUNC_OLD, FUNC_ADD, 1)
        write(path, c)
        print(f'OK   {rel}')
    else:
        print(f'WARN {rel} — anchor not found')

# ─────────────────────────────────────────────────────────────────────────────
# 2. Home page — DIF5 banner uses gap:40px flex, not covered by existing rules
# ─────────────────────────────────────────────────────────────────────────────

HOME_OLD = '  div[style*="padding:0 80px"]{padding:0!important;}'
HOME_ADD = (
    '  div[style*="padding:0 80px"]{padding:0!important;}\n'
    '  /* DIF banners: stack on mobile */\n'
    '  div[style*="align-items:center;gap:40px"]{flex-direction:column!important;gap:20px!important;}\n'
    '  div[style*="padding:40px 56px"]{padding:32px 24px!important;}\n'
)

home = os.path.join(BASE, 'index.html')
c = read(home)
if HOME_OLD in c:
    c = c.replace(HOME_OLD, HOME_ADD, 1)
    write(home, c)
    print('OK   index.html')
else:
    print('WARN index.html — anchor not found')

# ─────────────────────────────────────────────────────────────────────────────
# 3. Precio page — DIF5 uses gap:48px flex + padding:48px 56px; also pricing grid
# ─────────────────────────────────────────────────────────────────────────────

PRECIO_OLD = 'div[style*="display:flex;gap:16px;justify-content:center"]{flex-direction:column!important;align-items:center!important;}'
PRECIO_ADD = (
    'div[style*="display:flex;gap:16px;justify-content:center"]{flex-direction:column!important;align-items:center!important;}'
    'div[style*="align-items:center;gap:48px"]{flex-direction:column!important;gap:24px!important;}'
    'div[style*="padding:48px 56px"]{padding:32px 24px!important;}'
    'section[style*="background:#fff;padding:40px 40px 100px"]{padding:32px 20px 60px!important;}'
    'h2[style*="font-size:28px"]{font-size:22px!important;}'
    '.comp-wrap{margin:0 -20px!important;}'
)

precio = os.path.join(BASE, 'precio/index.html')
c = read(precio)
if PRECIO_OLD in c:
    c = c.replace(PRECIO_OLD, PRECIO_ADD, 1)
    write(precio, c)
    print('OK   precio/index.html')
else:
    print('WARN precio/index.html — anchor not found')

# ─────────────────────────────────────────────────────────────────────────────
# 4. Sectores pages — hero H1 already handled, but check CTA padding
#    Sectores pages have CTA: padding:80px 60px — add rule if not present
# ─────────────────────────────────────────────────────────────────────────────

sector_pages = glob.glob(os.path.join(BASE, 'sectores/*/index.html'))
sector_pages.append(os.path.join(BASE, 'sectores/index.html'))

SECT_CTA_RULE = 'div[style*="padding:80px 60px"]{padding:40px 24px!important;}'
SECT_H1_RULE  = 'h1{font-size:36px !important; line-height:1.15 !important;}'

for path in sorted(sector_pages):
    c = read(path)
    rel = os.path.relpath(path, BASE)
    changed = False
    # Add CTA padding fix if not present
    if SECT_CTA_RULE not in c and 'padding:80px 60px' in c:
        # Inject before the closing of the first @media(max-width:768px)
        # Find a reliable anchor: the H1 font-size rule
        if SECT_H1_RULE in c:
            c = c.replace(
                SECT_H1_RULE,
                SECT_H1_RULE + '\n      ' + SECT_CTA_RULE,
                1
            )
            changed = True
    if changed:
        write(path, c)
        print(f'OK   {rel}')
    else:
        print(f'skip {rel} (no changes needed)')

# ─────────────────────────────────────────────────────────────────────────────
# 5. Lista-de-espera — check for any large flex sections not covered
# ─────────────────────────────────────────────────────────────────────────────
# lista-de-espera already has good mobile CSS per earlier check — skip

print('\nDone.')
