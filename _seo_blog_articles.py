#!/usr/bin/env python3
"""
SEO optimization for Godolphy blog articles:
  1. Add Article schema JSON-LD to <head>
  2. Add 2-3 internal links naturally in post-content
"""
import os, re, json

BASE = '/Users/neusfigueres/godolphy-static'
GUARD = '<!-- SEO:schema-article -->'

MONTHS = {
    'enero':'01','febrero':'02','marzo':'03','abril':'04',
    'mayo':'05','junio':'06','julio':'07','agosto':'08',
    'septiembre':'09','octubre':'10','noviembre':'11','diciembre':'12'
}

BLOG_SLUGS = [
    'abrir-centro-de-estetica-en-espana',
    'aspectos-clave-para-optimizar-tu-centro-de-estetica',
    'casos-de-exito-de-campanas-de-marketing-de-salones-es-estetica',
    'como-atraer-clientas-para-unas',
    'como-calcular-los-precios-de-barberia',
    'como-calcular-los-precios-de-mis-masajes',
    'como-calcular-los-precios-de-mis-servicios-de-belleza',
    'como-calcular-los-precios-de-mis-servicios-de-manicura',
    'como-conseguir-mas-clientes-salon-de-belleza',
    'como-contratar-una-manicurista-consejos-requisitos-y-mas',
    'como-crear-una-experiencia-memorable-en-tu-salon-de-unas-peluqueria-o-barberia',
    'como-crear-una-factura-para-un-servicio-estetico',
    'como-dar-de-alta-mi-salon-en-espana-legalmente',
    'como-empezar-un-negocio-de-peluqueria-a-domicilio',
    'como-escoger-el-local-para-mi-centro-de-estetica-salon-de-unas-peluqueria-o-barberia',
    'como-escoger-el-mejor-software-para-mi-salon-de-unas',
    'como-evitar-clientes-indeseados-en-un-spa',
    'como-evitar-las-citas-canceladas-de-mi-salon',
    'como-un-masajista-puede-evitar-clientes-indeseados-sin-renunciar-a-la-organizacion-digital',
    'como-utilizar-whatsapp-para-recordar-citas-promociones',
    'consejos-evitar-cancelaciones-turnos-clientes',
    'consejos-para-seleccionar-tecnicos-de-unas-peluqueros-barberos-centro-de-estetica',
    'cual-es-el-iva-para-un-servicio-de-estetica',
    'cuanto-gana-un-salon-de-unas-en-espana',
    'cuanto-gana-una-manicurista-en-espana',
    'diferencias-entre-fresha-y-godolphy',
    'errores-legales-en-centro-de-masajes',
    'estrategias-atraer-y-retener-clientes',
    'franquicias-de-estetica-rentables',
    'inbound-marketing-para-salones-de-estetica',
    'inspeccion-a-un-centro-de-masajes',
    'lampistas-fontaneros-reparaciones-software',
    'licencias-para-un-centro-de-masajes',
    'marketing-local-para-salones-de-estetica',
    'plan-financiero-salon-estetica-excel-google-sheet',
    'plantilla-facturacion-centros-de-estetica-excel',
    'precios-de-servicios-de-peluqueria',
    'que-debo-tener-en-cuenta-antes-de-abrir-mi-salon-de-unas-o-centro-de-estetica',
    'que-se-necesita-para-abrir-un-salon-de-estetica',
    'que-se-necesita-para-abrir-un-salon-de-unas',
    'requisitos-de-sanidad-para-un-salon-de-belleza',
    'requisitos-para-abrir-un-centro-de-masajes-en-espana',
    'servicio-de-manicura-en-espana',
    'tecnicas-para-fidelizar-los-clientes-de-tu-centro-de-estetica',
    'tus-excusas-para-no-realizar-servicios-a-domicilio',
]

# Each entry: [(target_url, [candidate_phrases_in_priority_order]), ...]
# The first phrase found in post-content (not already in a link) gets linked.
LINK_MAP = {
    'consejos-evitar-cancelaciones-turnos-clientes': [
        ('/funcionalidades/chat-y-notificaciones/',  ['recordatorios personalizados', 'recordatorios automatizados', 'recordatorios', 'recordatorio']),
        ('/funcionalidades/pagos-y-depositos/',      ['pago anticipado', 'pagos anticipados', 'pago por adelantado', 'cobro anticipado']),
    ],
    'como-evitar-las-citas-canceladas-de-mi-salon': [
        ('/funcionalidades/pagos-y-depositos/',      ['pago anticipado', 'pagos anticipados', 'señal al reservar', 'cobrar una señal', 'depósito al reservar']),
        ('/funcionalidades/chat-y-notificaciones/',  ['recordatorio', 'recordatorios', 'WhatsApp', 'notificaciones']),
    ],
    'tecnicas-para-fidelizar-los-clientes-de-tu-centro-de-estetica': [
        ('/funcionalidades/fidelizacion-ai/',         ['fidelización automática', 'fidelización con IA', 'fidelización', 'fidelizar']),
        ('/funcionalidades/cupones-y-tarjetas-regalo/', ['cupones de descuento', 'tarjetas regalo', 'cupones', 'descuentos']),
        ('/funcionalidades/gestion-de-clientes/',     ['ficha de cliente', 'historial de visitas', 'historial del cliente', 'historial']),
    ],
    'como-atraer-clientas-para-unas': [
        ('/funcionalidades/fidelizacion-ai/',         ['fidelización', 'fidelizar', 'retener clientes', 'lealtad']),
        ('/funcionalidades/cupones-y-tarjetas-regalo/', ['cupones', 'descuentos', 'tarjetas regalo', 'promociones']),
        ('/funcionalidades/gestion-de-clientes/',     ['ficha de cliente', 'historial', 'clientes habituales', 'datos de los clientes']),
    ],
    'estrategias-atraer-y-retener-clientes': [
        ('/funcionalidades/fidelizacion-ai/',         ['fidelización', 'retener clientes', 'fidelizar', 'lealtad']),
        ('/funcionalidades/cupones-y-tarjetas-regalo/', ['cupones de descuento', 'tarjetas regalo', 'cupones', 'descuentos']),
        ('/funcionalidades/gestion-de-clientes/',     ['ficha de cliente', 'historial de visitas', 'historial', 'datos de los clientes']),
    ],
    'casos-de-exito-de-campanas-de-marketing-de-salones-es-estetica': [
        ('/funcionalidades/fidelizacion-ai/',         ['fidelización', 'fidelizar', 'retener clientes', 'lealtad']),
        ('/funcionalidades/cupones-y-tarjetas-regalo/', ['cupones', 'descuentos', 'tarjeta regalo', 'promociones']),
        ('/funcionalidades/gestion-de-clientes/',     ['base de datos de clientes', 'ficha de cliente', 'historial de clientes', 'historial']),
    ],
    'marketing-local-para-salones-de-estetica': [
        ('/funcionalidades/reservas-online/',         ['reservas online', 'reserva online', 'citas online', 'reservas en línea']),
        ('/funcionalidades/chat-y-notificaciones/',   ['WhatsApp', 'notificaciones automáticas', 'recordatorios', 'notificaciones']),
    ],
    'inbound-marketing-para-salones-de-estetica': [
        ('/funcionalidades/reservas-online/',         ['reservas online', 'citas online', 'reservas en línea', 'booking']),
        ('/funcionalidades/chat-y-notificaciones/',   ['WhatsApp', 'notificaciones', 'mensajes automáticos', 'recordatorios']),
    ],
    'como-conseguir-mas-clientes-salon-de-belleza': [
        ('/funcionalidades/reservas-online/',         ['reservas online', 'reserva online', 'citas online', 'reservas en línea']),
        ('/funcionalidades/chat-y-notificaciones/',   ['WhatsApp', 'notificaciones automáticas', 'recordatorios']),
    ],
    'como-utilizar-whatsapp-para-recordar-citas-promociones': [
        ('/funcionalidades/reservas-online/',         ['reservas online', 'citas online', 'reservas en línea']),
        ('/funcionalidades/chat-y-notificaciones/',   ['recordatorio', 'recordatorios', 'WhatsApp', 'notificaciones']),
    ],
    'como-calcular-los-precios-de-mis-masajes': [
        ('/funcionalidades/facturacion-y-reporte/',   ['tus ingresos', 'los ingresos', 'ingresos', 'facturación', 'rentabilidad']),
        ('/sectores/software-para-spa-y-masajes/',    ['masajista', 'centro de masajes', 'spa', 'masajes']),
        ('/funcionalidades/pagos-y-depositos/',       ['depósito', 'pago anticipado', 'cobro']),
    ],
    'como-calcular-los-precios-de-barberia': [
        ('/funcionalidades/facturacion-y-reporte/',   ['tus ingresos', 'los ingresos', 'ingresos', 'facturación', 'rentabilidad']),
        ('/sectores/software-para-barberias/',        ['barbería', 'barberías', 'barbero', 'barberos']),
    ],
    'como-calcular-los-precios-de-mis-servicios-de-manicura': [
        ('/funcionalidades/facturacion-y-reporte/',   ['tus ingresos', 'los ingresos', 'ingresos', 'facturación', 'rentabilidad']),
        ('/precio/',                                   ['software de gestión', 'plataforma de gestión', 'herramienta de gestión', 'software']),
    ],
    'precios-de-servicios-de-peluqueria': [
        ('/funcionalidades/facturacion-y-reporte/',   ['tus ingresos', 'los ingresos', 'ingresos', 'facturación', 'rentabilidad']),
        ('/precio/',                                   ['software de gestión', 'herramienta de gestión', 'plataforma de gestión']),
    ],
    'como-calcular-los-precios-de-mis-servicios-de-belleza': [
        ('/funcionalidades/facturacion-y-reporte/',   ['tus ingresos', 'los ingresos', 'ingresos', 'facturación', 'rentabilidad']),
        ('/precio/',                                   ['software de gestión', 'plataforma de gestión', 'herramienta de gestión']),
    ],
    'plan-financiero-salon-estetica-excel-google-sheet': [
        ('/funcionalidades/facturacion-y-reporte/',   ['tus ingresos', 'los ingresos', 'ingresos', 'facturación', 'rentabilidad']),
        ('/integraciones/holded/',                    ['Holded', 'contabilidad', 'facturación automática']),
    ],
    'abrir-centro-de-estetica-en-espana': [
        ('/funcionalidades/reservas-online/',         ['reservas online', 'sistema de reservas', 'citas online', 'reservas en línea']),
        ('/sectores/software-para-centro-de-estetica-y-salones/', ['software para centros de estética', 'software de gestión', 'gestión del centro']),
        ('/lista-de-espera/',                         ['prueba gratuita', 'probar gratis', 'Godolphy gratis']),
    ],
    'que-se-necesita-para-abrir-un-salon-de-estetica': [
        ('/funcionalidades/reservas-online/',         ['reservas online', 'sistema de reservas', 'citas online', 'reservas en línea']),
        ('/sectores/software-para-centro-de-estetica-y-salones/', ['software para centros de estética', 'software de gestión', 'software para salón']),
        ('/lista-de-espera/',                         ['probar gratis', 'prueba gratuita', 'Godolphy gratis']),
    ],
    'que-se-necesita-para-abrir-un-salon-de-unas': [
        ('/funcionalidades/reservas-online/',         ['reservas online', 'sistema de reservas', 'citas online']),
        ('/sectores/software-para-centro-de-estetica-y-salones/', ['software para centros de estética', 'software de gestión', 'gestión del negocio']),
        ('/lista-de-espera/',                         ['probar gratis', 'prueba gratuita', 'Godolphy gratis']),
    ],
    'como-dar-de-alta-mi-salon-en-espana-legalmente': [
        ('/funcionalidades/reservas-online/',         ['reservas online', 'sistema de reservas', 'citas online']),
        ('/sectores/software-para-centro-de-estetica-y-salones/', ['software para centros de estética', 'software de gestión', 'gestión del salón']),
        ('/lista-de-espera/',                         ['probar gratis', 'Godolphy gratis', 'prueba gratuita']),
    ],
    'que-debo-tener-en-cuenta-antes-de-abrir-mi-salon-de-unas-o-centro-de-estetica': [
        ('/funcionalidades/reservas-online/',         ['reservas online', 'sistema de reservas', 'citas online']),
        ('/sectores/software-para-centro-de-estetica-y-salones/', ['software para centros de estética', 'software de gestión']),
        ('/lista-de-espera/',                         ['probar gratis', 'Godolphy gratis', 'prueba gratuita']),
    ],
    'como-empezar-un-negocio-de-peluqueria-a-domicilio': [
        ('/funcionalidades/reservas-online/',         ['reservas online', 'citas online', 'sistema de reservas', 'reservas en línea']),
        ('/sectores/software-para-centro-de-estetica-y-salones/', ['software de gestión', 'software para salón', 'gestión del negocio']),
        ('/lista-de-espera/',                         ['probar gratis', 'Godolphy gratis', 'prueba gratuita']),
    ],
    'consejos-para-seleccionar-tecnicos-de-unas-peluqueros-barberos-centro-de-estetica': [
        ('/funcionalidades/equipo-y-horarios/',       ['gestión del equipo', 'equipo de profesionales', 'horarios del personal', 'gestión del personal', 'equipo']),
        ('/funcionalidades/facturacion-y-reporte/',   ['comisiones', 'rendimiento de cada profesional', 'ingresos', 'productividad']),
    ],
    'como-contratar-una-manicurista-consejos-requisitos-y-mas': [
        ('/funcionalidades/equipo-y-horarios/',       ['gestión del equipo', 'equipo de profesionales', 'horarios', 'gestión del personal', 'equipo']),
        ('/funcionalidades/facturacion-y-reporte/',   ['comisiones', 'rendimiento', 'ingresos', 'productividad']),
    ],
    'tus-excusas-para-no-realizar-servicios-a-domicilio': [
        ('/funcionalidades/servicios-a-domicilio/',   ['servicios a domicilio', 'servicio a domicilio', 'trabajo a domicilio', 'domicilio']),
        ('/funcionalidades/reservas-online/',         ['reservas online', 'citas online', 'sistema de reservas']),
    ],
    'servicio-de-manicura-en-espana': [
        ('/funcionalidades/servicios-a-domicilio/',   ['servicios a domicilio', 'servicio a domicilio', 'domicilio']),
        ('/funcionalidades/reservas-online/',         ['reservas online', 'reservas en línea', 'citas online']),
    ],
    'como-evitar-clientes-indeseados-en-un-spa': [
        ('/sectores/software-para-spa-y-masajes/',    ['spa', 'masajes', 'centro de masajes', 'masajista']),
        ('/funcionalidades/pagos-y-depositos/',       ['depósito', 'pago anticipado', 'señal al reservar', 'cobro anticipado']),
    ],
    'como-un-masajista-puede-evitar-clientes-indeseados-sin-renunciar-a-la-organizacion-digital': [
        ('/sectores/software-para-spa-y-masajes/',    ['masajista', 'masajistas', 'spa', 'masajes']),
        ('/funcionalidades/pagos-y-depositos/',       ['depósito', 'pago anticipado', 'señal al reservar', 'cobro anticipado']),
    ],
    'requisitos-para-abrir-un-centro-de-masajes-en-espana': [
        ('/sectores/software-para-spa-y-masajes/',    ['centro de masajes', 'masajes', 'masajista', 'spa']),
        ('/funcionalidades/reservas-online/',         ['reservas online', 'citas online', 'sistema de reservas', 'reservas']),
    ],
    'errores-legales-en-centro-de-masajes': [
        ('/sectores/software-para-spa-y-masajes/',    ['centro de masajes', 'masajes', 'masajista', 'spa']),
        ('/funcionalidades/pagos-y-depositos/',       ['cobros', 'pagos', 'depósitos', 'reservas']),
    ],
    'licencias-para-un-centro-de-masajes': [
        ('/sectores/software-para-spa-y-masajes/',    ['centro de masajes', 'masajes', 'spa', 'masajista']),
        ('/funcionalidades/reservas-online/',         ['reservas online', 'citas online', 'sistema de reservas']),
    ],
    'inspeccion-a-un-centro-de-masajes': [
        ('/sectores/software-para-spa-y-masajes/',    ['centro de masajes', 'masajes', 'spa', 'masajista']),
        ('/funcionalidades/reservas-online/',         ['reservas online', 'citas online', 'sistema de reservas']),
    ],
    'diferencias-entre-fresha-y-godolphy': [
        ('/precio/',                                   ['precios de Godolphy', 'precios', 'tarifas', 'coste']),
        ('/funcionalidades/reservas-online/',         ['reservas online', 'reservas sin comisiones', 'comisiones', 'sin comisiones']),
        ('/lista-de-espera/',                         ['prueba gratis', 'probar gratis', '30 días gratis', 'gratuita']),
    ],
    'franquicias-de-estetica-rentables': [
        ('/funcionalidades/multiples-ubicaciones/',   ['múltiples ubicaciones', 'varias ubicaciones', 'múltiples centros', 'varios centros', 'franquicias']),
        ('/sectores/software-para-centro-de-estetica-y-salones/', ['software para centros de estética', 'software de gestión', 'gestión del centro']),
    ],
    'cual-es-el-iva-para-un-servicio-de-estetica': [
        ('/funcionalidades/facturacion-y-reporte/',   ['facturación', 'facturas', 'factura electrónica', 'tus ingresos']),
        ('/integraciones/holded/',                    ['Holded', 'software de contabilidad', 'contabilidad']),
    ],
    'como-crear-una-factura-para-un-servicio-estetico': [
        ('/funcionalidades/facturacion-y-reporte/',   ['factura electrónica', 'facturas electrónicas', 'facturación', 'facturas']),
        ('/integraciones/holded/',                    ['Holded', 'software de contabilidad', 'contabilidad']),
    ],
    'como-crear-una-experiencia-memorable-en-tu-salon-de-unas-peluqueria-o-barberia': [
        ('/funcionalidades/gestion-de-clientes/',     ['gestión de clientes', 'ficha de cliente', 'historial del cliente', 'historial']),
        ('/funcionalidades/reservas-online/',         ['reservas online', 'sistema de reservas', 'citas online']),
    ],
    'aspectos-clave-para-optimizar-tu-centro-de-estetica': [
        ('/funcionalidades/gestion-de-clientes/',     ['gestión de clientes', 'ficha de cliente', 'historial del cliente', 'historial']),
        ('/funcionalidades/reservas-online/',         ['reservas online', 'sistema de reservas', 'citas online']),
    ],
    'como-escoger-el-local-para-mi-centro-de-estetica-salon-de-unas-peluqueria-o-barberia': [
        ('/funcionalidades/gestion-de-clientes/',     ['gestión de clientes', 'ficha de cliente', 'historial', 'datos de los clientes']),
        ('/funcionalidades/reservas-online/',         ['reservas online', 'sistema de reservas', 'citas online']),
    ],
    'como-escoger-el-mejor-software-para-mi-salon-de-unas': [
        ('/precio/',                                   ['ver precios', 'los precios', 'tarifas del software', 'coste']),
        ('/funcionalidades/reservas-online/',         ['reservas online', 'sistema de reservas', 'reservas en línea']),
        ('/lista-de-espera/',                         ['prueba gratis', 'probar gratis', '30 días gratis', 'gratuita']),
    ],
    # Articles not explicitly mapped — add relevant links based on topic
    'cuanto-gana-un-salon-de-unas-en-espana': [
        ('/funcionalidades/facturacion-y-reporte/',   ['ingresos', 'facturación', 'rentabilidad', 'ganancias']),
        ('/sectores/software-para-salones-de-unas/',  ['salón de uñas', 'salones de uñas', 'negocio de uñas']),
    ],
    'cuanto-gana-una-manicurista-en-espana': [
        ('/funcionalidades/facturacion-y-reporte/',   ['ingresos', 'facturación', 'rentabilidad', 'ganancias']),
        ('/funcionalidades/reservas-online/',         ['reservas online', 'citas online', 'sistema de reservas']),
    ],
    'lampistas-fontaneros-reparaciones-software': [
        ('/funcionalidades/reservas-online/',         ['reservas online', 'citas online', 'sistema de reservas']),
        ('/funcionalidades/chat-y-notificaciones/',   ['notificaciones', 'recordatorios', 'WhatsApp']),
    ],
    'plantilla-facturacion-centros-de-estetica-excel': [
        ('/funcionalidades/facturacion-y-reporte/',   ['facturación', 'facturas', 'ingresos', 'control financiero']),
        ('/integraciones/holded/',                    ['Holded', 'contabilidad', 'software de contabilidad']),
    ],
    'requisitos-de-sanidad-para-un-salon-de-belleza': [
        ('/funcionalidades/reservas-online/',         ['reservas online', 'sistema de reservas', 'citas online']),
        ('/sectores/software-para-centro-de-estetica-y-salones/', ['software para centros de estética', 'software de gestión', 'gestión del salón']),
    ],
}

# ──────────────────────────────────────────────────────────────
# Helper functions
# ──────────────────────────────────────────────────────────────

def parse_date_iso(html):
    m = re.search(r'(\d+)\s+de\s+(\w+)\s+de\s+(\d{4})', html)
    if m:
        day, month, year = m.group(1), m.group(2).lower(), m.group(3)
        return f"{year}-{MONTHS.get(month, '01')}-{int(day):02d}"
    return '2025-01-01'

def extract_title(html):
    m = re.search(r'<title>([^<]+)</title>', html)
    if not m: return ''
    t = m.group(1).strip()
    return re.sub(r'\s*[-–|]\s*Godolphy\s*$', '', t).strip()

def extract_desc(html):
    m = re.search(r'<meta\s+name="description"\s+content="([^"]+)"', html)
    return m.group(1) if m else ''

def build_schema(title, desc, slug, date_iso):
    url = f"https://godolphy.com/{slug}/"
    obj = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": desc,
        "url": url,
        "datePublished": date_iso,
        "dateModified": date_iso,
        "author": {"@type": "Organization", "name": "Godolphy", "url": "https://godolphy.com"},
        "publisher": {
            "@type": "Organization",
            "name": "Godolphy",
            "url": "https://godolphy.com",
            "logo": {"@type": "ImageObject", "url": "https://godolphy.com/logo.png"}
        }
    }
    return f'<script type="application/ld+json">\n{json.dumps(obj, ensure_ascii=False, indent=2)}\n</script>'

def find_post_content_bounds(html):
    """Return (content_start, content_end) indices of post-content div inner text."""
    marker = '<div class="post-content">'
    idx = html.find(marker)
    if idx == -1:
        return None, None
    content_start = idx + len(marker)
    # Count div depth to find matching </div>
    depth = 1
    pos = content_start
    while pos < len(html) and depth > 0:
        next_open = html.find('<div', pos)
        next_close = html.find('</div>', pos)
        if next_close == -1:
            break
        if next_open != -1 and next_open < next_close:
            depth += 1
            pos = next_open + 4
        else:
            depth -= 1
            if depth == 0:
                return content_start, next_close
            pos = next_close + 6
    return None, None

def insert_link(content, phrase, url):
    """
    Find first occurrence of phrase in content that is NOT inside an <a> tag.
    Returns (new_content, was_replaced).
    """
    # Split by existing <a>...</a> blocks (keeping delimiters)
    parts = re.split(r'(<a\b[^>]*>.*?</a>)', content, flags=re.DOTALL | re.IGNORECASE)
    for i in range(0, len(parts), 2):  # even indices = outside existing links
        if phrase in parts[i]:
            parts[i] = parts[i].replace(phrase, f'<a href="{url}">{phrase}</a>', 1)
            return ''.join(parts), True
    return content, False

def apply_links(html, slug):
    """Add internal links into the post-content of the article."""
    rules = LINK_MAP.get(slug, [])
    if not rules:
        return html, 0

    cs, ce = find_post_content_bounds(html)
    if cs is None:
        return html, 0

    post_content = html[cs:ce]
    links_added = 0

    for url, phrases in rules:
        if links_added >= 3:
            break
        for phrase in phrases:
            new_pc, replaced = insert_link(post_content, phrase, url)
            if replaced:
                post_content = new_pc
                links_added += 1
                break  # move to next rule

    html = html[:cs] + post_content + html[ce:]
    return html, links_added

# ──────────────────────────────────────────────────────────────
# Main processing
# ──────────────────────────────────────────────────────────────

def process(slug):
    path = os.path.join(BASE, slug, 'index.html')
    if not os.path.exists(path):
        print(f"  MISSING : {slug}")
        return

    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    if GUARD in html:
        print(f"  SKIP    : {slug} (already processed)")
        return

    title    = extract_title(html)
    desc     = extract_desc(html)
    date_iso = parse_date_iso(html)
    schema   = build_schema(title, desc, slug, date_iso)

    # 1. Insert schema before </head>
    html = html.replace('</head>', f'  {GUARD}\n  {schema}\n</head>', 1)

    # 2. Add internal links
    html, n_links = apply_links(html, slug)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"  OK [{n_links} links] : {slug[:55]}  ({date_iso})")

print(f"\n{'='*60}")
print(f"  Godolphy Blog SEO — schema + links")
print(f"{'='*60}")
total = 0
for slug in BLOG_SLUGS:
    process(slug)
    total += 1
print(f"{'='*60}")
print(f"  Processed {total} articles.")
print(f"{'='*60}\n")
