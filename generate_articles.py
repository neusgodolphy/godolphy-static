#!/usr/bin/env python3
"""Generate 20 scheduled blog articles for /borrador/"""

import os

OUT_DIR = "/Users/neusfigueres/godolphy-static/borrador"
os.makedirs(OUT_DIR, exist_ok=True)

NAV = '''<nav style="background:#fff;border-bottom:1px solid rgba(2,2,30,.08);padding:14px 0;position:sticky;top:0;z-index:50;">
  <div style="max-width:1320px;margin:0 auto;padding:0 40px;display:flex;align-items:center;justify-content:space-between;">
    <a href="/"><img src="/wp-images/logo-violeta.png" alt="Godolphy" style="height:36px;width:auto;" loading="lazy" /></a>
    <ul style="display:flex;gap:32px;list-style:none;margin:0;padding:0;">
      <li><a href="/sectores/" style="color:#02021e;font-size:14px;font-weight:500;text-decoration:none;">Sectores</a></li>
      <li><a href="/funcionalidades/" style="color:#02021e;font-size:14px;font-weight:500;text-decoration:none;">Funcionalidades</a></li>
      <li><a href="/blog/" style="color:#02021e;font-size:14px;font-weight:500;text-decoration:none;">Blog</a></li>
      <li><a href="/precio/" style="color:#02021e;font-size:14px;font-weight:500;text-decoration:none;">Precio</a></li>
    </ul>
    <div style="display:flex;gap:12px;">
      <a href="#" style="border:2px solid #631cff;color:#631cff;font-size:14px;font-weight:600;padding:8px 28px;border-radius:20px;text-decoration:none;">Demo</a>
      <a href="/lista-de-espera/" style="background:#631cff;color:#fff;font-size:14px;font-weight:600;padding:8px 28px;border-radius:20px;text-decoration:none;">Lista de espera</a>
    </div>
    <button id="nav-hamburger" onclick="toggleMobileNav()" aria-label="Abrir menú" style="display:none;flex-direction:column;justify-content:center;gap:5px;background:none;border:none;cursor:pointer;padding:4px;">
      <span style="display:block;width:24px;height:2px;background:#02021e;border-radius:2px;"></span>
      <span style="display:block;width:24px;height:2px;background:#02021e;border-radius:2px;"></span>
      <span style="display:block;width:24px;height:2px;background:#02021e;border-radius:2px;"></span>
    </button>
  </div>
</nav>
<div id="mobile-nav" style="display:none;position:fixed;inset:0;z-index:200;background:linear-gradient(160deg,#9B4FE8 0%,#7835C3 30%,#631cff 65%,#3a0aaa 100%);flex-direction:column;padding:24px 24px 40px;">
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:48px;">
    <a href="/"><img src="/wp-images/logo.png" alt="Godolphy" style="height:36px;width:auto;"/></a>
    <button onclick="toggleMobileNav()" aria-label="Cerrar menú" style="background:none;border:none;cursor:pointer;padding:4px;">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M18 6L6 18M6 6l12 12" stroke="#fff" stroke-width="2" stroke-linecap="round"/></svg>
    </button>
  </div>
  <nav style="display:flex;flex-direction:column;gap:0;flex:1;">
    <a href="/sectores/" style="color:#fff;font-size:22px;font-weight:600;text-decoration:none;padding:18px 0;border-bottom:1px solid rgba(255,255,255,.15);font-family:'Gabarito',sans-serif;">Sectores</a>
    <a href="/funcionalidades/" style="color:#fff;font-size:22px;font-weight:600;text-decoration:none;padding:18px 0;border-bottom:1px solid rgba(255,255,255,.15);font-family:'Gabarito',sans-serif;">Funcionalidades</a>
    <a href="/blog/" style="color:#fff;font-size:22px;font-weight:600;text-decoration:none;padding:18px 0;border-bottom:1px solid rgba(255,255,255,.15);font-family:'Gabarito',sans-serif;">Blog</a>
    <a href="/precio/" style="color:#fff;font-size:22px;font-weight:600;text-decoration:none;padding:18px 0;border-bottom:1px solid rgba(255,255,255,.15);font-family:'Gabarito',sans-serif;">Precio</a>
  </nav>
  <div style="display:flex;flex-direction:column;gap:12px;margin-top:32px;">
    <a href="#" style="background:#EEFE3A;color:#631cff;font-size:16px;font-weight:700;padding:14px 24px;border-radius:20px;text-decoration:none;text-align:center;">Demo</a>
    <a href="/lista-de-espera/" style="border:2px solid #fff;color:#fff;font-size:16px;font-weight:700;padding:14px 24px;border-radius:20px;text-decoration:none;text-align:center;">Lista de espera</a>
  </div>
</div>
<script>
function toggleMobileNav(){
  var o=document.getElementById('mobile-nav');
  var open=o.style.display==='flex';
  o.style.display=open?'none':'flex';
  document.body.style.overflow=open?'':'hidden';
}
</script>'''

FOOTER = '''<footer style="background:#02021e;padding:80px 40px 40px;width:100%;max-width:100%;overflow-x:hidden;box-sizing:border-box"><div style="max-width:1200px;margin:0 auto;"><div style="display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:60px;margin-bottom:60px;"><div><img src="/wp-images/logo.png" alt="Godolphy" style="height:36px;margin-bottom:20px;display:block;width:auto;"/><p style="color:rgba(255,255,255,.5);font-size:14px;line-height:1.7;max-width:280px;margin:0;">El software de reservas con IA para negocios de servicios.</p></div><div><h3 style="color:#fff;font-size:13px;font-weight:600;margin:0 0 20px;letter-spacing:.05em;">INDUSTRIAS</h3><ul style="list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:12px;"><li><a href="/sectores/software-para-peluquerias/" style="color:rgba(255,255,255,.5);font-size:14px;text-decoration:none;">Peluquería</a></li><li><a href="/sectores/software-para-barberias/" style="color:rgba(255,255,255,.5);font-size:14px;text-decoration:none;">Barbería</a></li><li><a href="/sectores/software-para-centro-de-estetica-y-salones/" style="color:rgba(255,255,255,.5);font-size:14px;text-decoration:none;">Centro de estética</a></li><li><a href="/sectores/software-para-salones-de-unas/" style="color:rgba(255,255,255,.5);font-size:14px;text-decoration:none;">Salón de uñas</a></li><li><a href="/sectores/software-para-empresas-de-limpieza/" style="color:rgba(255,255,255,.5);font-size:14px;text-decoration:none;">Empresa de limpieza</a></li></ul></div><div><h3 style="color:#fff;font-size:13px;font-weight:600;margin:0 0 20px;letter-spacing:.05em;">FUNCIONALIDADES</h3><ul style="list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:12px;"><li><a href="/funcionalidades/reservas-online/" style="color:rgba(255,255,255,.5);font-size:14px;text-decoration:none;">Reservas online</a></li><li><a href="/funcionalidades/calendario/" style="color:rgba(255,255,255,.5);font-size:14px;text-decoration:none;">Calendario</a></li><li><a href="/funcionalidades/equipo-y-horarios/" style="color:rgba(255,255,255,.5);font-size:14px;text-decoration:none;">Equipo y horarios</a></li><li><a href="/funcionalidades/pagos-y-depositos/" style="color:rgba(255,255,255,.5);font-size:14px;text-decoration:none;">Pagos y depósitos</a></li><li><a href="/funcionalidades/gestion-de-clientes/" style="color:rgba(255,255,255,.5);font-size:14px;text-decoration:none;">Gestión de clientes</a></li><li><a href="/funcionalidades/chat-y-notificaciones/" style="color:rgba(255,255,255,.5);font-size:14px;text-decoration:none;">Chat y notificaciones</a></li><li><a href="/funcionalidades/fidelizacion-ai/" style="color:rgba(255,255,255,.5);font-size:14px;text-decoration:none;">Fidelización AI</a></li><li><a href="/funcionalidades/facturacion-y-reporte/" style="color:rgba(255,255,255,.5);font-size:14px;text-decoration:none;">Facturación y reporte</a></li></ul></div><div><h3 style="color:#fff;font-size:13px;font-weight:600;margin:0 0 20px;letter-spacing:.05em;">RECURSOS</h3><ul style="list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:12px;"><li><a href="/blog/" style="color:rgba(255,255,255,.5);font-size:14px;text-decoration:none;">Blog</a></li><li><a href="/precio/" style="color:rgba(255,255,255,.5);font-size:14px;text-decoration:none;">Precio</a></li><li><a href="/lista-de-espera/" style="color:rgba(255,255,255,.5);font-size:14px;text-decoration:none;">Lista de espera</a></li></ul></div></div><div style="border-top:1px solid rgba(255,255,255,.1);padding-top:32px;display:flex;justify-content:space-between;align-items:center;"><p style="color:rgba(255,255,255,.3);font-size:13px;margin:0;">© 2025 Godolphy. Todos los derechos reservados.</p><div style="display:flex;gap:24px;"><a href="/politica-de-privacidad/" style="color:rgba(255,255,255,.3);font-size:13px;text-decoration:none;">Privacidad</a><a href="/terminos-y-condiciones/" style="color:rgba(255,255,255,.3);font-size:13px;text-decoration:none;">Términos</a><a href="/politica-de-cookies/" style="color:rgba(255,255,255,.3);font-size:13px;text-decoration:none;">Cookies</a></div></div></div></footer>'''

STYLES = '''  <style>
    body{font-family:'Poppins',sans-serif;margin:0;overflow-x:hidden;color:#02021e;}
    .font-gabarito{font-family:'Gabarito',sans-serif;}
    .post-content h2{font-family:'Gabarito',sans-serif;font-size:22px;font-weight:700;color:#111827;margin:48px 0 16px;line-height:1.2;}
    .post-content h3{font-family:'Gabarito',sans-serif;font-size:18px;font-weight:700;color:#111827;margin:32px 0 12px;}
    .post-content p{font-size:17px;line-height:1.8;color:#374151;margin:0 0 20px;}
    .post-content ul,ol{margin:0 0 20px;padding-left:22px;}
    .post-content li{font-size:17px;line-height:1.8;color:#374151;margin-bottom:8px;}
    .post-content strong{color:#111827;font-weight:600;}
    .post-content a{color:#631cff;text-decoration:none;}
    .post-content a:hover{text-decoration:underline;}
    .post-content table{width:100%;border-collapse:collapse;margin:24px 0;font-size:15px;}
    .post-content th{background:#f8f7ff;font-weight:600;color:#111827;padding:10px 14px;text-align:left;border:1px solid rgba(2,2,30,.1);}
    .post-content td{padding:10px 14px;border:1px solid rgba(2,2,30,.1);color:#374151;vertical-align:top;}
    .disclaimer{background:#fef9c3;border-left:4px solid #eab308;padding:16px 20px;border-radius:8px;margin:0 0 32px;font-size:15px;color:#713f12;}
    @media(max-width:768px){nav ul{display:none!important;}nav>div>div{display:none!important;}nav>div{padding:0 20px!important;}#nav-hamburger{display:flex!important;}.post-content h2{font-size:19px;}.post-content p,.post-content li{font-size:16px;}}
    @media(max-width:768px){div[style*="grid-template-columns:2fr 1fr 1fr 1fr"]{grid-template-columns:1fr!important;gap:32px!important;}}
    footer{box-sizing:border-box;width:100%;overflow-x:hidden;}
    @media(max-width:768px){footer{padding:48px 20px 24px!important;}footer > div{padding:0!important;max-width:100%!important;}div[style*="justify-content:space-between;align-items:center"]{flex-direction:column!important;align-items:flex-start!important;gap:16px!important;}footer div[style*="display:flex;gap:24px"]{flex-wrap:wrap!important;}}
    @media(max-width:768px){div[style*="grid-template-columns:2fr 1fr 1fr 1fr"] > div:nth-child(n+2),div[style*="grid-template-columns:1fr 1fr 1fr 1fr"] > div:nth-child(n+2){display:none!important;}div[style*="grid-template-columns:2fr 1fr 1fr 1fr"],div[style*="grid-template-columns:1fr 1fr 1fr 1fr"]{grid-template-columns:1fr!important;gap:0!important;margin-bottom:32px!important;}.footer-mobile-cta{display:inline-block!important;}}
  </style>'''

CTA = '''  <div style="margin:56px 0 0;padding:48px 40px;background:radial-gradient(ellipse at 30% 40%,#6B2FFF 0%,#8B20CC 50%,#7B1099 100%);border-radius:24px;text-align:center;">
    <h2 class="font-gabarito" style="font-family:'Gabarito',sans-serif;font-size:28px;font-weight:700;color:#fff;margin:0 0 12px;line-height:1.2;">¿Quieres probar Godolphy en tu negocio?</h2>
    <p style="font-size:16px;color:rgba(255,255,255,.85);margin:0 0 28px;line-height:1.6;">30 días gratis, sin tarjeta de crédito.</p>
    <a href="/lista-de-espera/" style="display:inline-block;background:#EEFE3A;color:#02021e;font-size:15px;font-weight:700;padding:14px 36px;border-radius:20px;text-decoration:none;">Empezar gratis</a>
  </div>'''


def build(filename, title_tag, desc, canonical, h1, date_iso, date_human, schema_headline, content_html):
    slug = canonical.rstrip('/').split('/')[-1]
    schema = f'''  <script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{schema_headline}",
  "description": "{desc}",
  "url": "{canonical}",
  "datePublished": "{date_iso}",
  "dateModified": "{date_iso}",
  "author": {{
    "@type": "Organization",
    "name": "Godolphy",
    "url": "https://godolphy.com"
  }},
  "publisher": {{
    "@type": "Organization",
    "name": "Godolphy",
    "url": "https://godolphy.com",
    "logo": {{
      "@type": "ImageObject",
      "url": "https://godolphy.com/wp-images/logo.png"
    }}
  }}
}}
</script>'''

    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title_tag} - Godolphy</title>
  <meta name="description" content="{desc}" />
  <link rel="canonical" href="{canonical}" />
  <link rel="preload" href="https://cdn.tailwindcss.com" as="script">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="preload" href="https://fonts.googleapis.com/css2?family=Gabarito:wght@400;600;700;800&family=Poppins:wght@300;400;500;600&display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gabarito:wght@400;600;700;800&family=Poppins:wght@300;400;500;600&display=swap"></noscript>
{STYLES}
{schema}
</head>
<body style="overflow-x:hidden">

{NAV}

<main>
<article style="max-width:780px;margin:0 auto;padding:60px 40px 80px;">

  <div style="margin-bottom:24px;">
    <a href="/blog/" style="font-size:13px;color:rgba(2,2,30,.4);text-decoration:none;">Blog</a>
    <span style="font-size:13px;color:rgba(2,2,30,.25);margin:0 6px;">/</span>
    <span style="font-size:13px;color:rgba(2,2,30,.4);">Consejos de negocio</span>
  </div>

  <h1 class="font-gabarito" style="font-size:40px;font-weight:700;color:#02021e;line-height:1.15;margin:0 0 24px;">{h1}</h1>

  <div style="display:flex;align-items:center;gap:16px;margin-bottom:40px;padding-bottom:32px;border-bottom:1px solid rgba(2,2,30,.08);">
    <span style="font-size:14px;color:rgba(2,2,30,.45);">{date_human}</span>
    <span style="width:4px;height:4px;border-radius:50%;background:rgba(2,2,30,.2);display:inline-block;"></span>
    <span style="font-size:14px;color:rgba(2,2,30,.45);">Godolphy</span>
  </div>

  <div class="post-content">
{content_html}
{CTA}
  </div>

</article>
</main>

{FOOTER}

</body>
</html>'''
    path = os.path.join(OUT_DIR, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Created: {filename}")


# ─── ARTICLE 1 ────────────────────────────────────────────────────────────────
build(
    filename="2026-05-12-mejor-software-peluquerias-espana.html",
    title_tag="Mejor software para peluquerías en España 2026",
    desc="Comparativa honesta de los mejores programas de gestión para peluquerías en España: Koibox, Booksy, Fresha, Shortcuts y Godolphy. Precios, funciones y para quién es cada uno.",
    canonical="https://godolphy.com/mejor-software-peluquerias-espana/",
    h1="Mejor software para peluquerías en España 2026 — Comparativa real",
    date_iso="2026-05-12",
    date_human="12 de mayo de 2026",
    schema_headline="Mejor software para peluquerías en España 2026 — Comparativa real",
    content_html='''
    <p>Elegir el software para tu peluquería es una de las decisiones más importantes que puedes tomar para tu negocio. Un buen programa no solo ahorra tiempo: reduce los no-shows, mejora la experiencia del cliente y te da información real sobre qué está funcionando y qué no. Pero el mercado está lleno de opciones y cada una promete ser la mejor. En este artículo analizamos las cinco más utilizadas en España con datos reales.</p>

    <h2>Por qué importa elegir bien el software de tu peluquería</h2>
    <p>El software de gestión es la columna vertebral operativa de tu negocio. De él depende cómo llegan las reservas, cómo se comunica el equipo con los clientes, cómo se cobran los servicios y cómo entiendes la rentabilidad de tu negocio. Una mala elección no solo supone dinero desperdiciado: supone tiempo perdido, clientes frustrados y decisiones tomadas a ciegas.</p>
    <p>Los criterios que más importan al elegir son: el precio mensual real (con todas las funciones activadas), si incluye WhatsApp automático, si permite servicios a domicilio, si tiene inteligencia artificial para análisis o fidelización, y si cobra comisiones sobre tus reservas.</p>

    <h2>Comparativa de los 5 principales softwares para peluquerías en España</h2>
    <table>
      <thead>
        <tr><th>Software</th><th>Precio desde</th><th>Trial</th><th>WhatsApp</th><th>Domicilio</th><th>IA</th><th>Comisiones</th></tr>
      </thead>
      <tbody>
        <tr><td>Koibox</td><td>~35€/mes</td><td>Sí, 30 días</td><td>Sí (extra)</td><td>No</td><td>No</td><td>No</td></tr>
        <tr><td>Booksy</td><td>~30€/mes</td><td>Sí, 14 días</td><td>No</td><td>No</td><td>No</td><td>No</td></tr>
        <tr><td>Fresha</td><td>0€ base</td><td>Sin trial (freemium)</td><td>No</td><td>No</td><td>No</td><td>Sí (2,19% + 0,20€)</td></tr>
        <tr><td>Shortcuts</td><td>~80€/mes</td><td>Sí</td><td>Sí</td><td>No</td><td>No</td><td>No</td></tr>
        <tr><td>Godolphy</td><td>33€/mes</td><td>Sí, 30 días</td><td>Sí</td><td>Sí</td><td>Sí</td><td>No</td></tr>
      </tbody>
    </table>

    <h2>Koibox — el veterano del mercado español</h2>
    <p>Koibox es probablemente el software más conocido en España. Lleva muchos años en el mercado y tiene una base de usuarios amplia. Su interfaz es madura, el soporte en español es bueno y la integración con TPV físico está bien trabajada. El inconveniente principal es que las funciones avanzadas (WhatsApp, múltiples ubicaciones) elevan el precio considerablemente. Tampoco tiene servicios a domicilio ni análisis con IA. Es una buena opción para peluquerías establecidas que buscan estabilidad por encima de innovación.</p>

    <h2>Booksy — fuerte en captación de clientes nuevos</h2>
    <p>Booksy funciona como un marketplace además de como software de gestión. Sus clientes pueden encontrarte en el directorio de Booksy, lo que puede traer reservas nuevas. Sin embargo, eso tiene un precio: dependes de su plataforma para la visibilidad y no construyes una relación directa con el cliente. La comunicación automática por WhatsApp no está disponible y la personalización es limitada. Ideal si empiezas y necesitas visibilidad rápida, pero puede resultar restrictivo a largo plazo.</p>

    <h2>Fresha — el más popular globalmente, con letra pequeña</h2>
    <p>Fresha ofrece un plan base gratuito que suena muy atractivo. El problema está en las comisiones: cada reserva que llega a través de su marketplace tiene un coste de 2,19% + 0,20€ por transacción. Para un negocio con volumen, esa cifra puede superar fácilmente lo que pagarías en una suscripción mensual. Si la mayoría de tus clientes vienen por tu propia red y no por el directorio de Fresha, el plan gratuito puede ser razonable. Pero hay que calcularlo bien.</p>

    <h2>Shortcuts — la opción enterprise</h2>
    <p>Shortcuts está orientado a cadenas y franquicias con varios centros. Tiene un nivel de personalización muy alto y funciones avanzadas de gestión multiubicación. El precio es proporcional: empieza en torno a los 80€/mes y sube con cada módulo adicional. Para una peluquería independiente o un equipo pequeño, probablemente es más de lo que necesitas y más de lo que quieres pagar.</p>

    <h2>Godolphy — para quién es la mejor opción</h2>
    <p>Godolphy está diseñado específicamente para negocios que combinan atención en local con servicios a domicilio, y para quienes quieren usar la inteligencia artificial para crecer sin necesitar un equipo de analistas. El copiloto financiero analiza automáticamente qué servicios son más rentables, qué días tienes la agenda floja y qué clientes están en riesgo de no volver. Desde <a href="/precio/">33€/mes</a>, incluye WhatsApp automático, depósitos y sin comisiones sobre reservas.</p>

    <h2>Conclusión: para quién es cada uno</h2>
    <ul>
      <li><strong>Koibox</strong> — peluquerías con años de trayectoria que buscan estabilidad y soporte local.</li>
      <li><strong>Booksy</strong> — negocios nuevos que necesitan visibilidad y captar clientes rápido.</li>
      <li><strong>Fresha</strong> — negocios con pocos clientes nuevos del marketplace y que quieren empezar con coste cero.</li>
      <li><strong>Shortcuts</strong> — cadenas y franquicias con múltiples centros y presupuesto alto.</li>
      <li><strong>Godolphy</strong> — peluquerías que ofrecen domicilio, quieren IA real y no quieren pagar comisiones.</li>
    </ul>
    <p>Si quieres una comparativa más detallada con Koibox, consulta nuestra <a href="/alternativa-a-koibox/">página de alternativa a Koibox</a>.</p>
'''
)

# ─── ARTICLE 2 ────────────────────────────────────────────────────────────────
build(
    filename="2026-05-14-como-usar-inteligencia-artificial-peluqueria.html",
    title_tag="Cómo usar la inteligencia artificial en tu peluquería 2026",
    desc="La IA ya no es solo para grandes empresas. Descubre cómo los salones de belleza están usando la inteligencia artificial para crecer, fidelizar clientes y mejorar su rentabilidad.",
    canonical="https://godolphy.com/como-usar-inteligencia-artificial-peluqueria/",
    h1="Cómo usar la inteligencia artificial en tu peluquería en 2026",
    date_iso="2026-05-14",
    date_human="14 de mayo de 2026",
    schema_headline="Cómo usar la inteligencia artificial en tu peluquería en 2026",
    content_html='''
    <p>Hace cinco años, hablar de inteligencia artificial en una peluquería sonaba a ciencia ficción. Hoy es una realidad que está cambiando cómo los negocios de belleza gestionan su día a día, retienen clientes y toman decisiones. La buena noticia: no necesitas conocimientos técnicos ni un equipo de datos para aprovecharlo. Solo el software adecuado.</p>

    <h2>¿Qué puede hacer la IA por tu peluquería?</h2>
    <p>La inteligencia artificial aplicada a una peluquería no es un robot que corta el pelo. Es un sistema que analiza los datos de tu negocio (reservas, pagos, patrones de visita, servicios) y los convierte en información útil y acciones automáticas. En la práctica, esto se traduce en cuatro áreas concretas:</p>
    <ul>
      <li><strong>Recordatorios inteligentes:</strong> no solo envía un recordatorio 24 horas antes, sino que aprende cuándo cada cliente tiene más probabilidad de confirmar o cancelar.</li>
      <li><strong>Análisis financiero automático:</strong> detecta qué servicios te generan más margen real, no solo más ingresos.</li>
      <li><strong>Detección de clientes en riesgo:</strong> identifica clientas que llevan más tiempo del habitual sin reservar y lanza acciones de recuperación.</li>
      <li><strong>Predicción de demanda:</strong> anticipa qué días tendrás la agenda llena y cuáles floja, para que puedas actuar antes.</li>
    </ul>

    <h2>Análisis financiero automático</h2>
    <p>La mayoría de propietarios de peluquerías saben cuánto facturan, pero pocos saben qué servicios les dejan más dinero después de descontar el tiempo del profesional y el coste del producto. Un corte de 25€ que dura 30 minutos puede ser más rentable que un tratamiento de 80€ que ocupa dos horas y media.</p>
    <p>La IA de Godolphy calcula automáticamente la rentabilidad por servicio teniendo en cuenta la duración, el coste estimado de producto y el tiempo del profesional. También identifica los días de la semana con menor ocupación de agenda, para que puedas lanzar una promoción o bloquear horas antes de que se queden vacías.</p>
    <p>Accede a este análisis desde <a href="/funcionalidades/facturacion-y-reporte/">Facturación y reporte</a>, sin necesidad de exportar datos ni usar Excel.</p>

    <h2>Fidelización inteligente</h2>
    <p>Una clienta que viene cada tres semanas y de repente lleva seis semanas sin aparecer es una señal de alerta. Sin IA, esa señal pasa desapercibida. Con IA, el sistema la detecta automáticamente y puede enviarte una alerta o directamente lanzar un mensaje personalizado a esa clienta antes de que se vaya a la competencia.</p>
    <p>El módulo de <a href="/funcionalidades/fidelizacion-ai/">Fidelización AI</a> de Godolphy analiza el patrón de visita de cada cliente individualmente. Si alguien solía venir cada 4 semanas y lleva 7 sin reservar, el sistema lo marca como cliente en riesgo. Puedes configurar qué mensaje enviar, con qué incentivo y en qué momento.</p>
    <p>El resultado práctico: menos clientes perdidos sin que tengas que hacer nada manualmente.</p>

    <h2>Predicción de demanda y optimización de agenda</h2>
    <p>La IA también puede ayudarte a llenar los huecos antes de que sean un problema. Si históricamente los martes por la mañana son tu momento más flojo, el sistema puede sugerirte lanzar una mini-campaña el lunes por la tarde. Si hay un festivo próximo que históricamente genera un pico de reservas, puede avisarte para que ajustes el equipo con tiempo.</p>
    <p>Esta predicción no es perfecta, pero es infinitamente mejor que gestionar la agenda completamente a ciegas.</p>

    <h2>¿Necesito conocimientos técnicos para usar la IA de Godolphy?</h2>
    <p>No. Ese es el principio de diseño de todo el sistema. No hay modelos que configurar, no hay parámetros que ajustar, no hay datos que limpiar. El copiloto de IA de Godolphy se activa desde el primer día y trabaja con los datos de tu negocio desde el momento en que empiezas a usarlo. Cuantos más datos acumula, más precisas son las recomendaciones.</p>
    <p>No necesitas saber qué es un algoritmo. Solo necesitas mirar el panel de recomendaciones y actuar.</p>

    <h2>El coste de no usar IA</h2>
    <p>Cada cliente que se pierde sin que te hayas dado cuenta, cada servicio poco rentable que sigues ofreciendo con el mismo precio de hace tres años, cada martes por la tarde con agenda medio vacía que podrías haber llenado... todo eso tiene un coste real en euros. La IA no es el futuro del sector belleza: es el presente. Y los negocios que la están usando ya están tomando mejores decisiones que sus competidores.</p>
'''
)

# ─── ARTICLE 3 ────────────────────────────────────────────────────────────────
build(
    filename="2026-05-19-software-peluqueria-gratis-vs-pago.html",
    title_tag="Software peluquería gratis vs de pago — qué merece la pena",
    desc="¿Merece la pena un software gratuito para gestionar tu peluquería? Analizamos qué ofrecen las opciones gratis y en qué momento compensa pagar.",
    canonical="https://godolphy.com/software-peluqueria-gratis-vs-pago/",
    h1="Software para peluquería gratis vs de pago — qué merece la pena",
    date_iso="2026-05-19",
    date_human="19 de mayo de 2026",
    schema_headline="Software para peluquería gratis vs de pago — qué merece la pena",
    content_html='''
    <p>Lo gratuito siempre atrae. Cuando empiezas un negocio o cuando quieres reducir gastos, la idea de gestionar tu peluquería sin pagar nada al mes parece irresistible. Pero como en casi todo, lo gratuito tiene un precio. En este artículo analizamos honestamente qué puedes esperar de las opciones sin coste y cuándo tiene sentido hacer la transición a un plan de pago.</p>

    <h2>Qué suelen incluir los planes gratuitos</h2>
    <p>La mayoría de softwares para peluquerías que ofrecen un plan gratuito incluyen las funciones más básicas: un calendario de citas, un perfil público donde los clientes pueden reservar y algún tipo de recordatorio por email. Eso es suficiente para empezar, pero tiene limitaciones importantes:</p>
    <ul>
      <li>Número máximo de citas al mes (habitualmente entre 50 y 100)</li>
      <li>Sin recordatorios por WhatsApp (solo email, con tasas de apertura mucho menores)</li>
      <li>Sin posibilidad de cobrar depósitos al reservar</li>
      <li>Sin análisis ni informes de negocio</li>
      <li>Sin gestión de varios profesionales</li>
      <li>Soporte limitado o inexistente</li>
      <li>En el caso de Fresha: comisiones sobre reservas del marketplace</li>
    </ul>

    <h2>El coste oculto de lo gratuito</h2>
    <p>El coste más grande de un software gratuito no está en la factura mensual (que es cero), sino en lo que no hace por ti. Analicemos tres casos concretos:</p>
    <p><strong>Los no-shows.</strong> Sin depósitos obligatorios al reservar, las cancelaciones de última hora y las no presentaciones son mucho más frecuentes. En una peluquería que mueve 80 citas al mes con un ticket medio de 45€, incluso un 10% de no-shows supone 360€ al mes en ingresos perdidos. Un software de pago que cuesta 35€/mes y reduce los no-shows al 2% se paga diez veces solo.</p>
    <p><strong>La comunicación manual.</strong> Sin WhatsApp automático, tienes que enviar tú los recordatorios o confiar en que el cliente se acuerde. Eso son minutos al día que se convierten en horas al mes, y horas que podrías dedicar a trabajar o descansar.</p>
    <p><strong>Las decisiones a ciegas.</strong> Sin informes, no sabes qué servicios te generan más margen, qué días son más rentables o qué clientes llevan demasiado tiempo sin volver. Gestionar sin datos es gestionar por intuición, y la intuición se equivoca.</p>

    <h2>Cuándo tiene sentido pagar</h2>
    <p>Hay un momento claro en el que la inversión en software de pago se amortiza: cuando tienes más de 40-50 citas al mes. A partir de ese volumen, los no-shows duelen en la factura, la comunicación manual consume demasiado tiempo y necesitas datos para tomar buenas decisiones.</p>
    <p>Si empiezas y tienes menos de 20 citas al mes, un plan gratuito puede ser suficiente para los primeros meses. Pero tan pronto como el negocio empiece a tener tracción, el salto a un plan de pago no es un gasto: es una inversión.</p>

    <h2>Qué debería incluir un buen software de pago para peluquerías</h2>
    <ul>
      <li>Reservas online con página propia (sin depender de un marketplace)</li>
      <li>Recordatorios automáticos por WhatsApp</li>
      <li>Cobro de depósitos al reservar para eliminar no-shows</li>
      <li>Gestión del equipo con horarios y permisos diferenciados</li>
      <li>Informes de facturación y rentabilidad por servicio</li>
      <li>Sin comisiones sobre tus propias reservas</li>
      <li>Soporte real en caso de problemas</li>
    </ul>

    <h2>El cálculo real: no-show vs coste del software</h2>
    <p>Supongamos una peluquería con 60 citas al mes, ticket medio de 40€ y una tasa de no-show del 8%:</p>
    <ul>
      <li>No-shows al mes: ~5 citas</li>
      <li>Ingresos perdidos: ~200€/mes</li>
      <li>Coste de Godolphy con depósitos: <a href="/precio/">desde 33€/mes</a></li>
      <li>Reducción estimada de no-shows con depósito obligatorio: 70-80%</li>
      <li>Ahorro mensual neto: ~140€ - 33€ = más de 100€/mes en positivo</li>
    </ul>
    <p>Los <a href="/funcionalidades/pagos-y-depositos/">depósitos automáticos</a> son, por sí solos, uno de los elementos más rentables de cualquier software de gestión para peluquerías.</p>

    <h2>Conclusión</h2>
    <p>Lo gratuito tiene sentido al principio, cuando el volumen es bajo y el presupuesto es ajustado. Pero en cuanto el negocio empieza a moverse, el coste real de no tener WhatsApp automático, depósitos y análisis supera ampliamente el coste de una suscripción mensual. No es un gasto: es recuperar ingresos que ya estás perdiendo.</p>
'''
)

# ─── ARTICLE 4 ────────────────────────────────────────────────────────────────
build(
    filename="2026-05-21-como-recuperar-clientes-peluqueria.html",
    title_tag="Cómo recuperar clientes que dejaron de venir a tu salón",
    desc="Perder una clienta habitual cuesta más que captarla. Estas estrategias te ayudan a detectarlas a tiempo y recuperarlas antes de que sea demasiado tarde.",
    canonical="https://godolphy.com/como-recuperar-clientes-peluqueria/",
    h1="Cómo recuperar clientes que dejaron de venir a tu peluquería o salón",
    date_iso="2026-05-21",
    date_human="21 de mayo de 2026",
    schema_headline="Cómo recuperar clientes que dejaron de venir a tu peluquería o salón",
    content_html='''
    <p>Captar una clienta nueva cuesta entre 5 y 7 veces más que retener a una que ya tienes. Y sin embargo, la mayoría de peluquerías y salones dedican mucho más esfuerzo a atraer clientes nuevos que a recuperar las que ya perdieron. En este artículo te explicamos cómo detectar a tiempo cuando una clienta está a punto de irse, y qué hacer para recuperarla.</p>

    <h2>El coste real de perder una clienta</h2>
    <p>Una clienta habitual que viene cada cuatro semanas y gasta una media de 50€ por visita genera 650€ al año. Si tienes 200 clientas y pierdes el 15% cada año (que es una tasa habitual), estás perdiendo 30 clientas × 650€ = 19.500€ anuales en ingresos que ya tenías asegurados. Sustituirlas con clientas nuevas requiere inversión en marketing, tiempo y oferta inicial, con márgenes mucho más bajos.</p>
    <p>Dicho de otro modo: recuperar una clienta que se está yendo cuesta mucho menos que captarla de cero.</p>

    <h2>Por qué se van las clientas</h2>
    <p>Antes de actuar, es importante entender por qué se van. Las razones más habituales son:</p>
    <ul>
      <li><strong>Olvido o pérdida de rutina:</strong> un cambio de trabajo, mudanza o simplemente el caos del día a día hace que dejen de mantener la frecuencia de visita.</li>
      <li><strong>Falta de comunicación:</strong> si no recibes ningún recordatorio de que llevas tiempo sin venir, simplemente no lo piensan.</li>
      <li><strong>Mala experiencia puntual:</strong> un servicio que no quedó bien, una espera innecesaria o un malentendido que nunca se resolvió.</li>
      <li><strong>Competencia más cómoda:</strong> una peluquería más cerca, con mejor app o más fácil de reservar.</li>
      <li><strong>Precio:</strong> aunque suele ser la última razón real, es la primera que dan cuando te preguntan.</li>
    </ul>

    <h2>Cómo detectar una clienta en riesgo</h2>
    <p>El primer paso es dejar de gestionar la fidelización por intuición. No puedes acordarte de cuánto tiempo lleva cada clienta sin venir. Necesitas un sistema que lo haga por ti.</p>
    <p>Los indicadores de riesgo más claros son:</p>
    <ul>
      <li>Ha pasado el doble del tiempo habitual entre visitas sin nueva reserva</li>
      <li>Canceló la última cita y no reprogramó</li>
      <li>Su gasto por visita ha bajado en las últimas visitas (servicio más corto, sin extras)</li>
      <li>No ha respondido al último recordatorio</li>
    </ul>

    <h2>Estrategias de recuperación que funcionan</h2>
    <p>Una vez identificada la clienta en riesgo, el momento de actuar es ahora. Esperar más solo reduce las probabilidades de éxito.</p>
    <p><strong>El mensaje personalizado:</strong> un mensaje que menciona su nombre, el servicio que solía hacer y cuánto tiempo lleva sin aparecer tiene una tasa de respuesta mucho mayor que un mensaje genérico. No hace falta un descuento: a veces basta con que noten que las recuerdas.</p>
    <p><strong>La oferta exclusiva:</strong> si el mensaje solo no funciona, añade un incentivo. No tiene que ser un descuento grande. Un "te reservamos tu hora habitual del martes con X incluido" puede ser suficiente para activar la decisión.</p>
    <p><strong>El recordatorio de servicio pendiente:</strong> si sabes que hace tiempo que no hace un tratamiento que necesita con regularidad (tinte, retoque, manicura), mencionarlo crea urgencia natural sin parecer agresivo.</p>

    <h2>El momento clave para actuar</h2>
    <p>La ventana de recuperación varía según el tipo de servicio:</p>
    <ul>
      <li><strong>Manicura / pedicura:</strong> actuar a las 4-5 semanas sin visita</li>
      <li><strong>Corte de pelo:</strong> actuar a las 7-8 semanas</li>
      <li><strong>Tinte / coloración:</strong> actuar a las 7-9 semanas</li>
      <li><strong>Tratamientos de spa:</strong> actuar a los 45-60 días</li>
    </ul>
    <p>Pasado ese tiempo, la probabilidad de recuperación cae significativamente. La clienta ya ha encontrado otra opción o ha normalizado no venir.</p>

    <h2>Cómo automatizar la recuperación con Godolphy</h2>
    <p>El módulo de <a href="/funcionalidades/fidelizacion-ai/">Fidelización AI</a> de Godolphy monitoriza automáticamente la frecuencia de visita de cada cliente. Cuando detecta una anomalía (demasiado tiempo sin reservar), genera una alerta y puede enviar automáticamente un mensaje personalizado por WhatsApp.</p>
    <p>Puedes configurar cuándo activar la alerta (por ejemplo, a los 30 días para manicura o 45 para corte), qué mensaje enviar y si incluir algún incentivo. Todo sin que tengas que recordar ni revisar manualmente tu lista de clientes.</p>
    <p>El módulo de <a href="/funcionalidades/gestion-de-clientes/">Gestión de clientes</a> te da la vista completa del historial de cada clienta: qué servicios ha hecho, cuánto ha gastado, cuándo fue la última vez y cómo responde a los mensajes.</p>
'''
)

# ─── ARTICLE 5 ────────────────────────────────────────────────────────────────
build(
    filename="2026-05-26-cuanto-cuesta-software-centro-estetica.html",
    title_tag="¿Cuánto cuesta un software para centro de estética? 2026",
    desc="Analizamos los precios reales de los principales programas de gestión para centros de estética en España. Desde 0€ hasta más de 100€/mes.",
    canonical="https://godolphy.com/cuanto-cuesta-software-centro-estetica/",
    h1="¿Cuánto cuesta un software para centro de estética en 2026?",
    date_iso="2026-05-26",
    date_human="26 de mayo de 2026",
    schema_headline="¿Cuánto cuesta un software para centro de estética en 2026?",
    content_html='''
    <p>El mercado de software para centros de estética tiene una horquilla de precios muy amplia: desde cero euros al mes hasta más de 150€ dependiendo del proveedor y las funciones activadas. Entender qué incluye cada rango de precio es fundamental para tomar una decisión que se adapte a tu negocio sin pagar por lo que no necesitas ni quedarte corto cuando el negocio crezca.</p>

    <h2>Software gratuito (0€/mes)</h2>
    <p>Existen opciones sin coste mensual, el ejemplo más conocido es Fresha en su versión base. Permiten gestionar reservas básicas, tener un perfil público en su marketplace y enviar confirmaciones por email. Las limitaciones son importantes: no hay WhatsApp automático, no hay depósitos, no hay informes avanzados y, en el caso de Fresha, hay comisiones del 2,19% + 0,20€ por cada reserva que llegue a través de su directorio.</p>
    <p>Son útiles para negocios que empiezan con muy poco volumen o que quieren probar cómo funciona la gestión digital antes de comprometerse con un plan de pago.</p>

    <h2>Software básico (15-30€/mes)</h2>
    <p>En este rango encontramos planes de entrada de proveedores como Koibox Free o Booksy en sus versiones más económicas. Suelen incluir reservas online, calendario, algunos recordatorios automáticos y gestión básica de clientes. Las funciones que quedan fuera de este rango son habitualmente el WhatsApp, los pagos online con depósito y los informes detallados.</p>
    <p>Para un centro de estética con 1-2 profesionales y menos de 60 citas al mes, puede ser un punto de partida razonable.</p>

    <h2>Software medio (30-60€/mes)</h2>
    <p>Aquí se concentra la mayoría de opciones que tienen sentido para un centro de estética en funcionamiento. En este rango encontramos:</p>
    <ul>
      <li><strong>Godolphy Solo (33€/mes):</strong> reservas online, WhatsApp automático, depósitos, IA de fidelización y análisis financiero. Sin comisiones.</li>
      <li><strong>Booksy Boost:</strong> añade herramientas de marketing y visibilidad en el marketplace.</li>
      <li><strong>Koibox Basic:</strong> incluye más profesionales y funciones de punto de venta.</li>
    </ul>
    <p>Para la mayoría de centros de estética independientes con 1-3 profesionales, este rango ofrece la mejor relación calidad-precio. Las funciones incluidas (especialmente depósitos y WhatsApp) tienen un impacto directo en la facturación que supera con creces el coste mensual.</p>
    <p>Consulta los <a href="/precio/">precios de Godolphy</a> con detalle de funciones por plan.</p>

    <h2>Software avanzado (60-100€/mes)</h2>
    <p>A partir de los 60€/mes, los planes suelen añadir más profesionales incluidos, módulos de stock y productos, TPV integrado, gestión de programas de puntos más sofisticados y en algunos casos informes personalizables. Koibox Pro y algunos planes avanzados de Booksy entran en este rango.</p>
    <p>Es el rango adecuado para centros con 4 o más profesionales, o con un volumen de facturación que justifica herramientas más especializadas de análisis y marketing.</p>

    <h2>Software enterprise (+100€/mes)</h2>
    <p>Flowww y Shortcuts son los ejemplos más habituales en este rango. Están pensados para cadenas, franquicias o centros grandes que necesitan gestión multiubicación, integración con sistemas de contabilidad, módulos de formación de equipo y niveles de personalización muy altos. Para un centro de estética independiente, raramente tiene sentido llegar a este nivel de inversión.</p>

    <h2>Qué factores encarecen el precio</h2>
    <p>Más allá del plan base, el precio de un software para centros de estética sube por varios motivos:</p>
    <ul>
      <li><strong>Número de profesionales:</strong> la mayoría de planes base incluyen 1-2. Cada profesional adicional tiene un coste.</li>
      <li><strong>WhatsApp Business API:</strong> el envío real de mensajes por WhatsApp tiene un coste de operador que los proveedores repercuten de diferentes formas.</li>
      <li><strong>Módulos de IA:</strong> las funciones de análisis inteligente y fidelización automática suelen estar en planes superiores.</li>
      <li><strong>Múltiples ubicaciones:</strong> gestionar dos centros desde un solo panel siempre tiene un coste adicional.</li>
    </ul>

    <h2>Tabla resumen de precios orientativos</h2>
    <table>
      <thead>
        <tr><th>Rango</th><th>Precio</th><th>Para quién</th></tr>
      </thead>
      <tbody>
        <tr><td>Gratuito</td><td>0€</td><td>Negocios que empiezan, volumen muy bajo</td></tr>
        <tr><td>Básico</td><td>15-30€/mes</td><td>1-2 profesionales, pocas citas</td></tr>
        <tr><td>Medio</td><td>30-60€/mes</td><td>Centro en funcionamiento, 1-4 profesionales</td></tr>
        <tr><td>Avanzado</td><td>60-100€/mes</td><td>Equipos de 4+, alto volumen</td></tr>
        <tr><td>Enterprise</td><td>+100€/mes</td><td>Cadenas, franquicias, multiubicación</td></tr>
      </tbody>
    </table>
    <p>Si quieres comparar funciones concretas con Koibox, visita nuestra <a href="/alternativa-a-koibox/">comparativa con Koibox</a>.</p>
'''
)

print("\nArticles 1-5 created.")
