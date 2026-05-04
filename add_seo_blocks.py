#!/usr/bin/env python3
import os

BASE = '/Users/neusfigueres/godolphy-static/funcionalidades'

PAGES = {
    'calendario': {
        'h2': 'Agenda online para peluquerías y centros de estética',
        'paragraphs': [
            'Llevar el control de las citas a mano o con hojas de cálculo tiene los días contados. Con Godolphy, tu peluquería o centro de estética dispone de un <a href="/funcionalidades/reservas-online/" style="color:#631cff;text-decoration:none;font-weight:600;">sistema de reservas online</a> totalmente integrado con el calendario, para que tú y tu equipo tengáis siempre una visión clara de la jornada, la semana y el mes. Los clientes pueden reservar en cualquier momento, incluso fuera del horario comercial, y el calendario se actualiza en tiempo real sin que tengas que mover un dedo.',
            'El calendario de Godolphy está diseñado pensando en los ritmos reales de un salón: cambios de última hora, servicios de distinta duración, solapamientos entre profesionales. Puedes ver la agenda de toda la semana de un vistazo o filtrar por profesional, cabina o servicio. La <a href="/funcionalidades/equipo-y-horarios/" style="color:#631cff;text-decoration:none;font-weight:600;">gestión del equipo y horarios</a> se sincroniza automáticamente, de modo que el sistema solo muestra los huecos disponibles de cada profesional según su turno real.',
            'Olvídate de las llamadas para confirmar citas o de los huecos vacíos por cancelaciones tardías. Godolphy envía recordatorios automáticos a los clientes, gestiona listas de espera y te avisa cuando un hueco queda libre. Así optimizas la ocupación de tu salón cada día, reduces el estrés en recepción y ofreces una experiencia más profesional desde el primer contacto con tu negocio.',
        ],
    },
    'equipo-y-horarios': {
        'h2': 'Gestiona tu equipo de profesionales desde un solo panel',
        'paragraphs': [
            'Coordinar los turnos, los permisos y los servicios de cada profesional puede convertirse en un quebradero de cabeza cuando el equipo crece. Godolphy centraliza toda esa información en un único panel, para que puedas configurar los horarios de trabajo, asignar servicios a cada miembro y gestionar las ausencias sin salir de la plataforma. Todo queda sincronizado automáticamente con el <a href="/funcionalidades/calendario/" style="color:#631cff;text-decoration:none;font-weight:600;">calendario de citas</a>, eliminando conflictos y dobles reservas.',
            'Cada profesional accede con sus propias credenciales y ve únicamente la información que le corresponde según el rol que le hayas asignado. Puedes distinguir entre empleados fijos, autónomos que alquilan cabina o freelances externos, y configurar los permisos de cada uno de forma independiente. De esta manera, tu centro de estética o peluquería funciona con la máxima eficiencia operativa, sin renunciar a la privacidad de los datos de negocio.',
            'La visión global del equipo también te ayuda a tomar mejores decisiones: detecta qué profesionales tienen mayor carga de trabajo, reorganiza turnos en épocas de mayor demanda y lleva un registro de horas trabajadas. Combinado con la <a href="/funcionalidades/gestion-de-clientes/" style="color:#631cff;text-decoration:none;font-weight:600;">gestión de clientes</a>, puedes además asociar a cada cliente con su profesional de confianza y garantizar continuidad en el servicio, algo que marca la diferencia en la fidelización.',
        ],
    },
    'pagos-y-depositos': {
        'h2': 'Cobra depósitos en la reserva y elimina los no-shows',
        'paragraphs': [
            'Los clientes que no aparecen sin avisar son una de las principales fuentes de pérdidas en peluquerías y centros de estética. Con Godolphy puedes solicitar un depósito en el momento de la reserva, integrado directamente con Stripe, de forma que el cliente confirma su cita con un pago parcial o total antes de llegar. Esto reduce drásticamente los no-shows y te permite cubrir esos huecos con clientes de lista de espera a través del <a href="/funcionalidades/reservas-online/" style="color:#631cff;text-decoration:none;font-weight:600;">sistema de reservas online</a>.',
            'A diferencia de plataformas como Fresha o Treatwell, Godolphy no cobra comisiones por reserva. Tú defines el importe del depósito, la política de cancelación y los plazos de devolución según las necesidades de tu negocio. El cobro automático tras el servicio simplifica además el cierre de caja diario: los pagos quedan registrados, vinculados a cada cita y disponibles para su análisis en la sección de <a href="/funcionalidades/facturacion-y-reporte/" style="color:#631cff;text-decoration:none;font-weight:600;">facturación y reportes</a>.',
            'Configurar los pagos en Godolphy lleva solo unos minutos. Puedes aceptar tarjeta, vincular un TPV físico o combinar ambas opciones según el tipo de servicio. La plataforma guarda el historial de pagos de cada cliente, lo que facilita la gestión de abonos, bonos de sesiones y tarjetas regalo. Todo ello sin papeles, sin errores y con total trazabilidad para que tu negocio cumpla con las obligaciones fiscales de forma sencilla.',
        ],
    },
    'gestion-de-clientes': {
        'h2': 'CRM para salones de belleza y centros de estética',
        'paragraphs': [
            'Conocer bien a tus clientes es la base de cualquier negocio de belleza exitoso. Godolphy incluye un CRM diseñado específicamente para peluquerías y centros de estética, donde cada cliente tiene su propia ficha con historial de visitas, servicios realizados, productos comprados, notas del profesional y preferencias personales. Esta información te permite ofrecer un trato personalizado desde la primera llamada y mejorar la experiencia en cada visita, lo que refuerza la <a href="/funcionalidades/fidelizacion-ai/" style="color:#631cff;text-decoration:none;font-weight:600;">fidelización con IA</a> que Godolphy pone a tu disposición.',
            'La base de datos de clientes se actualiza automáticamente con cada reserva, pago o interacción registrada en la plataforma. Puedes buscar clientes por nombre, teléfono, servicio habitual o fecha de última visita, y segmentar tu audiencia para lanzar campañas específicas. Identificar a los clientes más fieles, a los que llevan tiempo sin venir o a los que gastan más es cuestión de segundos, sin necesidad de exportar datos ni usar hojas de cálculo externas.',
            'Godolphy te permite también añadir alertas en la ficha de cada cliente: alergias, preferencias de producto, tono habitual de coloración o cualquier detalle que marque la diferencia en el servicio. Junto con los <a href="/funcionalidades/cupones-y-tarjetas-regalo/" style="color:#631cff;text-decoration:none;font-weight:600;">cupones y tarjetas regalo</a>, el CRM se convierte en una herramienta poderosa para retener clientes, aumentar el ticket medio y construir relaciones duraderas que sostengan el crecimiento de tu salón.',
        ],
    },
    'chat-y-notificaciones': {
        'h2': 'Recordatorios automáticos que reducen las citas perdidas',
        'paragraphs': [
            'Cada cita perdida es dinero que no entra y un hueco difícil de rellenar a última hora. Godolphy automatiza los recordatorios por WhatsApp y correo electrónico para que tus clientes no olviden sus citas en la peluquería o el centro de estética. Puedes configurar cuándo se envía cada recordatorio —24 horas antes, 2 horas antes o ambos— y personalizar el mensaje con el nombre del cliente, el servicio y el profesional asignado. Todo conectado con las <a href="/funcionalidades/reservas-online/" style="color:#631cff;text-decoration:none;font-weight:600;">reservas online</a> para que la información sea siempre exacta.',
            'El sistema de notificaciones va más allá de los simples recordatorios. Godolphy también avisa a los clientes cuando una cita ha sido modificada o cancelada, y envía confirmaciones instantáneas en cuanto se realiza una nueva reserva. Así reduces las llamadas entrantes al salón, liberas tiempo en recepción y ofreces una comunicación más ágil y profesional que la competencia. Además, los mensajes automatizados pueden activarse también para campañas de <a href="/funcionalidades/fidelizacion-ai/" style="color:#631cff;text-decoration:none;font-weight:600;">fidelización automática con IA</a>, multiplicando su impacto.',
            'Configurar las notificaciones en Godolphy no requiere conocimientos técnicos. Desde el panel de administración, defines las plantillas de mensaje, los canales preferidos y las reglas de envío en pocos pasos. El historial de comunicaciones queda registrado en la ficha de cada cliente, lo que te permite ver qué mensajes ha recibido, cuándo y si ha respondido. Una solución completa para mantener tu agenda llena y tus clientes bien informados en todo momento.',
        ],
    },
    'fidelizacion-ai': {
        'h2': 'Fidelización automática con IA para centros de estética',
        'paragraphs': [
            'Recuperar un cliente que lleva meses sin venir cuesta mucho menos que conseguir uno nuevo. Godolphy utiliza inteligencia artificial para analizar los patrones de visita de tu base de datos y detectar automáticamente qué clientes están en riesgo de abandonar tu peluquería o centro de estética. A partir de ese análisis, el sistema lanza campañas de recuperación personalizadas por WhatsApp o email, con mensajes adaptados al historial de cada persona y al tipo de servicio que solía consumir, todo conectado con la <a href="/funcionalidades/gestion-de-clientes/" style="color:#631cff;text-decoration:none;font-weight:600;">gestión de clientes y CRM</a> de Godolphy.',
            'La fidelización automática no se limita a recuperar clientes perdidos. También puedes configurar flujos de comunicación para premiar a tus clientes más fieles, felicitarles en su cumpleaños con una oferta exclusiva o invitarles a probar un servicio nuevo basándote en sus preferencias anteriores. Todo ocurre de forma automática, sin que tengas que dedicar tiempo a revisar listas ni redactar mensajes uno a uno, combinándose perfectamente con los <a href="/funcionalidades/chat-y-notificaciones/" style="color:#631cff;text-decoration:none;font-weight:600;">recordatorios automáticos por WhatsApp</a> ya activos en tu cuenta.',
            'Los resultados de cada campaña quedan registrados en el panel de Godolphy: clientes contactados, reservas generadas, ingresos atribuidos y tasa de respuesta. Esto te permite afinar la estrategia mes a mes y entender qué mensajes funcionan mejor con cada segmento de tu clientela. Una herramienta de marketing profesional incluida en tu suscripción, sin necesidad de contratar agencias ni plataformas externas.',
        ],
    },
    'facturacion-y-reporte': {
        'h2': 'Facturación automática para centros de estética',
        'paragraphs': [
            'Cerrar el mes sin tener que rebuscar entre tickets y anotaciones es posible con Godolphy. La plataforma genera automáticamente las facturas de cada servicio en el momento del pago, vinculándolas a la cita, al profesional y al cliente correspondiente. Puedes emitir facturas simplificadas o completas según el tipo de cliente, exportarlas en PDF y llevar un registro ordenado de todos los ingresos, todo integrado con el módulo de <a href="/funcionalidades/pagos-y-depositos/" style="color:#631cff;text-decoration:none;font-weight:600;">pagos y depósitos online</a> para una trazabilidad total.',
            'Los reportes de Godolphy te dan una visión clara del rendimiento de tu negocio: ingresos por profesional, por servicio, por período o por tipo de cliente. Detecta qué días son los más rentables, qué servicios generan más margen o cuáles son tus clientes de mayor valor, todo desde el mismo panel donde gestionas las citas. Esta información es clave para tomar decisiones de negocio informadas, ajustar precios o planificar promociones en momentos estratégicos del año.',
            'El sistema de facturación de Godolphy está pensado para cumplir con los requisitos fiscales en España, con la posibilidad de añadir el NIF del cliente para facturas a empresas. Si tienes un gestor o asesor contable, puede acceder directamente a los reportes exportables o recibirlos por correo de forma periódica, eliminando el trabajo manual de recopilación de datos. Para conocer todos los planes disponibles, consulta la sección de <a href="/precio/" style="color:#631cff;text-decoration:none;font-weight:600;">ver los planes y precios</a>.',
        ],
    },
    'servicios-a-domicilio': {
        'h2': 'Software para servicios a domicilio — Rutas inteligentes y reservas automáticas',
        'paragraphs': [
            'Ofrecer servicios de peluquería, estética o cuidado personal a domicilio implica coordinar desplazamientos, tiempos de viaje y disponibilidad de profesionales en tiempo real. Godolphy resuelve este reto con un módulo específico para negocios a domicilio que integra la planificación de rutas directamente con el calendario de reservas. La <a href="/funcionalidades/geolocalizacion-equipo/" style="color:#631cff;text-decoration:none;font-weight:600;">geolocalización del equipo en tiempo real</a> te permite saber dónde está cada profesional y asignar la siguiente cita al que esté más cerca, optimizando los desplazamientos y reduciendo tiempos muertos entre servicio y servicio.',
            'Los clientes reservan igual que si acudieran al salón: a través del <a href="/funcionalidades/reservas-online/" style="color:#631cff;text-decoration:none;font-weight:600;">sistema de reservas online</a> con su dirección, el servicio que necesitan y el profesional preferido. El sistema valida automáticamente si el profesional puede llegar a tiempo según su ubicación actual y la duración del servicio anterior. Una vez confirmada la reserva, el cliente recibe la confirmación y los recordatorios habituales, y el profesional ve el itinerario del día actualizado en su aplicación móvil.',
            'Gestionar un equipo itinerante sin las herramientas adecuadas genera confusión, retrasos y clientes insatisfechos. Godolphy elimina esa fricción al centralizar en un solo lugar la agenda, las rutas, los pagos y la comunicación con el cliente. Si además ofreces servicios a empresas o tienes varios profesionales en ruta simultáneamente, el panel de control te da una visión global de todas las operaciones para intervenir rápidamente ante cualquier imprevisto.',
        ],
    },
    'cupones-y-tarjetas-regalo': {
        'h2': 'Cupones y tarjetas regalo para fidelizar clientes',
        'paragraphs': [
            'Las promociones bien diseñadas no solo atraen nuevos clientes, también incentivan la repetición de visita y aumentan el ticket medio de tu peluquería o centro de estética. Godolphy incluye un módulo completo de cupones y tarjetas regalo que puedes configurar en minutos: descuentos porcentuales, importes fijos, servicios gratuitos o combinaciones de ambos. Cada cupón puede limitarse a un segmento de clientes concreto, a un período determinado o a ciertos servicios, conectándose directamente con la <a href="/funcionalidades/fidelizacion-ai/" style="color:#631cff;text-decoration:none;font-weight:600;">fidelización automática con IA</a> para enviar las ofertas en el momento más oportuno.',
            'Las tarjetas regalo son uno de los productos más demandados en el sector belleza, especialmente en épocas como Navidad, San Valentín o el Día de la Madre. Con Godolphy, puedes emitirlas digitalmente, personalizarlas con el nombre del destinatario y definir su importe y validez. El cliente que la recibe puede canjearla al hacer su reserva online sin necesidad de llamar al salón, y el sistema descuenta el importe automáticamente al cerrar el pago.',
            'Toda la actividad de cupones y tarjetas queda registrada en el historial de la <a href="/funcionalidades/gestion-de-clientes/" style="color:#631cff;text-decoration:none;font-weight:600;">gestión de clientes</a>, para que puedas ver qué promociones han sido más efectivas, cuántos cupones se han canjeado y qué ingresos han generado. Esta información te ayuda a diseñar campañas cada vez más inteligentes y a rentabilizar tus acciones de marketing sin necesidad de herramientas externas ni de un equipo dedicado.',
        ],
    },
    'multiples-ubicaciones': {
        'h2': 'Gestiona varios salones desde un único panel',
        'paragraphs': [
            'Cuando tu negocio crece y abres un segundo o tercer centro, la complejidad de la gestión se multiplica. Godolphy está pensado para cadenas de salones, franquicias y grupos de centros de estética que necesitan tener todo bajo control sin perder agilidad. Desde un único panel puedes ver la actividad de todos tus centros, gestionar reservas, consultar ingresos y supervisar el rendimiento de cada ubicación de forma independiente o consolidada, con la misma comodidad que si gestionaras un solo salón.',
            'La <a href="/funcionalidades/equipo-y-horarios/" style="color:#631cff;text-decoration:none;font-weight:600;">gestión de equipo y horarios</a> se adapta a la estructura de cada centro: cada ubicación puede tener sus propios profesionales, sus tarifas y su configuración de servicios, manteniendo una identidad operativa propia dentro de la misma cuenta. También puedes permitir que ciertos clientes reserven en cualquiera de tus centros y que su historial y ficha se compartan entre ubicaciones, ofreciendo una experiencia coherente independientemente de dónde se atienda.',
            'Para cadenas que buscan escalar, Godolphy ofrece funciones de reporte comparativo entre centros, campañas de fidelización a nivel de grupo y configuración centralizada de productos y servicios que se despliega en todas las ubicaciones con un solo clic. Si quieres conocer las condiciones específicas para gestionar varios centros, consulta la página de <a href="/precio/" style="color:#631cff;text-decoration:none;font-weight:600;">ver precios para múltiples ubicaciones</a> y descubre el plan que mejor se adapta a tu estructura.',
        ],
    },
    'geolocalizacion-equipo': {
        'h2': 'Localiza a tu equipo en tiempo real',
        'paragraphs': [
            'Cuando tus profesionales trabajan fuera del salón —a domicilio, en empresas cliente o en distintas ubicaciones— saber dónde están en cada momento es fundamental para coordinar bien el servicio. Godolphy incluye un sistema de geolocalización en tiempo real que muestra la posición de cada miembro del equipo en un mapa, actualizada automáticamente desde la aplicación móvil. Así puedes asignar la siguiente cita al profesional más cercano, estimar tiempos de llegada y responder con agilidad ante imprevistos, todo integrado con la <a href="/funcionalidades/servicios-a-domicilio/" style="color:#631cff;text-decoration:none;font-weight:600;">gestión de servicios a domicilio</a>.',
            'La geolocalización de Godolphy no es solo un mapa: está conectada con el calendario de citas y con el módulo de rutas, de modo que el sistema puede sugerirte el orden óptimo de visitas para cada profesional según su punto de partida y los destinos del día. Esto es especialmente útil para empresas de limpieza, cuidado personal, fisioterapia a domicilio o cualquier servicio que implique desplazamientos frecuentes. Para estas empresas, también puedes consultar nuestra solución específica de <a href="/sectores/software-para-empresas-de-limpieza/" style="color:#631cff;text-decoration:none;font-weight:600;">software para empresas de limpieza</a>.',
            'La privacidad del equipo está garantizada: la localización solo se activa durante el horario de trabajo configurado en la plataforma y cada profesional puede ver cuándo está siendo visible para la empresa. Los datos de geolocalización quedan registrados por jornada, lo que facilita la gestión de incidencias, la verificación de presencia en cliente y la planificación de futuros turnos en función de las zonas geográficas donde opera cada profesional.',
        ],
    },
}


def build_section(h2: str, paragraphs: list) -> str:
    p_tags = ''
    for i, text in enumerate(paragraphs):
        margin = '0 0 20px' if i < len(paragraphs) - 1 else '0'
        p_tags += f'    <p style="color:rgba(2,2,30,.75);font-size:17px;line-height:1.75;margin:{margin};">{text}</p>\n'

    return (
        '<section style="background:#fff;padding:80px 40px;">\n'
        '  <!-- SEO_TEXT_BLOCK -->\n'
        '  <div style="max-width:780px;margin:0 auto;">\n'
        f'    <h2 class="font-gabarito" style="font-size:32px;font-weight:700;color:#02021e;margin:0 0 24px;">{h2}</h2>\n'
        + p_tags +
        '  </div>\n'
        '</section>\n'
    )


def process_page(slug: str, data: dict) -> None:
    page_dir = os.path.join(BASE, slug)
    index_path = os.path.join(page_dir, 'index.html')

    if not os.path.isfile(index_path):
        print(f'MISSING  {slug}')
        return

    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'SEO_TEXT_BLOCK' in content:
        print(f'SKIP     {slug}')
        return

    footer_pos = content.find('<footer')
    if footer_pos == -1:
        print(f'NO_FOOTER {slug}')
        return

    section_html = build_section(data['h2'], data['paragraphs'])
    new_content = content[:footer_pos] + section_html + content[footer_pos:]

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f'OK       {slug}')


def main():
    for slug, data in PAGES.items():
        process_page(slug, data)


if __name__ == '__main__':
    main()
