#!/usr/bin/env python3
"""
Update year 2025 → 2026 in marketing/SEO content.
Skips: © copyright, blog publication dates, legal update dates, image filenames.
"""
import os

BASE = '/Users/neusfigueres/godolphy-static'

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()

def write(p, c):
    with open(p, 'w', encoding='utf-8') as f: f.write(c)

def patch(rel, replacements):
    path = os.path.join(BASE, rel)
    c = read(path)
    changed = False
    for old, new in replacements:
        if old in c:
            c = c.replace(old, new)
            changed = True
            print(f'  OK  {old!r:.70} → {new!r:.30}')
        else:
            print(f'  MISS {old!r:.70}')
    if changed:
        write(path, c)
        print(f'SAVED {rel}')
    return changed

# ── Sectores SEO H2 headings ────────────────────────────────────────────────

patch('sectores/software-para-centro-de-estetica-y-salones/index.html', [
    ('El software para centros de estética que digitaliza tu negocio en 2025',
     'El software para centros de estética que digitaliza tu negocio en 2026'),
])

patch('sectores/software-para-empresas-de-limpieza/index.html', [
    ('Software para empresas de limpieza — Organiza tu equipo y tus servicios en 2025',
     'Software para empresas de limpieza — Organiza tu equipo y tus servicios en 2026'),
])

patch('sectores/software-para-peluquerias/index.html', [
    ('El software de gestión para peluquerías que necesitas en 2025',
     'El software de gestión para peluquerías que necesitas en 2026'),
])

patch('sectores/software-para-salones-de-unas/index.html', [
    ('Software para salones de uñas — Gestiona tu negocio sin caos en 2025',
     'Software para salones de uñas — Gestiona tu negocio sin caos en 2026'),
])

patch('sectores/software-para-spa-y-masajes/index.html', [
    ('Software para spas y centros de masajes — Gestión profesional en 2025',
     'Software para spas y centros de masajes — Gestión profesional en 2026'),
])

# ── Blog article: como-conseguir-mas-clientes ────────────────────────────────

patch('como-conseguir-mas-clientes-salon-de-belleza/index.html', [
    ('Cómo conseguir más clientes para tu salón de belleza en 2025 - Godolphy',
     'Cómo conseguir más clientes para tu salón de belleza en 2026 - Godolphy'),
    ('fideliza clientes en 2025.',
     'fideliza clientes en 2026.'),
    ('Cómo conseguir más clientes para mi salón de belleza en 2025: Guía Completa',
     'Cómo conseguir más clientes para mi salón de belleza en 2026: Guía Completa'),
    ('Con el 2025 ya aquí, los clientes esperan más que nunca',
     'Con el 2026 ya aquí, los clientes esperan más que nunca'),
    ('atraer más clientes a tu salón de belleza en 2025.',
     'atraer más clientes a tu salón de belleza en 2026.'),
])

# ── Blog listing page ────────────────────────────────────────────────────────

patch('blog/index.html', [
    ('Cómo Conseguir Más Clientes para mi salón de Belleza en 2025',
     'Cómo Conseguir Más Clientes para mi salón de Belleza en 2026'),
])

print('\nDone.')
