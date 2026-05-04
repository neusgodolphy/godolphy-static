#!/usr/bin/env python3
"""
PARTE 1: Add new rows to /precio/ comparison table
PARTE 2: Add payment config section to /funcionalidades/pagos-y-depositos/
PARTE 3: Add brand + extras sections to /funcionalidades/reservas-online/
"""
import os

BASE = '/Users/neusfigueres/godolphy-static'

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()
def write(p, c):
    with open(p, 'w', encoding='utf-8') as f: f.write(c)

CHECK = '<svg class="check" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>'
DASH  = '<span class="val-dash">—</span>'

def row(name, solo, pro, max_):
    def cell(v): return f'<td>{CHECK if v else DASH}</td>'
    return f'\n          <tr><td>{name}</td>{cell(solo)}{cell(pro)}{cell(max_)}</tr>'

# ─────────────────────────────────────────────────────────────────────────────
# PARTE 1 — /precio/ new table rows
# ─────────────────────────────────────────────────────────────────────────────

PRECIO_PATH = os.path.join(BASE, 'precio/index.html')
c = read(PRECIO_PATH)

# --- Reservas y agenda: remove "Dominio propio" row, add new rows before <!-- EQUIPO --> ---
# First: replace "Dominio propio" row with "Personalización de la página de reservas"
OLD_DOMINIO = '<tr><td>Dominio propio en reservas</td><td><span class="val-dash">—</span></td><td><span class="val-dash">—</span></td><td>' + CHECK + '</td></tr>'
NEW_PERSONALIZ = '<tr><td>Personalización de la página de reservas (logo y color de marca)</td><td>' + CHECK + '</td><td>' + CHECK + '</td><td>' + CHECK + '</td></tr>'

if OLD_DOMINIO in c:
    c = c.replace(OLD_DOMINIO, NEW_PERSONALIZ, 1)
    print('OK   precio: replaced Dominio propio row with Personalización')
else:
    print('WARN precio: Dominio propio row not found, appending Personalización separately')

# Rows to add before <!-- EQUIPO -->
new_reservas_rows = (
    row('Extras por servicio (tiempo y precio)', True, True, True) +
    row('Tipos de ubicación del cliente', False, True, True) +
    row('Precio de desplazamiento por zonas', False, True, True)
)

EQUIPO_ANCHOR = '\n          <!-- EQUIPO -->'
c = c.replace(EQUIPO_ANCHOR, new_reservas_rows + EQUIPO_ANCHOR, 1)
print('OK   precio: added 3 rows to Reservas y agenda')

# --- Equipo: add rows before <!-- CLIENTES --> ---
new_equipo_rows = (
    row('Precio y duración por profesional', False, True, True) +
    row('Horarios especiales y festivos', True, True, True)
)

CLIENTES_ANCHOR = '\n          <!-- CLIENTES -->'
c = c.replace(CLIENTES_ANCHOR, new_equipo_rows + CLIENTES_ANCHOR, 1)
print('OK   precio: added 2 rows to Equipo')

# --- Clientes: add rows before <!-- PAGOS --> ---
new_clientes_rows = row('Venta de tarjetas regalo online', False, True, True)

PAGOS_ANCHOR = '\n          <!-- PAGOS -->'
c = c.replace(PAGOS_ANCHOR, new_clientes_rows + PAGOS_ANCHOR, 1)
print('OK   precio: added 1 row to Clientes')

# --- Notificaciones: add rows before <!-- ONBOARDING --> or end of section ---
new_notif_rows = row('Solicitud de reseña post-servicio', False, True, True)

# Find ONBOARDING anchor
ONBOARDING_ANCHOR = '\n          <!-- ONBOARDING'
if ONBOARDING_ANCHOR not in c:
    # Try other patterns
    ONBOARDING_ANCHOR = '\n          <!-- SOPORTE'
if ONBOARDING_ANCHOR not in c:
    # Find "Onboarding y soporte" header
    import re
    m = re.search(r'\n\s+<!-- [A-Z]+ -->\s*\n\s+<tr class="sect-hd"><td>Onboarding', c)
    if m:
        ONBOARDING_ANCHOR = c[m.start():m.start()+30]

if ONBOARDING_ANCHOR in c:
    c = c.replace(ONBOARDING_ANCHOR, new_notif_rows + ONBOARDING_ANCHOR, 1)
    print('OK   precio: added 1 row to Notificaciones')
else:
    # Fallback: inject after last notificaciones row - find the section end
    notif_idx = c.find('<!-- NOTIFICACIONES -->')
    # Find next section after notificaciones
    next_section = c.find('<tr class="sect-hd">', notif_idx + 50)
    if next_section != -1:
        # inject before the next section header's preceding comment
        prev_comment = c.rfind('<!--', notif_idx, next_section)
        if prev_comment != -1:
            insert_at = c.rfind('\n', 0, prev_comment) + 1
            c = c[:insert_at] + new_notif_rows[1:] + '\n' + c[insert_at:]
            print('OK   precio: added 1 row to Notificaciones (fallback)')
        else:
            print('WARN precio: could not find Notificaciones section end')
    else:
        print('WARN precio: no next section after Notificaciones')

write(PRECIO_PATH, c)
print('SAVED precio/index.html')
print()

# ─────────────────────────────────────────────────────────────────────────────
# PARTE 2 — /funcionalidades/pagos-y-depositos/ new section
# ─────────────────────────────────────────────────────────────────────────────

PAGOS_PATH = os.path.join(BASE, 'funcionalidades/pagos-y-depositos/index.html')
c = read(PAGOS_PATH)
GUARD2 = 'PAGOS_CONFIG_SECTION'

if GUARD2 in c:
    print('SKIP pagos-y-depositos: already patched')
else:
    SECTION = f'''
<!-- {GUARD2} -->
<section style="background:#f8f7ff;padding:96px 40px;">
  <div style="max-width:900px;margin:0 auto;">
    <h2 class="font-gabarito" style="font-size:38px;font-weight:700;color:#02021e;margin:0 0 16px;line-height:1.15;">Configura exactamente cómo y cuándo cobras</h2>
    <p style="color:rgba(2,2,30,.65);font-size:17px;line-height:1.75;margin:0 0 56px;">Godolphy te da control total sobre la gestión de pagos de tu negocio. Desde la pantalla de configuración puedes definir cada detalle.</p>

    <div style="display:grid;grid-template-columns:1fr 1fr;gap:32px;margin-bottom:32px;">

      <div style="background:#fff;border-radius:20px;padding:36px;">
        <div style="width:44px;height:44px;background:linear-gradient(135deg,#9B4FE8,#631cff);border-radius:12px;display:flex;align-items:center;justify-content:center;margin-bottom:20px;">
          <svg width="22" height="22" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" viewBox="0 0 24 24"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
        </div>
        <h3 class="font-gabarito" style="font-size:20px;font-weight:700;color:#02021e;margin:0 0 12px;">¿Cobras al reservar o después?</h3>
        <p style="color:rgba(2,2,30,.65);font-size:15px;line-height:1.7;margin:0;">Elige si el cliente paga el servicio completo al reservar o solo un depósito. El depósito puede ser un importe fijo o un porcentaje del total — tú decides.</p>
      </div>

      <div style="background:#fff;border-radius:20px;padding:36px;">
        <div style="width:44px;height:44px;background:linear-gradient(135deg,#9B4FE8,#631cff);border-radius:12px;display:flex;align-items:center;justify-content:center;margin-bottom:20px;">
          <svg width="22" height="22" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
        </div>
        <h3 class="font-gabarito" style="font-size:20px;font-weight:700;color:#02021e;margin:0 0 12px;">Cobro automático del resto</h3>
        <p style="color:rgba(2,2,30,.65);font-size:15px;line-height:1.7;margin:0;">Si el cliente pagó solo el depósito, el sistema cobra automáticamente el importe restante. Elige cuándo: 15 minutos después de empezar la cita, al finalizar, o cuando el profesional marque el servicio como completado.</p>
      </div>

      <div style="background:#fff;border-radius:20px;padding:36px;">
        <div style="width:44px;height:44px;background:linear-gradient(135deg,#9B4FE8,#631cff);border-radius:12px;display:flex;align-items:center;justify-content:center;margin-bottom:20px;">
          <svg width="22" height="22" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" viewBox="0 0 24 24"><path d="M9 14l-4-4 4-4"/><path d="M5 10h11a4 4 0 0 1 0 8h-1"/></svg>
        </div>
        <h3 class="font-gabarito" style="font-size:20px;font-weight:700;color:#02021e;margin:0 0 12px;">Política de cancelación</h3>
        <p style="color:rgba(2,2,30,.65);font-size:15px;line-height:1.7;margin:0 0 12px;">Define qué pasa si el cliente cancela fuera de plazo o no aparece. Puedes configurar por separado cancelación tardía y no-show:</p>
        <ul style="list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:6px;">
          <li style="color:rgba(2,2,30,.65);font-size:14px;">· Devolver el depósito completo</li>
          <li style="color:rgba(2,2,30,.65);font-size:14px;">· Retener el depósito</li>
          <li style="color:rgba(2,2,30,.65);font-size:14px;">· Cobrar el servicio completo</li>
        </ul>
      </div>

      <div style="background:#fff;border-radius:20px;padding:36px;">
        <div style="width:44px;height:44px;background:linear-gradient(135deg,#9B4FE8,#631cff);border-radius:12px;display:flex;align-items:center;justify-content:center;margin-bottom:20px;">
          <svg width="22" height="22" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
        </div>
        <h3 class="font-gabarito" style="font-size:20px;font-weight:700;color:#02021e;margin:0 0 12px;">Precio de desplazamiento por zonas</h3>
        <p style="color:rgba(2,2,30,.65);font-size:15px;line-height:1.7;margin:0 0 12px;">Para servicios a domicilio, define zonas con precio extra automático. El sistema calcula la zona del cliente al reservar y añade el coste al total:</p>
        <ul style="list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:6px;">
          <li style="color:rgba(2,2,30,.65);font-size:14px;">· 0–5 km → sin cargo</li>
          <li style="color:rgba(2,2,30,.65);font-size:14px;">· 5–10 km → +10€</li>
          <li style="color:rgba(2,2,30,.65);font-size:14px;">· 10–15 km → +20€</li>
        </ul>
      </div>

    </div>

    <div style="background:linear-gradient(135deg,#02021e,#1a0a4a);border-radius:20px;padding:36px;display:flex;gap:32px;flex-wrap:wrap;">
      <div style="flex:1;min-width:200px;display:flex;align-items:flex-start;gap:14px;">
        <div style="flex-shrink:0;width:36px;height:36px;background:rgba(255,255,255,.1);border-radius:10px;display:flex;align-items:center;justify-content:center;">
          <svg width="18" height="18" fill="none" stroke="#EEFE3A" stroke-width="2" viewBox="0 0 24 24"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
        </div>
        <div><p style="color:#fff;font-size:14px;font-weight:600;margin:0 0 4px;">Sin comisiones por transacción</p><p style="color:rgba(255,255,255,.55);font-size:13px;margin:0;">Solo pagas la cuota mensual de Godolphy.</p></div>
      </div>
      <div style="flex:1;min-width:200px;display:flex;align-items:flex-start;gap:14px;">
        <div style="flex-shrink:0;width:36px;height:36px;background:rgba(255,255,255,.1);border-radius:10px;display:flex;align-items:center;justify-content:center;">
          <svg width="18" height="18" fill="none" stroke="#EEFE3A" stroke-width="2" viewBox="0 0 24 24"><rect x="1" y="4" width="22" height="16" rx="2"/><line x1="1" y1="10" x2="23" y2="10"/></svg>
        </div>
        <div><p style="color:#fff;font-size:14px;font-weight:600;margin:0 0 4px;">Stripe, TPV físico y efectivo</p><p style="color:rgba(255,255,255,.55);font-size:13px;margin:0;">Tú decides cómo cobras en cada caso.</p></div>
      </div>
      <div style="flex:1;min-width:200px;display:flex;align-items:flex-start;gap:14px;">
        <div style="flex-shrink:0;width:36px;height:36px;background:rgba(255,255,255,.1);border-radius:10px;display:flex;align-items:center;justify-content:center;">
          <svg width="18" height="18" fill="none" stroke="#EEFE3A" stroke-width="2" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
        </div>
        <div><p style="color:#fff;font-size:14px;font-weight:600;margin:0 0 4px;">Sin IVA europeo</p><p style="color:rgba(255,255,255,.55);font-size:13px;margin:0;">Godolphy opera como LLC en EE.UU. El precio que ves es el final.</p></div>
      </div>
    </div>

  </div>
</section>
'''

    # Inject before the SEO_TEXT_BLOCK section (or before footer if no SEO block)
    if 'SEO_TEXT_BLOCK' in c:
        # Find the section opening tag that contains SEO_TEXT_BLOCK
        seo_idx = c.find('SEO_TEXT_BLOCK')
        section_start = c.rfind('<section', 0, seo_idx)
        c = c[:section_start] + SECTION + '\n' + c[section_start:]
    else:
        footer_idx = c.find('<footer')
        c = c[:footer_idx] + SECTION + '\n' + c[footer_idx:]

    write(PAGOS_PATH, c)
    print('OK   funcionalidades/pagos-y-depositos: added payment config section')

print()

# ─────────────────────────────────────────────────────────────────────────────
# PARTE 3 — /funcionalidades/reservas-online/ two new sections
# ─────────────────────────────────────────────────────────────────────────────

RESERVAS_PATH = os.path.join(BASE, 'funcionalidades/reservas-online/index.html')
c = read(RESERVAS_PATH)
GUARD3A = 'RESERVAS_BRAND_SECTION'
GUARD3B = 'RESERVAS_EXTRAS_SECTION'

BRAND_SECTION = f'''
<!-- {GUARD3A} -->
<section style="background:#f8f7ff;padding:96px 40px;">
  <div style="max-width:900px;margin:0 auto;display:flex;align-items:center;gap:64px;">
    <div style="flex:1;">
      <h2 class="font-gabarito" style="font-size:38px;font-weight:700;color:#02021e;margin:0 0 20px;line-height:1.15;">Tu marca en cada reserva</h2>
      <p style="color:rgba(2,2,30,.7);font-size:17px;line-height:1.75;margin:0 0 20px;">La página de reservas de Godolphy no es una página genérica. Desde el primer clic, tu cliente ve tu logo y tus colores — en todos los planes, sin coste adicional.</p>
      <p style="color:rgba(2,2,30,.7);font-size:17px;line-height:1.75;margin:0 0 28px;">En la configuración del negocio defines el logo que aparece en la página de reservas y en las notificaciones, y el color primario de tu marca para botones y elementos visuales. El resultado es una experiencia coherente que transmite profesionalidad y confianza desde el primer clic.</p>
      <div style="display:flex;flex-direction:column;gap:14px;">
        <div style="display:flex;align-items:center;gap:12px;">
          <svg width="20" height="20" fill="url(#checkGrad)" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
          <span style="color:rgba(2,2,30,.8);font-size:16px;">Tu logo en la página de reservas y en los emails</span>
        </div>
        <div style="display:flex;align-items:center;gap:12px;">
          <svg width="20" height="20" fill="url(#checkGrad)" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
          <span style="color:rgba(2,2,30,.8);font-size:16px;">Color de marca en botones y elementos visuales</span>
        </div>
        <div style="display:flex;align-items:center;gap:12px;">
          <svg width="20" height="20" fill="url(#checkGrad)" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
          <span style="color:rgba(2,2,30,.8);font-size:16px;">Disponible en todos los planes desde el primer día</span>
        </div>
      </div>
    </div>
    <div style="flex:1;background:linear-gradient(135deg,#f0ebff,#e0d5ff);border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:16px;">
      <div style="background:#fff;border-radius:14px;padding:20px 24px;display:flex;align-items:center;gap:16px;box-shadow:0 2px 12px rgba(99,28,255,.08);">
        <div style="width:40px;height:40px;background:linear-gradient(135deg,#9B4FE8,#631cff);border-radius:10px;flex-shrink:0;"></div>
        <div><p style="color:#02021e;font-size:14px;font-weight:600;margin:0;">Tu logo aquí</p><p style="color:rgba(2,2,30,.4);font-size:12px;margin:0;">Formato PNG o SVG recomendado</p></div>
      </div>
      <div style="background:#fff;border-radius:14px;padding:20px 24px;box-shadow:0 2px 12px rgba(99,28,255,.08);">
        <p style="color:rgba(2,2,30,.5);font-size:12px;font-weight:600;margin:0 0 10px;letter-spacing:.05em;">COLOR PRIMARIO</p>
        <div style="display:flex;gap:10px;">
          <div style="width:32px;height:32px;border-radius:8px;background:#631cff;"></div>
          <div style="width:32px;height:32px;border-radius:8px;background:#9B4FE8;"></div>
          <div style="width:32px;height:32px;border-radius:8px;background:#02021e;"></div>
          <div style="width:32px;height:32px;border-radius:8px;background:#EEFE3A;border:1px solid rgba(0,0,0,.08);"></div>
        </div>
      </div>
      <div style="background:#631cff;border-radius:14px;padding:16px 24px;text-align:center;">
        <span style="color:#fff;font-size:15px;font-weight:600;">Reservar cita →</span>
      </div>
    </div>
  </div>
</section>
'''

EXTRAS_SECTION = f'''
<!-- {GUARD3B} -->
<section style="background:#fff;padding:96px 40px;">
  <div style="max-width:900px;margin:0 auto;">
    <div style="text-align:center;margin-bottom:56px;">
      <h2 class="font-gabarito" style="font-size:38px;font-weight:700;color:#02021e;margin:0 0 16px;line-height:1.15;">Servicios personalizables con extras</h2>
      <p style="color:rgba(2,2,30,.6);font-size:17px;line-height:1.65;max-width:620px;margin:0 auto;">Cada servicio puede tener opciones extras que el cliente selecciona al reservar — con tiempo y precio adicional automático. Sin cálculos manuales.</p>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:24px;margin-bottom:48px;">
      <div style="border:1px solid rgba(2,2,30,.08);border-radius:16px;padding:28px;">
        <div style="font-size:28px;margin-bottom:12px;">💅</div>
        <p style="color:#02021e;font-size:15px;font-weight:600;margin:0 0 8px;">Manicura básica</p>
        <p style="color:rgba(2,2,30,.5);font-size:13px;margin:0 0 12px;">45 min · 25€</p>
        <div style="background:#f8f7ff;border-radius:8px;padding:10px 12px;">
          <p style="color:#631cff;font-size:13px;font-weight:600;margin:0 0 4px;">+ Gel de color</p>
          <p style="color:rgba(2,2,30,.5);font-size:12px;margin:0;">+15 min · +15€</p>
        </div>
      </div>
      <div style="border:1px solid rgba(2,2,30,.08);border-radius:16px;padding:28px;">
        <div style="font-size:28px;margin-bottom:12px;">💆</div>
        <p style="color:#02021e;font-size:15px;font-weight:600;margin:0 0 8px;">Masaje relajante</p>
        <p style="color:rgba(2,2,30,.5);font-size:13px;margin:0 0 12px;">60 min · 50€</p>
        <div style="background:#f8f7ff;border-radius:8px;padding:10px 12px;">
          <p style="color:#631cff;font-size:13px;font-weight:600;margin:0 0 4px;">+ Aromaterapia</p>
          <p style="color:rgba(2,2,30,.5);font-size:12px;margin:0;">+10 min · +10€</p>
        </div>
      </div>
      <div style="border:1px solid rgba(2,2,30,.08);border-radius:16px;padding:28px;">
        <div style="font-size:28px;margin-bottom:12px;">✂️</div>
        <p style="color:#02021e;font-size:15px;font-weight:600;margin:0 0 8px;">Corte de pelo</p>
        <p style="color:rgba(2,2,30,.5);font-size:13px;margin:0 0 12px;">45 min · 30€</p>
        <div style="background:#f8f7ff;border-radius:8px;padding:10px 12px;">
          <p style="color:#631cff;font-size:13px;font-weight:600;margin:0 0 4px;">+ Tratamiento hidratante</p>
          <p style="color:rgba(2,2,30,.5);font-size:12px;margin:0;">+20 min · +20€</p>
        </div>
      </div>
    </div>
    <div style="background:#f8f7ff;border-radius:20px;padding:36px;display:flex;gap:32px;flex-wrap:wrap;">
      <div style="flex:1;min-width:180px;">
        <p style="color:#631cff;font-size:13px;font-weight:600;letter-spacing:.05em;margin:0 0 6px;">TIEMPO AUTOMÁTICO</p>
        <p style="color:#02021e;font-size:15px;font-weight:600;margin:0 0 4px;">La agenda se bloquea con la duración exacta total</p>
        <p style="color:rgba(2,2,30,.55);font-size:14px;margin:0;">Servicio + todos los extras seleccionados.</p>
      </div>
      <div style="flex:1;min-width:180px;">
        <p style="color:#631cff;font-size:13px;font-weight:600;letter-spacing:.05em;margin:0 0 6px;">PRECIO AUTOMÁTICO</p>
        <p style="color:#02021e;font-size:15px;font-weight:600;margin:0 0 4px;">El total se calcula y cobra sin intervención manual</p>
        <p style="color:rgba(2,2,30,.55);font-size:14px;margin:0;">El cliente ve el precio final antes de confirmar.</p>
      </div>
      <div style="flex:1;min-width:180px;">
        <p style="color:#631cff;font-size:13px;font-weight:600;letter-spacing:.05em;margin:0 0 6px;">TÚ CONFIGURAS LAS REGLAS</p>
        <p style="color:#02021e;font-size:15px;font-weight:600;margin:0 0 4px;">Extras opcionales o obligatorios</p>
        <p style="color:rgba(2,2,30,.55);font-size:14px;margin:0;">Selección única o múltiple según el servicio.</p>
      </div>
    </div>
  </div>
</section>
'''

if GUARD3A in c and GUARD3B in c:
    print('SKIP reservas-online: already patched')
else:
    # Inject both sections before the FAQ section (Preguntas frecuentes)
    faq_idx = c.find('Preguntas frecuentes')
    if faq_idx == -1:
        faq_idx = c.find('<footer')
    section_start = c.rfind('<section', 0, faq_idx)

    if GUARD3A not in c:
        c = c[:section_start] + BRAND_SECTION + '\n' + c[section_start:]
        print('OK   reservas-online: added Tu marca en cada reserva section')
    if GUARD3B not in c:
        # Re-find FAQ after inserting brand section
        faq_idx = c.find('Preguntas frecuentes')
        if faq_idx == -1:
            faq_idx = c.find('<footer')
        section_start = c.rfind('<section', 0, faq_idx)
        c = c[:section_start] + EXTRAS_SECTION + '\n' + c[section_start:]
        print('OK   reservas-online: added Servicios personalizables con extras section')

    write(RESERVAS_PATH, c)

print('\nAll done.')
