#!/usr/bin/env python3
import os, re

BASE = '/Users/neusfigueres/godolphy-static'

# SVG check bullet
BULLET_SVG = '<svg width="18" height="18" viewBox="0 0 20 20" fill="#631cff"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>'

def bullet(text):
    return f'<div class="bullet">{BULLET_SVG}<span>{text}</span></div>'

def icon_visual(icon_path, bg='linear-gradient(135deg,#f0ebff,#e0d5ff)', accent='#631cff'):
    """Styled icon in a rounded square — used as right column when no image exists."""
    return (
        f'<div style="background:{bg};border-radius:24px;min-height:340px;display:flex;align-items:center;justify-content:center;">'
        f'<svg width="96" height="96" viewBox="0 0 24 24" fill="none" stroke="{accent}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">{icon_path}</svg>'
        f'</div>'
    )

def feat_section(h2, body_html, visual_html, alt=False, rev=False):
    bg = ' alt' if alt else ''
    direction = ' rev' if rev else ''
    return (
        f'\n<section class="feat-section{bg}">\n'
        f'  <div class="feat-content{direction}">\n'
        f'    <div class="feat-text">\n'
        f'      <h2>{h2}</h2>\n'
        f'      {body_html}\n'
        f'    </div>\n'
        f'    {visual_html}\n'
        f'  </div>\n'
        f'</section>\n'
    )

def highlight_box(text):
    """A styled callout or highlight block."""
    return (
        f'<div style="background:#f0ebff;border-left:3px solid #631cff;border-radius:0 12px 12px 0;padding:16px 20px;margin:20px 0;color:#3a0aaa;font-size:14px;line-height:1.65;">'
        f'{text}</div>'
    )

def policy_row(condition, action, color='#631cff'):
    return (
        f'<div style="display:flex;align-items:flex-start;gap:12px;padding:14px 0;border-bottom:1px solid rgba(2,2,30,.07);">'
        f'<div style="flex-shrink:0;margin-top:2px;width:8px;height:8px;border-radius:50%;background:{color};margin-top:7px;"></div>'
        f'<div><span style="font-size:15px;font-weight:600;color:#02021e;">{condition}</span>'
        f'<span style="font-size:15px;color:rgba(2,2,30,.6);"> → {action}</span></div>'
        f'</div>'
    )

# ─────────────────────────────────────────────────────────────────────────────
# SECTION BUILDERS
# ─────────────────────────────────────────────────────────────────────────────

# Dif 1 — Cesta múltiple (full version for reservas-online)
CESTA_VISUAL = (
    '<div style="background:linear-gradient(135deg,#f0ebff,#e0d5ff);border-radius:24px;padding:32px;">'
    '<div style="background:#fff;border-radius:16px;padding:24px;box-shadow:0 4px 24px rgba(99,28,255,.1);">'
    '<div style="font-size:13px;font-weight:600;color:#631cff;margin-bottom:16px;letter-spacing:.05em;">RESUMEN DE RESERVAS</div>'
    '<div style="display:flex;flex-direction:column;gap:10px;">'
    '<div style="background:#f8f7ff;border-radius:10px;padding:12px 16px;display:flex;justify-content:space-between;align-items:center;">'
    '<div><div style="font-size:14px;font-weight:600;color:#02021e;">Manicura con Ana</div><div style="font-size:12px;color:rgba(2,2,30,.5);">Lunes 12 mayo · 10:00</div></div>'
    '<div style="font-size:14px;font-weight:700;color:#631cff;">45€</div></div>'
    '<div style="background:#f8f7ff;border-radius:10px;padding:12px 16px;display:flex;justify-content:space-between;align-items:center;">'
    '<div><div style="font-size:14px;font-weight:600;color:#02021e;">Masaje con Laura</div><div style="font-size:12px;color:rgba(2,2,30,.5);">Miércoles 14 mayo · 11:30</div></div>'
    '<div style="font-size:14px;font-weight:700;color:#631cff;">60€</div></div>'
    '<div style="border-top:1px solid rgba(2,2,30,.08);margin-top:4px;padding-top:12px;display:flex;justify-content:space-between;align-items:center;">'
    '<div style="font-size:15px;font-weight:700;color:#02021e;">Total</div>'
    '<div style="font-size:20px;font-weight:800;color:#631cff;">105€</div></div>'
    '<div style="background:linear-gradient(90deg,#9B4FE8,#631cff);color:#fff;text-align:center;padding:12px;border-radius:10px;font-size:14px;font-weight:600;margin-top:4px;">Pagar todo de una vez</div>'
    '</div></div></div>'
)

CESTA_BODY = (
    '<p>Godolphy permite a tus clientes añadir varias reservas en una misma sesión y pagar todo de una vez. '
    'Por ejemplo: manicura con Ana el lunes y masaje con Laura el miércoles — una sola transacción, dos reservas independientes en tu agenda.</p>'
    '<p style="margin-top:16px;">Dentro de cada reserva, el cliente puede combinar varios servicios consecutivos con el mismo profesional. '
    'El sistema calcula automáticamente la duración total y bloquea el tiempo exacto en la agenda. Sin solapamientos, sin gestión manual.</p>'
    + bullet('Un solo pago para múltiples reservas')
    + bullet('Servicios combinados en una misma cita (ej: manicura + pedicura = 1h 45min bloqueados)')
    + bullet('El sistema valida automáticamente que el profesional puede realizar todos los servicios')
)

DIF1_RESERVAS = feat_section(
    'Reserva varios servicios a la vez, en un solo pago',
    CESTA_BODY,
    CESTA_VISUAL,
    alt=True
)

# Dif 1 — Cesta (condensed version for home page, inline styles)
DIF1_HOME = (
    '\n<!-- DIF: Cesta múltiple -->\n'
    '<section style="background:#f8f7ff;padding:80px 40px;">\n'
    '  <div style="max-width:1200px;margin:0 auto;display:flex;align-items:center;gap:80px;">\n'
    '    <div style="flex:1;">\n'
    '      <h2 class="font-gabarito" style="font-size:42px;line-height:1.1;font-weight:700;color:#02021e;margin:0 0 20px;">'
    'Reserva varios servicios a la vez, en un solo pago</h2>\n'
    '      <p style="color:rgba(2,2,30,.7);font-size:17px;line-height:1.65;margin:0 0 16px;">'
    'Tus clientes pueden añadir varias reservas — con distintos profesionales, en distintos días — y pagar todo de una vez. '
    'El sistema calcula la duración total y bloquea el tiempo exacto en la agenda. Sin solapamientos, sin gestión manual.</p>\n'
    '      <div style="display:flex;flex-direction:column;gap:12px;margin-top:24px;">\n'
    '        <div style="display:flex;align-items:flex-start;gap:12px;">'
    '<svg width="20" height="20" viewBox="0 0 20 20" fill="#631cff" style="flex-shrink:0;margin-top:2px;">'
    '<path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>'
    '<span style="color:rgba(2,2,30,.8);font-size:15px;">Un solo pago para múltiples reservas</span></div>\n'
    '        <div style="display:flex;align-items:flex-start;gap:12px;">'
    '<svg width="20" height="20" viewBox="0 0 20 20" fill="#631cff" style="flex-shrink:0;margin-top:2px;">'
    '<path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>'
    '<span style="color:rgba(2,2,30,.8);font-size:15px;">Servicios combinados en una cita (manicura + pedicura = 1h 45min bloqueados)</span></div>\n'
    '        <div style="display:flex;align-items:flex-start;gap:12px;">'
    '<svg width="20" height="20" viewBox="0 0 20 20" fill="#631cff" style="flex-shrink:0;margin-top:2px;">'
    '<path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>'
    '<span style="color:rgba(2,2,30,.8);font-size:15px;">El sistema valida que el profesional puede realizar todos los servicios seleccionados</span></div>\n'
    '      </div>\n'
    '    </div>\n'
    f'    <div style="flex:1;">{CESTA_VISUAL}</div>\n'
    '  </div>\n'
    '</section>\n'
)

# Dif 2 — Rutas avanzadas
RUTAS_VISUAL = (
    '<div style="background:linear-gradient(135deg,#f0ebff,#e0d5ff);border-radius:24px;padding:32px;">'
    '<div style="background:#fff;border-radius:16px;padding:24px;box-shadow:0 4px 24px rgba(99,28,255,.1);">'
    '<div style="font-size:13px;font-weight:600;color:#631cff;margin-bottom:16px;letter-spacing:.05em;">DISPONIBILIDAD REAL</div>'
    '<div style="display:flex;flex-direction:column;gap:0;">'
    '<div style="display:flex;align-items:center;gap:12px;padding:10px 0;">'
    '<div style="width:40px;height:40px;border-radius:10px;background:#f0ebff;display:flex;align-items:center;justify-content:center;flex-shrink:0;">'
    '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#631cff" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>'
    '</div>'
    '<div><div style="font-size:13px;font-weight:600;color:#02021e;">10:00 — Cliente A (60 min)</div>'
    '<div style="font-size:12px;color:rgba(2,2,30,.5);">Calle Mayor 12</div></div></div>'
    '<div style="margin-left:20px;width:2px;height:20px;background:linear-gradient(to bottom,#9B4FE8,#631cff);border-radius:2px;"></div>'
    '<div style="display:flex;align-items:center;gap:12px;padding:10px 0;">'
    '<div style="width:40px;height:40px;border-radius:10px;background:#fff3f3;display:flex;align-items:center;justify-content:center;flex-shrink:0;">'
    '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#e53e3e" stroke-width="2"><path d="M3 12h18M12 3l9 9-9 9"/></svg>'
    '</div>'
    '<div><div style="font-size:13px;font-weight:600;color:#02021e;">30 min desplazamiento</div>'
    '<div style="font-size:12px;color:rgba(2,2,30,.5);">Calculado con Google Maps</div></div></div>'
    '<div style="margin-left:20px;width:2px;height:20px;background:linear-gradient(to bottom,#631cff,#3a0aaa);border-radius:2px;"></div>'
    '<div style="display:flex;align-items:center;gap:12px;padding:10px 0;">'
    '<div style="width:40px;height:40px;border-radius:10px;background:#f0ebff;display:flex;align-items:center;justify-content:center;flex-shrink:0;">'
    '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#631cff" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>'
    '</div>'
    '<div><div style="font-size:13px;font-weight:600;color:#02021e;">11:30 — Cliente B (60 min)</div>'
    '<div style="font-size:12px;color:rgba(2,2,30,.5);">Primer hueco disponible real</div></div></div>'
    '<div style="background:#f0faf0;border-radius:8px;padding:10px 12px;margin-top:8px;font-size:12px;color:#2d7a3a;font-weight:600;">'
    '✓ 11:00 bloqueado — imposible llegar a tiempo</div>'
    '</div></div></div>'
)

RUTAS_BODY = (
    '<p>La mayoría de software de reservas calcula si un profesional está libre en un horario. '
    'Godolphy va más lejos: calcula si el profesional <em>puede llegar a tiempo</em>.</p>'
    '<p style="margin-top:16px;">Cuando un cliente quiere reservar un servicio a domicilio, el sistema tiene en cuenta:</p>'
    + bullet('La duración del servicio')
    + bullet('El tiempo de desplazamiento desde la cita anterior, calculado con Google Maps')
    + bullet('La ubicación real de ambos clientes')
    + '<p style="margin-top:16px;">Si hay 30 minutos de viaje entre cliente A y cliente B, y el servicio dura 1 hora, '
    'el sistema no ofrecerá el hueco de las 11:00 si eso hace imposible llegar a la cita de las 12:00. '
    'Solo aparecen los horarios que realmente funcionan.</p>'
    + highlight_box('Para la primera cita del día, el cálculo parte desde el punto base del profesional: local, oficina o dirección del freelance.')
    + '<p><strong>Resultado:</strong> cero citas imposibles en la agenda y cero sorpresas para el profesional.</p>'
)

DIF2_RUTAS = feat_section(
    'Disponibilidad real, no teórica',
    RUTAS_BODY,
    RUTAS_VISUAL,
    alt=True
)

# Dif 3 — Cobro automático tras el servicio
COBRO_VISUAL = (
    '<div style="background:linear-gradient(135deg,#f0ebff,#e0d5ff);border-radius:24px;padding:32px;">'
    '<div style="background:#fff;border-radius:16px;padding:24px;box-shadow:0 4px 24px rgba(99,28,255,.1);">'
    '<div style="font-size:13px;font-weight:600;color:#631cff;margin-bottom:16px;letter-spacing:.05em;">CICLO DE COBRO AUTOMÁTICO</div>'
    '<div style="display:flex;flex-direction:column;gap:0;">'
    '<div style="display:flex;gap:12px;padding:10px 0;">'
    '<div style="display:flex;flex-direction:column;align-items:center;">'
    '<div style="width:28px;height:28px;border-radius:50%;background:linear-gradient(90deg,#9B4FE8,#631cff);display:flex;align-items:center;justify-content:center;">'
    '<svg width="12" height="12" viewBox="0 0 24 24" fill="white"><path d="M5 13l4 4L19 7"/></svg></div>'
    '<div style="width:2px;flex:1;background:rgba(99,28,255,.15);margin:4px 0;"></div></div>'
    '<div><div style="font-size:13px;font-weight:600;color:#02021e;">Al reservar</div>'
    '<div style="font-size:12px;color:rgba(2,2,30,.5);">El cliente paga el depósito (30%)</div></div></div>'
    '<div style="display:flex;gap:12px;padding:10px 0;">'
    '<div style="display:flex;flex-direction:column;align-items:center;">'
    '<div style="width:28px;height:28px;border-radius:50%;background:linear-gradient(90deg,#9B4FE8,#631cff);display:flex;align-items:center;justify-content:center;">'
    '<svg width="12" height="12" viewBox="0 0 24 24" fill="white"><path d="M5 13l4 4L19 7"/></svg></div>'
    '<div style="width:2px;flex:1;background:rgba(99,28,255,.15);margin:4px 0;"></div></div>'
    '<div><div style="font-size:13px;font-weight:600;color:#02021e;">Servicio completado</div>'
    '<div style="font-size:12px;color:rgba(2,2,30,.5);">El profesional lo marca como completado</div></div></div>'
    '<div style="display:flex;gap:12px;padding:10px 0;">'
    '<div style="width:28px;height:28px;border-radius:50%;background:#EEFE3A;display:flex;align-items:center;justify-content:center;flex-shrink:0;">'
    '<svg width="12" height="12" viewBox="0 0 24 24" fill="#02021e"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>'
    '</div>'
    '<div><div style="font-size:13px;font-weight:600;color:#02021e;">Cobro automático del resto (70%)</div>'
    '<div style="font-size:12px;color:rgba(2,2,30,.5);">Sin pasos manuales</div></div></div>'
    '</div></div></div>'
)

COBRO_BODY = (
    '<p>Cuando un cliente paga solo el depósito al reservar, Godolphy puede cobrar automáticamente el importe restante '
    'sin que tengas que hacer nada.</p>'
    '<p style="margin-top:16px;font-weight:600;color:#02021e;">Tú decides cuándo se cobra:</p>'
    + bullet('15 minutos después de empezar la cita')
    + bullet('Al finalizar el servicio')
    + bullet('Cuando el profesional marca el servicio como completado')
    + '<p style="margin-top:16px;">El cobro se hace sobre la tarjeta que el cliente usó al reservar. '
    'Sin pasos manuales, sin olvidar cobrar, sin situaciones incómodas al finalizar.</p>'
)

DIF3_COBRO = feat_section(
    'El resto del pago, cobrado solo',
    COBRO_BODY,
    COBRO_VISUAL,
    alt=False
)

# Dif 3 — Política de cancelación
POLITICA_VISUAL = (
    '<div style="background:linear-gradient(135deg,#f0ebff,#e0d5ff);border-radius:24px;padding:32px;">'
    '<div style="background:#fff;border-radius:16px;padding:24px;box-shadow:0 4px 24px rgba(99,28,255,.1);">'
    '<div style="font-size:13px;font-weight:600;color:#631cff;margin-bottom:16px;letter-spacing:.05em;">POLÍTICA DE CANCELACIÓN</div>'
    '<div style="display:flex;flex-direction:column;gap:0;">'
    '<div style="background:#f0faf0;border-radius:8px;padding:12px 14px;margin-bottom:8px;">'
    '<div style="font-size:12px;font-weight:600;color:#2d7a3a;">Con + de 24h de antelación</div>'
    '<div style="font-size:13px;color:rgba(2,2,30,.7);margin-top:4px;">→ Devolver el depósito automáticamente</div></div>'
    '<div style="background:#fff3f3;border-radius:8px;padding:12px 14px;margin-bottom:8px;">'
    '<div style="font-size:12px;font-weight:600;color:#c53030;">Cancelación tardía</div>'
    '<div style="font-size:13px;color:rgba(2,2,30,.7);margin-top:4px;">→ Retener el depósito o cobrar el total</div></div>'
    '<div style="background:#fff3f3;border-radius:8px;padding:12px 14px;">'
    '<div style="font-size:12px;font-weight:600;color:#c53030;">No-show</div>'
    '<div style="font-size:13px;color:rgba(2,2,30,.7);margin-top:4px;">→ Retener el depósito o cobrar el total</div></div>'
    '<div style="border-top:1px solid rgba(2,2,30,.08);margin-top:12px;padding-top:12px;font-size:12px;color:rgba(2,2,30,.5);">'
    'Tú defines las reglas. Godolphy las aplica automáticamente.</div>'
    '</div></div></div>'
)

POLITICA_BODY = (
    '<p>Godolphy te permite configurar exactamente qué pasa cuando un cliente cancela o no aparece. '
    'Sin discusiones y sin gestión manual.</p>'
    + policy_row('Cancela dentro del plazo permitido', 'devolver el depósito automáticamente', '#2d7a3a')
    + policy_row('Cancela fuera del plazo', 'retener el depósito o cobrar el servicio completo', '#e53e3e')
    + policy_row('No-show (no aparece)', 'retener el depósito o cobrar el servicio completo', '#e53e3e')
    + '<p style="margin-top:20px;">Tú defines el plazo de cancelación sin penalización '
    '(por ejemplo, más de 24 horas antes). El sistema aplica la política automáticamente.'
    '</p>'
)

DIF3_POLITICA = feat_section(
    'Tú defines las reglas, el sistema las aplica',
    POLITICA_BODY,
    POLITICA_VISUAL,
    alt=True
)

# Dif 4 — Freelance y empleados
ROLES_VISUAL = (
    '<div style="background:linear-gradient(135deg,#f0ebff,#e0d5ff);border-radius:24px;padding:32px;">'
    '<div style="display:flex;flex-direction:column;gap:12px;">'
    '<div style="background:#fff;border-radius:16px;padding:20px;box-shadow:0 4px 24px rgba(99,28,255,.08);">'
    '<div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;">'
    '<div style="width:36px;height:36px;border-radius:10px;background:linear-gradient(90deg,#9B4FE8,#631cff);display:flex;align-items:center;justify-content:center;">'
    '<svg width="18" height="18" viewBox="0 0 24 24" fill="white"><path d="M12 2a5 5 0 110 10A5 5 0 0112 2zm0 12c-5.33 0-8 2.67-8 4v2h16v-2c0-1.33-2.67-4-8-4z"/></svg></div>'
    '<div><div style="font-size:13px;font-weight:700;color:#02021e;">Empleado</div>'
    '<div style="font-size:11px;color:rgba(2,2,30,.5);">Acceso estándar</div></div></div>'
    '<div style="display:flex;flex-direction:column;gap:6px;">'
    '<div style="display:flex;align-items:center;gap:8px;font-size:12px;color:rgba(2,2,30,.7);">'
    '<svg width="12" height="12" viewBox="0 0 20 20" fill="#631cff"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>'
    'Ve su agenda y sus clientes</div>'
    '<div style="display:flex;align-items:center;gap:8px;font-size:12px;color:rgba(2,2,30,.4);">'
    '<svg width="12" height="12" viewBox="0 0 20 20" fill="#ccc"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>'
    'No ve datos financieros ni emails</div>'
    '</div></div>'
    '<div style="background:#fff;border-radius:16px;padding:20px;box-shadow:0 4px 24px rgba(99,28,255,.08);">'
    '<div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;">'
    '<div style="width:36px;height:36px;border-radius:10px;background:#EEFE3A;display:flex;align-items:center;justify-content:center;">'
    '<svg width="18" height="18" viewBox="0 0 24 24" fill="#02021e"><path d="M20 6h-2.18c.07-.44.18-.88.18-1.36C18 2.06 15.86 0 13.5 0c-1.23 0-2.3.54-3 1.39C9.8.54 8.73 0 7.5 0 5.14 0 3 2.06 3 4.64c0 .48.11.92.18 1.36H1c-1.1 0-2 .9-2 2v13c0 1.1.9 2 2 2h19c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2z"/></svg></div>'
    '<div><div style="font-size:13px;font-weight:700;color:#02021e;">Freelance</div>'
    '<div style="font-size:11px;color:rgba(2,2,30,.5);">Acceso propio + aceptar/rechazar</div></div></div>'
    '<div style="display:flex;flex-direction:column;gap:6px;">'
    '<div style="display:flex;align-items:center;gap:8px;font-size:12px;color:rgba(2,2,30,.7);">'
    '<svg width="12" height="12" viewBox="0 0 20 20" fill="#631cff"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>'
    'Puede aceptar o rechazar servicios</div>'
    '<div style="display:flex;align-items:center;gap:8px;font-size:12px;color:rgba(2,2,30,.7);">'
    '<svg width="12" height="12" viewBox="0 0 20 20" fill="#631cff"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>'
    'Ve solo su agenda y sus asignados</div>'
    '</div></div>'
    '</div>'
)

FREELANCE_BODY = (
    '<p>Godolphy distingue entre dos tipos de profesionales: empleados internos y colaboradores freelance. '
    'Cada uno con permisos y funcionamiento diferente.</p>'
    '<p style="margin-top:16px;"><strong>Empleados</strong> tienen acceso a su agenda y sus clientes. '
    'No ven datos financieros ni la configuración global del negocio. No ven el email de los clientes.</p>'
    '<p style="margin-top:16px;"><strong>Colaboradores freelance</strong> pueden aceptar o rechazar servicios según la política que tú definas. '
    'Ideal para centros que trabajan con profesionales externos o por proyectos.</p>'
    '<p style="margin-top:16px;">En ambos casos, cada profesional solo ve lo que le corresponde. '
    'Tú, como administrador, tienes visión completa de todo el negocio.</p>'
    + bullet('Permisos diferenciados por rol')
    + bullet('Freelance pueden aceptar o rechazar servicios')
    + bullet('El administrador ve todo; el profesional, solo lo suyo')
)

DIF4_FREELANCE = feat_section(
    'Empleados y freelance, en el mismo sistema',
    FREELANCE_BODY,
    ROLES_VISUAL,
    alt=True
)

# Dif 5 — Sin IVA (funcionalidades pages — none; precio + home)
DIF5_PRECIO = (
    '\n<!-- DIF: Sin IVA -->\n'
    '<section style="background:#fff;padding:60px 40px;">\n'
    '  <div style="max-width:900px;margin:0 auto;background:linear-gradient(135deg,#02021e 0%,#1a0a4a 100%);border-radius:24px;padding:48px 56px;display:flex;align-items:center;gap:48px;">\n'
    '    <div style="flex-shrink:0;width:64px;height:64px;border-radius:16px;background:rgba(255,255,255,.1);display:flex;align-items:center;justify-content:center;">\n'
    '      <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#EEFE3A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>\n'
    '    </div>\n'
    '    <div style="flex:1;">\n'
    '      <h2 class="font-gabarito" style="color:#fff;font-size:28px;font-weight:700;margin:0 0 12px;line-height:1.2;">Sin IVA europeo — el precio que ves es el que pagas</h2>\n'
    '      <p style="color:rgba(255,255,255,.7);font-size:16px;line-height:1.7;margin:0 0 20px;">Godolphy opera como empresa registrada en Estados Unidos. Las suscripciones no llevan IVA europeo. '
    'Eso supone un <strong style="color:#EEFE3A;">21% de ahorro</strong> respecto a alternativas españolas equivalentes.</p>\n'
    '      <div style="display:inline-block;background:rgba(238,254,58,.15);border:1px solid rgba(238,254,58,.3);border-radius:10px;padding:8px 16px;font-size:14px;font-weight:600;color:#EEFE3A;">'
    'Sin IVA · Sin sorpresas · Sin costes ocultos</div>\n'
    '    </div>\n'
    '  </div>\n'
    '</section>\n'
)

DIF5_HOME = (
    '\n<!-- DIF: Sin IVA (home) -->\n'
    '<section style="background:#fff;padding:20px 40px 60px;">\n'
    '  <div style="max-width:1300px;margin:0 auto;">\n'
    '    <div style="background:linear-gradient(135deg,#02021e 0%,#1a0a4a 100%);border-radius:24px;padding:40px 56px;display:flex;align-items:center;gap:40px;">\n'
    '      <div style="flex-shrink:0;width:56px;height:56px;border-radius:14px;background:rgba(255,255,255,.1);display:flex;align-items:center;justify-content:center;">\n'
    '        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#EEFE3A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>\n'
    '      </div>\n'
    '      <div style="flex:1;">\n'
    '        <p style="color:#EEFE3A;font-size:12px;font-weight:600;letter-spacing:.08em;margin:0 0 6px;">EMPRESA USA · SIN IVA EUROPEO</p>\n'
    '        <h3 class="font-gabarito" style="color:#fff;font-size:24px;font-weight:700;margin:0 0 8px;">El precio que ves es el que pagas — 21% más económico que alternativas españolas</h3>\n'
    '        <p style="color:rgba(255,255,255,.65);font-size:15px;margin:0;">Godolphy opera como empresa registrada en EE.UU. Las suscripciones no llevan IVA europeo. Planes desde 33€/mes todo incluido.</p>\n'
    '      </div>\n'
    '      <a href="/precio/" style="flex-shrink:0;background:#EEFE3A;color:#02021e;font-size:15px;font-weight:700;padding:12px 28px;border-radius:14px;text-decoration:none;white-space:nowrap;">Ver precios</a>\n'
    '    </div>\n'
    '  </div>\n'
    '</section>\n'
)

# Dif 6 — Personalización página reservas
BRAND_VISUAL = (
    '<div style="background:linear-gradient(135deg,#f0ebff,#e0d5ff);border-radius:24px;padding:32px;">'
    '<div style="background:#fff;border-radius:16px;overflow:hidden;box-shadow:0 4px 24px rgba(99,28,255,.1);">'
    '<div style="background:linear-gradient(90deg,#9B4FE8,#631cff);padding:16px 20px;display:flex;align-items:center;gap:10px;">'
    '<div style="width:32px;height:32px;border-radius:8px;background:rgba(255,255,255,.2);display:flex;align-items:center;justify-content:center;">'
    '<svg width="16" height="16" viewBox="0 0 24 24" fill="white"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg></div>'
    '<div><div style="font-size:12px;font-weight:600;color:#fff;">Tu Negocio</div>'
    '<div style="font-size:10px;color:rgba(255,255,255,.7);">reservas.tunegocio.com</div></div></div>'
    '<div style="padding:20px;">'
    '<div style="font-size:13px;font-weight:600;color:#02021e;margin-bottom:12px;">Selecciona un servicio</div>'
    '<div style="display:flex;flex-direction:column;gap:8px;">'
    '<div style="border:1.5px solid #631cff;border-radius:10px;padding:10px 14px;font-size:13px;color:#631cff;font-weight:600;">Manicura básica · 45 min · 30€</div>'
    '<div style="border:1.5px solid rgba(2,2,30,.1);border-radius:10px;padding:10px 14px;font-size:13px;color:#02021e;">Pedicura · 60 min · 45€</div>'
    '<div style="border:1.5px solid rgba(2,2,30,.1);border-radius:10px;padding:10px 14px;font-size:13px;color:#02021e;">Nail art · 90 min · 65€</div>'
    '</div>'
    '<div style="background:linear-gradient(90deg,#9B4FE8,#631cff);color:#fff;text-align:center;padding:12px;border-radius:10px;font-size:13px;font-weight:600;margin-top:16px;">Continuar →</div>'
    '</div></div></div>'
)

BRAND_BODY = (
    '<p>La página de reservas de Godolphy se puede personalizar con el logo y el color de tu marca. '
    'Tus clientes ven una experiencia coherente con tu negocio, no una página genérica de terceros.</p>'
    + bullet('Logo y colores de tu marca en toda la experiencia de reserva')
    + bullet('Dominio propio (reservas.tunegocio.com) disponible en el plan Max')
    + bullet('Página pública, accesible desde cualquier dispositivo las 24 horas')
    + '<p style="margin-top:16px;">Puedes compartir el enlace en Instagram, WhatsApp, Google My Business o donde quieras. '
    'Sin redirigir a tus clientes a una plataforma externa con la marca de otra empresa.</p>'
)

DIF6_BRAND = feat_section(
    'Tu página de reservas, con tu imagen',
    BRAND_BODY,
    BRAND_VISUAL,
    alt=False
)

# ─────────────────────────────────────────────────────────────────────────────
# INSERTION ANCHORS
# ─────────────────────────────────────────────────────────────────────────────

# For funcionalidades pages — before the "Empieza gratis hoy mismo" CTA box
FUNC_CTA_ANCHOR = '<section style="background:#f8f7ff;padding:80px 40px;"><div style="max-width:900px;margin:0 auto;background:linear-gradient(160deg,#9B4FE8'

# For home — before CTA FINAL comment
HOME_CTA_ANCHOR = '<!-- ═══════════════════════════════════════ CTA FINAL ═══════════════════════════════════════ -->'

# For precio — before CTA section
PRECIO_CTA_ANCHOR = '<!-- CTA -->'

# ─────────────────────────────────────────────────────────────────────────────
# APPLY CHANGES
# ─────────────────────────────────────────────────────────────────────────────

def apply(filepath, insertions):
    """insertions = list of (anchor, content_to_prepend)"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    for anchor, new_content in insertions:
        if anchor in content:
            content = content.replace(anchor, new_content + anchor, 1)
        else:
            print(f'  WARNING: anchor not found in {filepath}')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'OK  {os.path.relpath(filepath, BASE)}')

# reservas-online: Dif1 + Dif6
apply(
    f'{BASE}/funcionalidades/reservas-online/index.html',
    [(FUNC_CTA_ANCHOR, DIF1_RESERVAS + DIF6_BRAND)]
)

# servicios-a-domicilio: Dif2
apply(
    f'{BASE}/funcionalidades/servicios-a-domicilio/index.html',
    [(FUNC_CTA_ANCHOR, DIF2_RUTAS)]
)

# pagos-y-depositos: Dif3 (cobro automático + política)
apply(
    f'{BASE}/funcionalidades/pagos-y-depositos/index.html',
    [(FUNC_CTA_ANCHOR, DIF3_COBRO + DIF3_POLITICA)]
)

# equipo-y-horarios: Dif4
apply(
    f'{BASE}/funcionalidades/equipo-y-horarios/index.html',
    [(FUNC_CTA_ANCHOR, DIF4_FREELANCE)]
)

# home: Dif1 (condensed) + Dif5
apply(
    f'{BASE}/index.html',
    [(HOME_CTA_ANCHOR, DIF5_HOME + DIF1_HOME)]
)

# precio: Dif5
apply(
    f'{BASE}/precio/index.html',
    [(PRECIO_CTA_ANCHOR, DIF5_PRECIO)]
)

print('\nDone.')
