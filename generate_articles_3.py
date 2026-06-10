#!/usr/bin/env python3
"""Generate articles 11-20 for /borrador/"""
import os, sys
sys.path.insert(0, '/Users/neusfigueres/godolphy-static')
from generate_articles import build, OUT_DIR

# ─── ARTICLE 11 ────────────────────────────────────────────────────────────────
build(
    filename="2026-06-16-organizar-rutas-servicios-domicilio-estetica.html",
    title_tag="Cómo organizar rutas para servicios a domicilio estética",
    desc="Organizar rutas para profesionales que se desplazan es uno de los mayores retos del domicilio. Descubre cómo automatizarlo.",
    canonical="https://godolphy.com/organizar-rutas-servicios-domicilio-estetica/",
    h1="Cómo organizar rutas para servicios a domicilio de estética y peluquería",
    date_iso="2026-06-16",
    date_human="16 de junio de 2026",
    schema_headline="Cómo organizar rutas para servicios a domicilio de estética y peluquería",
    content_html='''
    <p>Gestionar una agenda de servicios a domicilio parece sencillo desde fuera: confirmas las citas, asignas los profesionales y listo. La realidad es mucho más compleja. Una agenda de domicilio mal organizada genera retrasos en cadena, clientes insatisfechos, profesionales agotados por desplazamientos ineficientes y facturación desperdiciada en tiempo de viaje no rentabilizado. En este artículo explicamos cómo organizarlo bien, manual o automáticamente.</p>

    <h2>El error más común: confundir disponibilidad con posibilidad</h2>
    <p>Este es el fallo que más frecuentemente genera problemas en los negocios de domicilio. Una profesional que termina a las 11:00 en el barrio de Eixample está "disponible" a las 11:00 en términos de agenda. Pero si la siguiente cita está en Horta (35 minutos de trayecto), en realidad no puede empezar antes de las 11:35. Una app que no calcula esto va a crear solapamientos constantemente.</p>
    <p>La diferencia entre disponibilidad teórica (el hueco en el calendario) y disponibilidad real (cuándo puede llegar físicamente) es el concepto más importante en la gestión de servicios móviles.</p>

    <h2>Cómo calcular el tiempo real entre clientes</h2>
    <p>Para calcular correctamente la disponibilidad real de un profesional de domicilio, el sistema necesita saber tres cosas:</p>
    <ol>
      <li><strong>Duración del servicio anterior</strong> — cuándo termina realmente (incluyendo el tiempo de recogida de materiales y despedida).</li>
      <li><strong>Ubicación al terminar</strong> — la dirección del cliente anterior, no el punto de base del profesional.</li>
      <li><strong>Tiempo de desplazamiento al siguiente cliente</strong> — calculado según tráfico real, no distancia en línea recta.</li>
    </ol>
    <p>La suma de estos tres factores da la hora mínima real a la que puede empezar el próximo servicio. Todo lo que se acepte antes de esa hora generará un retraso.</p>

    <h2>Optimización de rutas por zona geográfica</h2>
    <p>La optimización más eficiente es la más simple: agrupar los clientes del mismo día en la misma zona o zonas contiguas. Si un martes tienes tres clientes en el norte de la ciudad y dos en el sur, lo más eficiente es hacer primero los tres del norte y luego desplazarse al sur, en lugar de ir y volver varias veces.</p>
    <p>Esta optimización puede hacerse manualmente en un negocio pequeño (1-2 profesionales, pocos clientes). En cuanto el volumen crece, necesitas una herramienta que lo haga automáticamente en el momento de la reserva: asigna al profesional más cercano disponible y la ruta más eficiente para el día.</p>

    <h2>Gestión del punto de partida del profesional</h2>
    <p>Otro detalle que pocos sistemas gestionan bien: ¿desde dónde empieza el profesional el día? Hay tres escenarios posibles:</p>
    <ul>
      <li><strong>Desde local:</strong> el más simple. El punto de partida siempre es el mismo.</li>
      <li><strong>Desde casa:</strong> el punto de partida varía por profesional y puede estar en cualquier parte de la ciudad.</li>
      <li><strong>Desde el último cliente del día anterior:</strong> en zonas densas, algunos negocios calculan la ruta del día siguiente desde donde terminó el día anterior.</li>
    </ul>
    <p>El sistema debe poder configurar esto por profesional y tenerlo en cuenta al calcular la primera disponibilidad del día.</p>

    <h2>Precio del desplazamiento por distancia</h2>
    <p>Cada kilómetro de desplazamiento tiene un coste real: tiempo del profesional, gasolina o transporte, desgaste del vehículo. Si no lo repercutes en el precio del servicio, lo estás absorbiendo tú como margen perdido.</p>
    <p>La forma más transparente es definir zonas geográficas con precios fijos de desplazamiento. El cliente ve el precio total antes de confirmar y no hay sorpresas. Una zona central gratuita, una zona intermedia con un cargo moderado y una zona exterior con un cargo mayor es el esquema más habitual y el que genera menos fricción.</p>

    <h2>Cómo lo automatiza Godolphy</h2>
    <p>El módulo de <a href="/funcionalidades/servicios-a-domicilio/">servicios a domicilio</a> de Godolphy gestiona automáticamente la disponibilidad real (con tiempo de desplazamiento incluido), asigna al profesional más cercano disponible en el momento de la reserva y aplica el precio de desplazamiento por zona configurado. El cliente ve un precio total claro desde el primer momento.</p>
    <p>Para empresas de limpieza con equipos más grandes, la página de <a href="/sectores/software-para-empresas-de-limpieza/">software para empresas de limpieza</a> tiene información específica sobre la gestión de equipos móviles.</p>
'''
)

# ─── ARTICLE 12 ────────────────────────────────────────────────────────────────
build(
    filename="2026-06-18-que-es-ticket-medio-peluqueria.html",
    title_tag="Qué es el ticket medio en una peluquería y cómo mejorarlo",
    desc="El ticket medio es la facturación media por visita. Entender esta métrica y saber cómo mejorarla puede transformar la rentabilidad de tu negocio.",
    canonical="https://godolphy.com/que-es-ticket-medio-peluqueria/",
    h1="Qué es el ticket medio en una peluquería y cómo mejorarlo",
    date_iso="2026-06-18",
    date_human="18 de junio de 2026",
    schema_headline="Qué es el ticket medio en una peluquería y cómo mejorarlo",
    content_html='''
    <p>Si gestionas una peluquería, probablemente sabes cuánto has facturado este mes. Pero ¿sabes cuánto gasta en promedio cada cliente cada vez que viene? Esa cifra se llama ticket medio y es una de las métricas más importantes para entender la salud de tu negocio y encontrar dónde puedes crecer sin aumentar la carga de trabajo.</p>

    <h2>Qué es exactamente el ticket medio</h2>
    <p>El ticket medio (también llamado valor medio por visita o gasto medio por cliente) mide cuánto gasta de promedio cada cliente en una sola visita a tu peluquería. No es lo mismo que la facturación total ni que el número de clientes: es el cruce entre ambos.</p>
    <p><strong>Fórmula:</strong> Ticket medio = Facturación total del período ÷ Número de visitas del mismo período</p>
    <p><strong>Ejemplo real:</strong> Si en mayo facturaste 8.400€ y atendiste a 210 visitas, tu ticket medio fue de 40€. Si en junio facturas los mismos 8.400€ pero con solo 180 visitas, tu ticket medio sube a 46,7€. Mismos ingresos, menos trabajo.</p>

    <h2>Ticket medio según tipo de negocio</h2>
    <p>Los rangos varían bastante según el tipo de servicio y la ubicación:</p>
    <table>
      <thead>
        <tr><th>Tipo de negocio</th><th>Ticket medio bajo</th><th>Ticket medio alto</th></tr>
      </thead>
      <tbody>
        <tr><td>Peluquería corte básico</td><td>15-20€</td><td>35-45€</td></tr>
        <tr><td>Peluquería con coloración</td><td>40€</td><td>90-120€</td></tr>
        <tr><td>Barbería</td><td>15€</td><td>35-45€</td></tr>
        <tr><td>Salón de uñas</td><td>25€</td><td>55-70€</td></tr>
        <tr><td>Centro de estética</td><td>40€</td><td>80-120€</td></tr>
        <tr><td>Spa / masajes</td><td>50€</td><td>100-150€</td></tr>
      </tbody>
    </table>
    <p>Si tu ticket medio está en la parte baja de tu categoría, hay margen de mejora sin subir precios: simplemente haciendo que los clientes combinen más servicios por visita.</p>

    <h2>Qué influye en el ticket medio</h2>
    <p>Los factores que más determinan el ticket medio de una peluquería son:</p>
    <ul>
      <li><strong>Combinación de servicios:</strong> un cliente que hace corte + tinte + tratamiento gasta el triple que uno que solo hace el corte.</li>
      <li><strong>Extras y complementos:</strong> masaje de cuero cabelludo, hidratación, nail art... cada extra añade 8-20€ al ticket.</li>
      <li><strong>Packs y bonos:</strong> los clientes que compran bonos anticipados gastan más de media que los que pagan por servicio suelto.</li>
      <li><strong>Nivel del profesional:</strong> un especialista en coloración o en técnicas avanzadas tiene un ticket natural más alto.</li>
      <li><strong>Momento de la venta:</strong> ofrecer extras en el momento de la reserva online tiene mayor tasa de aceptación que ofrecerlos en el local.</li>
    </ul>

    <h2>5 formas concretas de subir el ticket medio</h2>
    <p><strong>1. Extras en la reserva online.</strong> Cuando la clienta reserva su corte, ofrécele añadir un tratamiento de hidratación o un masaje de cuero cabelludo con un clic. La tasa de aceptación en el momento de la reserva es sorprendentemente alta porque la clienta ya está en modo "compra".</p>
    <p><strong>2. Packs estratégicos.</strong> Un pack de corte + tratamiento al precio de corte + 15€ (en lugar de los 25€ que costaría el tratamiento por separado) parece una oferta para la clienta y sube tu ticket medio.</p>
    <p><strong>3. Upselling natural en el servicio.</strong> Durante la visita, el profesional puede mencionar que ve el cabello seco o que el cuero cabelludo necesita atención. No es presión: es diagnóstico y recomendación profesional. Hay que entrenarlo.</p>
    <p><strong>4. Fidelización VIP.</strong> Las clientas más frecuentes y las que más gastan merecen un trato especial: acceso anticipado a nuevos servicios, un servicio extra de vez en cuando. Esto incentiva a las de ticket bajo a subir su gasto para acceder al estatus.</p>
    <p><strong>5. Precios diferenciados por profesional.</strong> Si tienes una especialista senior, sus servicios pueden tener un precio un 20-30% superior al del resto del equipo. Los clientes que la prefieren pagarán ese diferencial sin problema.</p>

    <h2>Cómo medir el ticket medio en Godolphy</h2>
    <p>El módulo de <a href="/funcionalidades/facturacion-y-reporte/">Facturación y reporte</a> calcula automáticamente el ticket medio por período, por profesional y por tipo de servicio. Puedes ver en qué mes subió, en cuál bajó y qué cambios coincidieron con esas variaciones. Eso es exactamente lo que necesitas para tomar decisiones informadas, sin hojas de cálculo ni cálculos manuales.</p>
    <p>Si quieres saber cuánto cobrar exactamente por tus servicios, visita también nuestra guía de <a href="/precio/">precios de Godolphy</a> para entender cómo se amortizan las herramientas de análisis.</p>
'''
)

# ─── ARTICLE 13 ────────────────────────────────────────────────────────────────
build(
    filename="2026-06-23-gestionar-freelances-centro-estetica.html",
    title_tag="Cómo gestionar freelances en tu centro de estética",
    desc="Cada vez más centros trabajan con freelances además de empleados. Descubre cómo gestionarlos sin perder el control de tu negocio.",
    canonical="https://godolphy.com/gestionar-freelances-centro-estetica/",
    h1="Cómo gestionar colaboradores freelance en tu centro de estética",
    date_iso="2026-06-23",
    date_human="23 de junio de 2026",
    schema_headline="Cómo gestionar colaboradores freelance en tu centro de estética",
    content_html='''
    <p>El modelo mixto —empleados fijos más colaboradores autónomos— se ha convertido en una de las formas más comunes de gestionar un centro de estética. Permite ajustar la capacidad a la demanda, incorporar especialistas sin el compromiso de una nómina fija y probar profesionales antes de contratarlos. Pero también genera retos de gestión que, sin las herramientas adecuadas, pueden convertirse en un dolor de cabeza diario.</p>

    <h2>Diferencias clave entre empleado y freelance en un salón</h2>
    <p>La diferencia no es solo contractual. Tiene implicaciones directas en cómo gestionas su acceso al sistema, qué información pueden ver y cómo se calculan sus ingresos:</p>
    <ul>
      <li><strong>Contrato:</strong> el empleado tiene nómina y relación laboral. El freelance es autónomo que factura al centro.</li>
      <li><strong>Acceso a datos:</strong> el empleado puede ver la agenda del centro. El freelance solo debería ver sus propias citas.</li>
      <li><strong>Responsabilidad:</strong> el empleado trabaja bajo la dirección del centro. El freelance tiene mayor autonomía en cómo ejecuta su trabajo.</li>
      <li><strong>Datos de clientes:</strong> un freelance no debería poder descargar la base de datos de clientes del centro. Esa es información del negocio, no del colaborador.</li>
    </ul>

    <h2>Qué puede ver un freelance y qué no debería ver</h2>
    <p>Esta es una de las preguntas más frecuentes cuando se configura un software para un equipo mixto. La regla general es simple: el freelance necesita ver todo lo necesario para hacer su trabajo, y nada más.</p>
    <p><strong>Debería ver:</strong> su propia agenda del día, los datos de contacto del cliente (nombre, teléfono para emergencias), el servicio a realizar y el tiempo asignado.</p>
    <p><strong>No debería ver:</strong> la facturación total del centro, los datos de clientes de otros profesionales, los precios de los servicios de sus compañeros, ni los informes financieros del negocio.</p>
    <p>En Godolphy, los permisos por perfil permiten configurar exactamente qué ve cada colaborador, con niveles diferenciados entre propietario, empleado y freelance.</p>

    <h2>Aceptación de servicios: el modelo de elección</h2>
    <p>En algunos centros, los freelances tienen la opción de aceptar o rechazar los servicios que les llegan. Esto es especialmente habitual en domicilio, donde el profesional puede evaluar si la ubicación y el tipo de servicio le compensa. El sistema debe poder gestionar esta dinámica sin crear caos en la agenda.</p>
    <p>El flujo recomendado es: el cliente reserva, el sistema asigna al freelance más apropiado y disponible, el freelance tiene un tiempo determinado (por ejemplo, 30 minutos) para aceptar. Si no acepta, el sistema pasa al siguiente disponible. Si ninguno acepta, el sistema avisa al propietario para gestión manual.</p>

    <h2>Comisiones y pagos a freelances</h2>
    <p>Hay dos modelos principales de reparto:</p>
    <ul>
      <li><strong>Porcentaje del servicio:</strong> el freelance se queda con un % de cada servicio que realiza (habitualmente entre el 40% y el 60% según el acuerdo). El centro retiene el resto.</li>
      <li><strong>Alquiler de cabina:</strong> el freelance paga una tarifa fija por usar el espacio y se queda con el 100% de sus servicios.</li>
    </ul>
    <p>Independientemente del modelo, el software debe calcular automáticamente lo que corresponde a cada freelance al final del período, sin que tengas que hacer cálculos manuales. El módulo de <a href="/funcionalidades/facturacion-y-reporte/">Facturación y reporte</a> de Godolphy genera los informes de comisiones por profesional con un clic.</p>

    <h2>Gestión del equipo: horarios y disponibilidad</h2>
    <p>Un freelance suele tener horarios irregulares o que cambian semana a semana. El sistema debe permitirle actualizar su disponibilidad de forma autónoma sin que eso afecte al resto de la agenda ni cree conflictos. En <a href="/funcionalidades/equipo-y-horarios/">Equipo y horarios</a>, cada colaborador puede gestionar su propia disponibilidad semanal y bloquear períodos sin necesidad de contactar al propietario.</p>

    <h2>El riesgo de no gestionar bien a los freelances</h2>
    <p>Un freelance que tiene acceso a la base de datos de clientes del centro puede, al terminar su colaboración, llevarse esa lista. Un freelance cuyas comisiones se calculan manualmente puede generar disputas si los números no cuadran. Un freelance que no puede gestionar su propia agenda genera trabajo administrativo extra al propietario. Todos estos riesgos se mitigan con el sistema adecuado y los permisos bien configurados desde el primer día.</p>
'''
)

# ─── ARTICLE 14 ────────────────────────────────────────────────────────────────
build(
    filename="2026-06-25-analisis-financiero-centro-estetica.html",
    title_tag="Análisis financiero para centros de estética — métricas clave",
    desc="La mayoría de centros de estética no analizan sus números. Descubre qué métricas importan de verdad y cómo usarlas para tomar mejores decisiones.",
    canonical="https://godolphy.com/analisis-financiero-centro-estetica/",
    h1="Análisis financiero para centros de estética — métricas que importan",
    date_iso="2026-06-25",
    date_human="25 de junio de 2026",
    schema_headline="Análisis financiero para centros de estética — métricas que importan",
    content_html='''
    <p>La mayoría de propietarias de centros de estética saben cuánto han facturado este mes. Pocas saben qué servicio les deja más dinero neto, qué profesional es más rentable por hora trabajada o qué porcentaje de sus clientes no han vuelto en los últimos 60 días. La diferencia entre saber cuánto facturas y saber cómo creces es el análisis financiero. Y no requiere ni un contable ni un MBA: requiere los datos correctos.</p>

    <h2>Por qué gestionar sin datos es gestionar a ciegas</h2>
    <p>Imagina que tienes dos servicios en tu menú: una limpieza facial a 45€ que dura 60 minutos y un masaje relajante a 60€ que dura 90 minutos. ¿Cuál es más rentable? La respuesta intuitiva es el masaje: genera más ingresos por sesión. Pero si calculas la rentabilidad por hora, la limpieza genera 45€/hora y el masaje 40€/hora. La limpieza es más rentable.</p>
    <p>Sin análisis, podrías estar promoviendo el servicio menos rentable sin saberlo. Con análisis, puedes tomar decisiones sobre precios, promociones y foco del negocio basadas en datos reales.</p>

    <h2>Las 6 métricas financieras clave para un centro de estética</h2>
    <ul>
      <li><strong>Facturación total:</strong> el número más básico. Importante pero insuficiente por sí solo.</li>
      <li><strong>Ticket medio:</strong> facturación dividida entre número de visitas. Mide el gasto promedio por cliente por visita.</li>
      <li><strong>Tasa de ocupación:</strong> porcentaje de horas disponibles que están ocupadas con servicios. El indicador más directo de eficiencia operativa.</li>
      <li><strong>Rentabilidad por servicio:</strong> margen neto de cada servicio después de descontar tiempo del profesional y coste de producto.</li>
      <li><strong>Tasa de retención:</strong> qué porcentaje de clientes vuelven en un período determinado. Un 70% de retención es un buen referente.</li>
      <li><strong>Coste de adquisición por cliente:</strong> cuánto gastas en marketing para conseguir un cliente nuevo vs cuánto vale ese cliente a lo largo del tiempo.</li>
    </ul>

    <h2>Rentabilidad por servicio: el análisis que cambia todo</h2>
    <p>Para calcular la rentabilidad real de un servicio necesitas tres datos: el precio que cobras, la duración del servicio (que es el coste de tiempo del profesional) y el coste del producto utilizado.</p>
    <p>La fórmula básica: Rentabilidad = Precio - (Duración en horas × Coste por hora del profesional) - Coste de producto</p>
    <p>El coste por hora del profesional incluye su salario o comisión, más la parte proporcional de los gastos fijos del centro (alquiler, suministros, amortización de equipos). Un cálculo realista suele situar este número entre 15€ y 30€/hora según el tipo de negocio y la ubicación.</p>
    <p>Con este análisis puedes decidir qué servicios potenciar, cuáles ajustar en precio y cuáles eliminar del menú porque no compensan.</p>

    <h2>Tasa de ocupación: el termómetro de tu agenda</h2>
    <p>La ocupación se calcula como: horas vendidas ÷ horas disponibles × 100. Una ocupación por encima del 75% es el objetivo habitual en centros de estética bien gestionados. Por debajo del 60%, hay problemas de demanda o de gestión de agenda.</p>
    <p>Lo importante no es solo la ocupación media, sino la distribución: si el martes por la mañana tienes el 30% de ocupación y el sábado estás al 100%, hay una oportunidad clara de mover demanda con precios diferenciados o promociones específicas para los días flojos.</p>

    <h2>Coste por hora de cada profesional</h2>
    <p>No todos los profesionales de un centro generan el mismo valor por hora trabajada. Una especialista en tratamientos avanzados puede generar 60-80€/hora mientras que una técnica junior genera 25-35€. Saber este dato por profesional permite tomar mejores decisiones sobre contratación, formación y asignación de servicios.</p>

    <h2>Cómo el copiloto IA de Godolphy automatiza este análisis</h2>
    <p>Calcular todo esto manualmente requiere exportar datos, cruzar tablas y hacer cálculos que consumen horas. El módulo de <a href="/funcionalidades/facturacion-y-reporte/">Facturación y reporte</a> de Godolphy lo calcula automáticamente y lo presenta en un panel claro. El copiloto de <a href="/funcionalidades/fidelizacion-ai/">Fidelización AI</a> añade la capa de análisis de comportamiento de cliente: qué clientes están en riesgo, cuál es la tendencia de retención y qué acciones recomienda para mejorarla.</p>
    <p>No necesitas ser analista para usar esta información. Necesitas mirar el panel y actuar.</p>
'''
)

# ─── ARTICLE 15 ────────────────────────────────────────────────────────────────
build(
    filename="2026-06-30-automatizar-recordatorios-citas-salon.html",
    title_tag="Cómo automatizar recordatorios de citas en tu salón",
    desc="Los recordatorios automáticos reducen los no-shows hasta un 70%. Descubre cómo configurarlos y qué canal funciona mejor.",
    canonical="https://godolphy.com/automatizar-recordatorios-citas-salon/",
    h1="Cómo automatizar los recordatorios de citas en tu salón de belleza",
    date_iso="2026-06-30",
    date_human="30 de junio de 2026",
    schema_headline="Cómo automatizar los recordatorios de citas en tu salón de belleza",
    content_html='''
    <p>Un no-show no es solo un hueco en la agenda: es tiempo perdido, ingresos perdidos y, en muchos casos, un coste de producto preparado para nada. Los estudios del sector estiman que entre el 8% y el 15% de las citas en salones de belleza terminan en no-show o cancelación de última hora. La buena noticia es que gran parte de ese problema tiene solución: recordatorios automáticos bien configurados pueden reducir esa cifra hasta el 2-3%.</p>

    <h2>Cuánto cuestan los no-shows en euros</h2>
    <p>Hagamos el cálculo para un salón con 80 citas al mes, ticket medio de 45€ y un 10% de no-shows:</p>
    <ul>
      <li>No-shows al mes: 8 citas</li>
      <li>Ingresos perdidos: 360€/mes</li>
      <li>Ingresos perdidos al año: 4.320€</li>
    </ul>
    <p>Un software que cuesta 35€/mes y reduce los no-shows al 2% te ahorra 300€ al mes: se amortiza en cuatro días.</p>

    <h2>WhatsApp vs SMS vs email — qué funciona mejor en España</h2>
    <p>La elección del canal no es baladí. Las tasas de apertura y respuesta varían mucho:</p>
    <table>
      <thead>
        <tr><th>Canal</th><th>Tasa de apertura</th><th>Tasa de respuesta</th><th>Tiempo de lectura</th></tr>
      </thead>
      <tbody>
        <tr><td>WhatsApp</td><td>95-98%</td><td>45-60%</td><td>Menos de 5 min</td></tr>
        <tr><td>SMS</td><td>85-90%</td><td>15-20%</td><td>Menos de 10 min</td></tr>
        <tr><td>Email</td><td>20-30%</td><td>5-8%</td><td>Variable, a veces horas</td></tr>
      </tbody>
    </table>
    <p>En España, WhatsApp es claramente el canal preferido para comunicaciones personales y de negocio cercano. Un recordatorio de cita por WhatsApp tiene casi garantizada la lectura. Un recordatorio por email puede perderse en la bandeja de entrada o en el spam.</p>

    <h2>Cuándo enviar el recordatorio</h2>
    <p>La investigación del sector apunta a dos momentos óptimos:</p>
    <ul>
      <li><strong>Confirmación inmediata:</strong> justo después de que el cliente reserva. Confirma los detalles y establece la política de cancelación desde el primer momento.</li>
      <li><strong>Recordatorio 24 horas antes:</strong> el momento de mayor impacto. Da tiempo para confirmar o cancelar con suficiente antelación para que puedas ofrecer el hueco a otro cliente.</li>
    </ul>
    <p>Algunos negocios añaden un tercer mensaje 2-3 horas antes, especialmente para tratamientos largos o servicios con alta preparación previa. Úsalo con moderación: demasiados mensajes generan molestia.</p>

    <h2>Qué debe incluir el mensaje de recordatorio</h2>
    <p>Un buen recordatorio de cita incluye:</p>
    <ul>
      <li>Nombre del cliente (personalización básica que marca la diferencia)</li>
      <li>Día y hora exactos de la cita</li>
      <li>Nombre del servicio y del profesional asignado</li>
      <li>Dirección del centro o, en domicilio, confirmación de la dirección del cliente</li>
      <li>Política de cancelación de forma breve y clara</li>
      <li>Un enlace o instrucción para confirmar o cancelar</li>
    </ul>
    <p>Ejemplo: "Hola Ana, te recordamos tu cita de manicura con Laura mañana martes 14 a las 17:30 en C/ Valencia 123. Para cancelar o cambiar la hora, hazlo antes de las 17:30 de hoy. ¡Hasta mañana! 💜"</p>

    <h2>Confirmación activa: pedir que respondan</h2>
    <p>El recordatorio más efectivo no es el que informa: es el que pide una acción. Un mensaje que dice "Confirma tu cita respondiendo SÍ a este mensaje" tiene una tasa de respuesta mucho mayor que uno que solo informa. Y si no responden en un tiempo determinado, el sistema puede alertarte para que puedas gestionar ese hueco manualmente.</p>

    <h2>Cómo configurarlo en Godolphy</h2>
    <p>El módulo de <a href="/funcionalidades/chat-y-notificaciones/">Chat y notificaciones</a> de Godolphy incluye la configuración de recordatorios automáticos por WhatsApp. Puedes personalizar el mensaje, elegir cuándo se envía y activar la confirmación activa. Combinado con <a href="/funcionalidades/pagos-y-depositos/">Pagos y depósitos</a>, tienes la combinación más efectiva contra los no-shows: el cliente recibe el recordatorio y, si no había pagado depósito, puede hacerlo directamente desde el mensaje.</p>
'''
)

# ─── ARTICLE 16 ────────────────────────────────────────────────────────────────
build(
    filename="2026-07-02-calcular-precio-desplazamiento-domicilio.html",
    title_tag="Cómo calcular el precio del desplazamiento a domicilio",
    desc="Cobrar el desplazamiento correctamente es clave para que los servicios a domicilio sean rentables. Guía práctica con ejemplos reales.",
    canonical="https://godolphy.com/calcular-precio-desplazamiento-domicilio/",
    h1="Cómo calcular y cobrar el desplazamiento en servicios a domicilio",
    date_iso="2026-07-02",
    date_human="2 de julio de 2026",
    schema_headline="Cómo calcular y cobrar el desplazamiento en servicios a domicilio",
    content_html='''
    <p>El desplazamiento es el gran agujero invisible de la rentabilidad en los servicios a domicilio. Los profesionales que no lo cobran correctamente están regalando tiempo y dinero sin darse cuenta. Los que lo cobran de forma opaca (añadiéndolo sin avisar al final) generan mala experiencia y conflictos con los clientes. La clave es calcularlo bien y comunicarlo con transparencia desde el momento de la reserva.</p>

    <h2>Por qué el desplazamiento no cobrado destruye el margen</h2>
    <p>Pongamos números concretos. Una esteticista que cobra 60€ por una sesión de un hora a domicilio parece que gana bien. Pero si incluye 30 minutos de desplazamiento de ida y 30 de vuelta, realmente está dedicando 2 horas a esa cita. Su ingreso real por hora de trabajo es 30€, no 60€.</p>
    <p>Si su coste por hora (tiempo, transporte, materiales) es de 20€, su margen con desplazamiento incluido y sin cobrar es de 10€ por hora real trabajada. Si cobrara el desplazamiento (15€ adicionales, por ejemplo), su margen sería de 37,5€/hora. La diferencia es enorme.</p>

    <h2>Métodos para calcular el precio del desplazamiento</h2>
    <p>Hay tres enfoques principales, cada uno con sus ventajas:</p>
    <p><strong>Por kilómetro:</strong> se cobra una tarifa fija por cada km recorrido desde el punto de base. Es transparente y fácil de entender, pero requiere calcular la distancia exacta de cada cita, lo que puede ser tedioso si no está automatizado.</p>
    <p><strong>Por zonas:</strong> defines áreas geográficas con precio fijo. Es el método más claro para el cliente y el más fácil de gestionar. "Sin cargo en el centro, 10€ en zona media, 20€ en zona exterior" es un mensaje que el cliente entiende en segundos.</p>
    <p><strong>Precio fijo según tipo de servicio:</strong> algunos negocios incluyen el desplazamiento en el precio del servicio directamente, diferenciando entre "en local" y "a domicilio". Más simple, pero menos flexible si los clientes están muy dispersos geográficamente.</p>

    <h2>El método por zonas: el más claro y recomendado</h2>
    <p>Para la mayoría de negocios de servicios a domicilio, el método por zonas es el más práctico. Aquí un ejemplo real para una esteticista en Barcelona:</p>
    <table>
      <thead>
        <tr><th>Zona</th><th>Área</th><th>Cargo desplazamiento</th></tr>
      </thead>
      <tbody>
        <tr><td>Zona 1 (gratis)</td><td>0-4 km desde base</td><td>0€</td></tr>
        <tr><td>Zona 2</td><td>4-8 km desde base</td><td>+9€</td></tr>
        <tr><td>Zona 3</td><td>8-15 km desde base</td><td>+15€</td></tr>
        <tr><td>Zona 4</td><td>Más de 15 km</td><td>Consultar / +25€</td></tr>
      </tbody>
    </table>
    <p>El cliente ve el cargo de desplazamiento en el momento de la reserva, antes de confirmar. No hay sorpresas al llegar la factura.</p>

    <h2>Cómo comunicarlo al cliente sin generar fricción</h2>
    <p>La transparencia es la clave. Los clientes no suelen molestarse por el precio del desplazamiento si lo saben de antemano. Lo que genera conflictos es descubrirlo al final.</p>
    <p>El mejor momento para comunicarlo es la página de reserva: "Tu ubicación está en la Zona 2. Se añadirá un cargo de desplazamiento de 9€ al total." Si el cliente acepta y confirma, no hay disputa posible.</p>
    <p>También es importante indicarlo en los mensajes de confirmación y recordatorio. Así el cliente llega a la cita con las expectativas claras.</p>

    <h2>El impacto del tiempo de viaje en tu disponibilidad real</h2>
    <p>Más allá del precio, el desplazamiento afecta a cuántas citas puedes aceptar al día. Si no tienes en cuenta el tiempo de viaje en la disponibilidad de tu agenda, terminarás aceptando citas que físicamente no puedes cumplir a tiempo.</p>
    <p>Un sistema de gestión para domicilio debe bloquear automáticamente el tiempo de desplazamiento entre citas, de forma que el cliente que intenta reservar a las 11:00 vea que esa hora no está disponible si la cita anterior termina a las 10:45 en otro punto de la ciudad.</p>

    <h2>Configuración en Godolphy</h2>
    <p>El módulo de <a href="/funcionalidades/servicios-a-domicilio/">servicios a domicilio</a> de Godolphy permite configurar las zonas de precio con sus tarifas correspondientes. El sistema aplica el cargo automáticamente en el proceso de reserva según la ubicación del cliente, calcula el tiempo de desplazamiento y bloquea los huecos necesarios en la agenda. Para empresas de limpieza con equipos más grandes, la página de <a href="/sectores/software-para-empresas-de-limpieza/">software para empresas de limpieza</a> tiene información más específica.</p>
'''
)

# ─── ARTICLE 17 ────────────────────────────────────────────────────────────────
build(
    filename="2026-07-07-cuanto-gana-barberia-espana.html",
    title_tag="¿Cuánto gana una barbería en España? Ingresos reales 2026",
    desc="Analizamos los ingresos reales de una barbería en España: facturación media, márgenes, costes y qué factores marcan la diferencia.",
    canonical="https://godolphy.com/cuanto-gana-barberia-espana/",
    h1="¿Cuánto gana una barbería en España? Ingresos reales en 2026",
    date_iso="2026-07-07",
    date_human="7 de julio de 2026",
    schema_headline="¿Cuánto gana una barbería en España? Ingresos reales en 2026",
    content_html='''
    <p>La barbería ha vivido un renacimiento extraordinario en la última década. Lo que antes era un negocio en declive ha vuelto a ser un referente cultural con clientela fiel, ticket en alza y márgenes que superan a muchos otros negocios del sector belleza. Pero ¿cuánto gana realmente una barbería en España? En este artículo analizamos los números reales, sin maquillaje.</p>

    <h2>Facturación media de una barbería en España</h2>
    <p>La facturación de una barbería varía enormemente según la ubicación, el número de barberos y el posicionamiento. Estos son los rangos orientativos para barberias independientes en España en 2026:</p>
    <table>
      <thead>
        <tr><th>Tipo de barbería</th><th>Facturación mensual</th><th>Facturación anual</th></tr>
      </thead>
      <tbody>
        <tr><td>Barbero autónomo (solo)</td><td>3.000-5.000€</td><td>36.000-60.000€</td></tr>
        <tr><td>Barbería pequeña (2 barberos)</td><td>6.000-10.000€</td><td>72.000-120.000€</td></tr>
        <tr><td>Barbería mediana (3-4 barberos)</td><td>12.000-18.000€</td><td>144.000-216.000€</td></tr>
        <tr><td>Barbería premium (ubicación céntrica)</td><td>15.000-30.000€</td><td>180.000-360.000€</td></tr>
      </tbody>
    </table>
    <p>Estos números son la facturación bruta, antes de descontar los costes del negocio.</p>

    <h2>Ticket medio de una barbería</h2>
    <p>El ticket medio es el indicador que mejor refleja el posicionamiento de una barbería. Los rangos habituales:</p>
    <ul>
      <li><strong>Barbería básica / barrio:</strong> 10-18€ (corte básico sin extras)</li>
      <li><strong>Barbería estándar:</strong> 20-28€ (corte + arreglo de barba)</li>
      <li><strong>Barbería media-alta:</strong> 30-45€ (corte + barba + tratamiento)</li>
      <li><strong>Barbería premium:</strong> 45-70€ (experiencia completa con rituales)</li>
    </ul>
    <p>El salto de barbería básica a media-alta no siempre requiere una ubicación céntrica ni reformas costosas: principalmente depende del posicionamiento, el ambiente y la experiencia que ofreces.</p>

    <h2>Costes principales de una barbería</h2>
    <p>Para entender el margen real, hay que restar los costes:</p>
    <ul>
      <li><strong>Alquiler del local:</strong> 600-2.500€/mes según ciudad y zona</li>
      <li><strong>Nóminas / comisiones:</strong> 35-45% de la facturación en barberias con empleados</li>
      <li><strong>Productos y material:</strong> 5-10% de la facturación</li>
      <li><strong>Suministros (luz, agua, internet):</strong> 200-400€/mes</li>
      <li><strong>Software de gestión:</strong> 33-80€/mes</li>
      <li><strong>Seguros, gestoría y otros:</strong> 150-300€/mes</li>
    </ul>

    <h2>Margen neto real</h2>
    <p>Para un barbero autónomo que trabaja solo en local alquilado, los márgenes netos suelen estar entre el 35% y el 55% de la facturación. Para una barbería con empleados, el margen neto baja al 20-35% dependiendo de la eficiencia operativa.</p>
    <p>Una barbería de barrio con un barbero autónomo que factura 4.000€/mes puede tener entre 1.400€ y 2.200€ de margen neto mensual. Una barbería mediana con tres empleados que factura 15.000€/mes puede tener entre 3.000€ y 5.250€ de margen neto.</p>

    <h2>Qué diferencia a una barbería rentable de una que no lo es</h2>
    <p>La diferencia no suele estar en el precio de los servicios ni en el número de clientes. Está en tres indicadores:</p>
    <p><strong>Ocupación de agenda.</strong> Una barbería con el 80% de ocupación gana significativamente más que una con el 55% de ocupación al mismo precio. La clave es llenar los huecos: recordatorios automáticos, lista de espera y promociones en horas flojas.</p>
    <p><strong>Ticket medio.</strong> Una barbería que vende solo cortes tiene el ticket más bajo posible. La que también vende arreglo de barba, tratamientos de hidratación y rituales de afeitado clásico puede doblar el ticket sin doblar el tiempo de trabajo.</p>
    <p><strong>Retención de clientes.</strong> Un cliente habitual que viene cada tres semanas vale mucho más que uno que viene una vez. Los barberos que conocen a sus clientes, recuerdan sus preferencias y hacen seguimiento tienen tasas de retención mucho más altas.</p>

    <h2>Cómo mejorar la rentabilidad con software</h2>
    <p>Un software de gestión para barberias no es solo un calendario digital. Los datos que genera te permiten identificar exactamente dónde están tus oportunidades de mejora: qué días tienes la agenda más floja, qué servicios generan más margen, qué clientes llevan demasiado tiempo sin volver.</p>
    <p>En <a href="/sectores/software-para-barberias/">software para barberias</a> explicamos en detalle cómo Godolphy se adapta a las necesidades específicas del sector. Y en <a href="/funcionalidades/facturacion-y-reporte/">Facturación y reporte</a> puedes ver el tipo de análisis que el sistema genera automáticamente para tomar mejores decisiones.</p>
'''
)

# ─── ARTICLE 18 ────────────────────────────────────────────────────────────────
build(
    filename="2026-07-09-cuanto-cobra-gestor-peluqueria.html",
    title_tag="¿Cuánto cobra un gestor para una peluquería? Guía 2026",
    desc="Contratar una gestoría es una de las primeras decisiones de un autónomo en el sector belleza. Precios reales y qué incluye cada servicio.",
    canonical="https://godolphy.com/cuanto-cobra-gestor-peluqueria/",
    h1="¿Cuánto cobra un gestor o gestoría para una peluquería en 2026?",
    date_iso="2026-07-09",
    date_human="9 de julio de 2026",
    schema_headline="¿Cuánto cobra un gestor o gestoría para una peluquería en 2026?",
    content_html='''
    <p>Una de las primeras preguntas que se hace cualquier peluquera o barbero al darse de alta como autónomo es: ¿necesito una gestoría? La respuesta corta es sí, casi siempre. La respuesta más útil es: depende del servicio, del volumen de tu negocio y de si eliges una gestoría presencial o una online. En este artículo explicamos qué servicios suele incluir una gestoría para una peluquería y cuánto cuesta en España en 2026.</p>

    <h2>Por qué necesitas una gestoría como peluquera autónoma</h2>
    <p>Las obligaciones fiscales y laborales de un autónomo en España son más complejas de lo que parece. Presentar el modelo 130 cada trimestre, gestionar el IVA con el modelo 303, controlar las retenciones, preparar la declaración anual de IRPF y, si tienes empleados, gestionar las nóminas y los seguros sociales. Intentar hacerlo todo sin ayuda profesional es posible, pero el riesgo de errores con Hacienda o la Seguridad Social hace que el coste de la gestoría se amortice rápidamente.</p>

    <h2>Qué servicios suele incluir una gestoría básica para peluquerías</h2>
    <ul>
      <li>Alta en Hacienda (modelo 036/037) y en la Seguridad Social como autónomo</li>
      <li>Presentación trimestral del modelo 130 (IRPF) y modelo 303 (IVA)</li>
      <li>Resumen anual del IVA (modelo 390)</li>
      <li>Declaración anual de IRPF (modelo 100)</li>
      <li>Asesoramiento básico sobre gastos deducibles</li>
    </ul>
    <p>Si tienes empleados, se añaden la gestión de nóminas, los seguros sociales mensuales y las altas y bajas en la Seguridad Social.</p>

    <h2>Precios medios en España según perfil</h2>
    <table>
      <thead>
        <tr><th>Perfil</th><th>Precio mensual orientativo</th></tr>
      </thead>
      <tbody>
        <tr><td>Autónoma sin empleados, estimación directa simplificada</td><td>50-80€/mes</td></tr>
        <tr><td>Autónoma sin empleados, estimación directa normal</td><td>70-100€/mes</td></tr>
        <tr><td>Autónoma con 1-2 empleados</td><td>100-160€/mes</td></tr>
        <tr><td>Sociedad (SL) con empleados</td><td>150-250€/mes</td></tr>
      </tbody>
    </table>
    <p>Estos precios pueden variar según la comunidad autónoma (Madrid y Barcelona suelen ser un 20-30% más caro que la media), el volumen de facturas mensuales y si la gestoría es presencial u online.</p>

    <h2>Gestoría online vs presencial</h2>
    <p>La gestoría online ha crecido mucho en los últimos años y suele ser entre un 30% y un 50% más barata que la presencial. Sus principales ventajas son el precio y la comodidad (todo se gestiona por email, app o videollamada). Su desventaja principal es la falta de relación personal y la posibilidad de un servicio menos personalizado si el volumen de clientes del proveedor es muy alto.</p>
    <p>Para una peluquera autónoma sin empleados y con un negocio estable, una gestoría online de confianza puede ser más que suficiente. Para negocios más complejos (varios empleados, sociedad, múltiples servicios con diferentes tipos de IVA), la cercanía de una gestoría presencial puede aportar valor adicional.</p>

    <h2>Qué documentación necesita tu gestor</h2>
    <p>Para que tu gestor pueda trabajar, necesita acceso a tus facturas de ingresos y gastos. En la práctica, esto significa:</p>
    <ul>
      <li>Todas las facturas emitidas a clientes (si emites facturas) o el resumen de ingresos por período</li>
      <li>Todas las facturas de gastos del negocio: proveedor de productos, alquiler, software, material</li>
      <li>Extractos bancarios de la cuenta del negocio</li>
      <li>Cualquier contrato relevante (arrendamiento del local, contrato de empleados)</li>
    </ul>

    <h2>Cómo Godolphy facilita el trabajo con tu gestor</h2>
    <p>El módulo de <a href="/funcionalidades/facturacion-y-reporte/">Facturación y reporte</a> de Godolphy permite exportar los informes de ingresos en PDF y Excel con el nivel de detalle que tu gestor necesita: ingresos por período, desglose por tipo de servicio, facturas individuales si se emiten. También puedes conectar Godolphy con Holded a través de nuestra <a href="/integraciones/holded/">integración con Holded</a> para sincronizar automáticamente la contabilidad sin trabajo manual adicional.</p>
'''
)

# ─── ARTICLE 19 ────────────────────────────────────────────────────────────────
build(
    filename="2026-07-14-obligaciones-fiscales-centro-estetica.html",
    title_tag="Obligaciones fiscales de un centro de estética España 2026",
    desc="Qué impuestos tiene que pagar un centro de estética en España, cuándo presentar cada declaración y cómo evitar errores con Hacienda.",
    canonical="https://godolphy.com/obligaciones-fiscales-centro-estetica-espana/",
    h1="Obligaciones fiscales de un centro de estética en España en 2026",
    date_iso="2026-07-14",
    date_human="14 de julio de 2026",
    schema_headline="Obligaciones fiscales de un centro de estética en España en 2026",
    content_html='''
    <p class="disclaimer"><strong>Aviso:</strong> Este artículo es orientativo e informativo. No constituye asesoramiento fiscal. Consulta siempre con un gestor o asesor fiscal para tu situación concreta.</p>

    <p>Gestionar las obligaciones fiscales de un centro de estética no es complicado si sabes qué tienes que presentar, cuándo y cómo. El problema habitual es que muchas propietarias no conocen bien su calendario fiscal hasta que reciben una notificación de Hacienda. En este artículo explicamos los impuestos principales, las declaraciones trimestrales y anuales, y los errores más comunes a evitar.</p>

    <h2>El calendario fiscal del autónomo en el sector estética</h2>
    <p>Como autónoma con un centro de estética, tus obligaciones fiscales principales se concentran en cuatro fechas al año para las declaraciones trimestrales, más la declaración anual en primavera. El incumplimiento de cualquiera de estas fechas puede generar recargos y sanciones.</p>
    <p>Las fechas de presentación de declaraciones trimestrales son: del 1 al 20 de abril (primer trimestre), del 1 al 20 de julio (segundo trimestre), del 1 al 20 de octubre (tercer trimestre) y del 1 al 30 de enero del año siguiente (cuarto trimestre).</p>

    <h2>Impuestos principales: IRPF e IVA</h2>
    <p><strong>IRPF (Impuesto sobre la Renta de las Personas Físicas).</strong> Como autónoma en estimación directa, pagas el IRPF sobre el rendimiento neto de tu actividad (ingresos menos gastos deducibles). Cada trimestre presentas el modelo 130, que es un pago fraccionado a cuenta del IRPF anual. El importe es el 20% del rendimiento neto del trimestre, menos los pagos ya realizados en trimestres anteriores del mismo año.</p>
    <p><strong>IVA (Impuesto sobre el Valor Añadido).</strong> Los servicios de estética en España tributan al tipo general del 21%. Cada trimestre presentas el modelo 303, donde declaras el IVA cobrado a tus clientes (IVA repercutido) y el IVA pagado en tus compras y gastos (IVA soportado). La diferencia es lo que pagas o te devuelven.</p>

    <h2>Declaraciones trimestrales: modelo 130 y modelo 303</h2>
    <p>El <strong>modelo 130</strong> (pago fraccionado de IRPF) requiere tener registrados todos tus ingresos y gastos del trimestre. La base de cálculo es: ingresos del trimestre - gastos deducibles del trimestre = rendimiento neto. Sobre ese rendimiento aplicas el 20%.</p>
    <p>El <strong>modelo 303</strong> (autoliquidación de IVA) requiere los mismos datos pero separando el IVA: suma todo el IVA de tus facturas de ingresos (IVA repercutido) y todo el IVA de tus facturas de gastos deducibles (IVA soportado). Si el IVA repercutido es mayor, pagas la diferencia. Si el IVA soportado es mayor, puedes compensarlo en siguientes trimestres o pedir devolución.</p>

    <h2>Declaración anual</h2>
    <p>Entre abril y junio de cada año presentas el <strong>modelo 100</strong> (declaración de la renta). En él declaras todos los rendimientos del año: los de tu actividad económica más cualquier otro ingreso (alquileres, inversiones, etc.). Los pagos fraccionados del modelo 130 que has ido haciendo durante el año se descuentan de la cuota resultante. Si has pagado más de lo que corresponde, te devuelven la diferencia.</p>
    <p>En enero del año siguiente también presentas el <strong>modelo 390</strong>, que es el resumen anual del IVA, con los datos consolidados de los cuatro trimestres.</p>

    <h2>Gastos deducibles en un centro de estética</h2>
    <p>Reducir la base imponible con gastos deducibles es completamente legal y recomendable. Los gastos más habituales en un centro de estética que pueden deducirse incluyen:</p>
    <ul>
      <li>Alquiler del local (si es local de negocio)</li>
      <li>Suministros proporcionales al local (luz, agua, internet)</li>
      <li>Productos cosméticos y material de trabajo</li>
      <li>Software de gestión (como Godolphy)</li>
      <li>Formación profesional relacionada con la actividad</li>
      <li>Publicidad y marketing</li>
      <li>Cuota de autónomo</li>
      <li>Gestoría y asesoría fiscal</li>
      <li>Vehículo (parcialmente, si se usa para la actividad)</li>
    </ul>

    <h2>Errores más comunes con Hacienda</h2>
    <ul>
      <li><strong>No guardar todas las facturas:</strong> Hacienda puede pedir justificante de cualquier gasto deducido en los últimos 4 años. Sin factura, no se puede justificar.</li>
      <li><strong>Mezclar gastos personales y de negocio:</strong> la factura de la cena de familia no es gasto de negocio, aunque la pagues con la tarjeta del negocio.</li>
      <li><strong>No llevar registro de ingresos:</strong> si usas efectivo, debes registrar todos los cobros, no solo los pagos con tarjeta.</li>
      <li><strong>Olvidar pagos fraccionados:</strong> perder la fecha del modelo 130 genera un recargo del 5-20% más intereses de demora.</li>
    </ul>

    <h2>Cómo el software de gestión facilita la contabilidad</h2>
    <p>Tener todos los ingresos registrados automáticamente en Godolphy y poder exportarlos en el formato que necesita tu gestor elimina una parte importante del trabajo contable. El módulo de <a href="/funcionalidades/facturacion-y-reporte/">Facturación y reporte</a> genera resúmenes por período, desglosados por tipo de servicio y profesional, que tu gestor puede usar directamente para preparar las declaraciones. La <a href="/integraciones/holded/">integración con Holded</a> permite sincronizar la contabilidad automáticamente si tu gestor trabaja con esa plataforma.</p>
'''
)

# ─── ARTICLE 20 ────────────────────────────────────────────────────────────────
build(
    filename="2026-07-16-declaracion-renta-peluquera-autonoma.html",
    title_tag="Renta para peluqueras y esteticistas autónomas 2026",
    desc="Guía práctica para peluqueras y esteticistas autónomas: qué declarar, qué deducir y cómo evitar los errores más comunes en la declaración de la renta.",
    canonical="https://godolphy.com/declaracion-renta-peluquera-autonoma/",
    h1="Declaración de la renta para peluqueras y esteticistas autónomas 2026",
    date_iso="2026-07-16",
    date_human="16 de julio de 2026",
    schema_headline="Declaración de la renta para peluqueras y esteticistas autónomas 2026",
    content_html='''
    <p class="disclaimer"><strong>Aviso:</strong> Este artículo es orientativo e informativo. No constituye asesoramiento fiscal. Consulta siempre con un gestor o asesor fiscal para tu situación concreta.</p>

    <p>La declaración de la renta de una peluquera o esteticista autónoma no funciona igual que la de un trabajador por cuenta ajena. Tienes más obligaciones, más posibilidades de deducción y más margen para optimizar tu carga fiscal si conoces bien las reglas. En esta guía explicamos los conceptos básicos para que llegues a la campaña de la renta con todo claro.</p>

    <h2>Por qué la renta del autónomo es diferente</h2>
    <p>Un empleado por cuenta ajena recibe su nómina con el IRPF ya retenido. Su declaración de la renta es normalmente sencilla: confirmas los datos y ves si sale a devolver o a pagar (la diferencia suele ser pequeña).</p>
    <p>Una autónoma funciona de forma diferente: durante el año has ido pagando pagos fraccionados trimestrales a cuenta del IRPF (modelo 130). En la declaración anual haces el cómputo definitivo de todos tus ingresos y gastos del año y calculas la cuota real que corresponde. La diferencia entre lo que ya pagaste y lo que corresponde realmente es lo que devuelven (o cobran).</p>

    <h2>Qué rendimientos declarar</h2>
    <p>En tu declaración de la renta como autónoma del sector belleza tienes que incluir:</p>
    <ul>
      <li><strong>Rendimientos de actividades económicas:</strong> los ingresos netos de tu negocio (ingresos brutos menos gastos deducibles).</li>
      <li><strong>Retenciones practicadas:</strong> si algún cliente empresarial te ha practicado retención del 15% (poco habitual en peluquerías, más en servicios a empresas).</li>
      <li><strong>Rendimientos del capital:</strong> si tienes alquileres, dividendos o intereses bancarios relevantes.</li>
      <li><strong>Deducciones y mínimos personales:</strong> mínimo personal y familiar, deducción por vivienda habitual (si aplica), etc.</li>
    </ul>

    <h2>Gastos deducibles como autónoma del sector belleza</h2>
    <p>Este es el apartado donde hay más margen de optimización. Los gastos que puedes deducir reducen directamente tu base imponible y, por tanto, lo que pagas a Hacienda. Los más relevantes:</p>
    <ul>
      <li><strong>Local:</strong> alquiler del local de negocio (100% deducible). Si trabajas desde casa, solo la parte proporcional del espacio dedicado al negocio.</li>
      <li><strong>Materiales y productos:</strong> todo el material cosmétic, instrumental y de trabajo con factura.</li>
      <li><strong>Software de gestión:</strong> la suscripción a Godolphy u otro software de gestión es un gasto deducible como gasto de explotación.</li>
      <li><strong>Formación profesional:</strong> cursos, talleres y formación relacionada con tu actividad.</li>
      <li><strong>Publicidad:</strong> anuncios en redes sociales, fotografía profesional, diseño de logo, página web.</li>
      <li><strong>Gestoría:</strong> los honorarios de tu gestor son deducibles.</li>
      <li><strong>Cuota de autónomo:</strong> la cuota de la Seguridad Social que pagas como autónoma es deducible en el IRPF.</li>
      <li><strong>Vehículo (domicilio):</strong> si ofreces servicios a domicilio, el vehículo puede ser parcialmente deducible. Es un área con cierta complejidad — consulta con tu gestor.</li>
    </ul>

    <h2>Estimación directa vs módulos</h2>
    <p>Como autónoma en el sector belleza, puedes tributar por dos métodos:</p>
    <p><strong>Estimación directa simplificada:</strong> pagas impuestos sobre el rendimiento neto real (ingresos menos gastos). Es el método más preciso y el más conveniente para negocios que tienen gastos significativos que deducir. Requiere llevar un registro de ingresos y gastos.</p>
    <p><strong>Módulos (estimación objetiva):</strong> pagas una cuota fija determinada por parámetros como el número de empleados o el local, independientemente de lo que realmente ganes. Es más simple pero puede ser más caro si tu margen neto es bajo. Está disponible para algunas actividades del sector belleza, pero con límites de facturación.</p>
    <p>En general, la estimación directa es más conveniente para negocios con una facturación superior a 30.000-40.000€ anuales o con gastos deducibles significativos. Por debajo de esa cifra, los módulos pueden ser más simples. Tu gestor puede hacer el cálculo comparativo para tu caso concreto.</p>

    <h2>Errores más comunes en la renta de autónomas del sector belleza</h2>
    <ul>
      <li>No deducir la cuota de autónomo: es un error más frecuente de lo que parece.</li>
      <li>Olvidar incluir ingresos cobrados en efectivo: todos los ingresos, independientemente del método de pago, deben declararse.</li>
      <li>Deducir gastos personales como gastos de negocio: la ropa de trabajo genérica no es deducible, pero el uniforme específico sí.</li>
      <li>No aprovechar las deducciones por inicio de actividad: el primer año hay reducciones específicas para nuevos autónomos.</li>
      <li>No guardar facturas de gastos: sin factura, Hacienda puede rechazar la deducción en una revisión.</li>
    </ul>

    <h2>Cómo tener toda la documentación lista con Godolphy</h2>
    <p>El módulo de <a href="/funcionalidades/facturacion-y-reporte/">Facturación y reporte</a> de Godolphy te permite exportar un resumen completo de tus ingresos anuales desglosados por mes, por servicio y por profesional. Puedes generar el informe en PDF o Excel y entregárselo directamente a tu gestor. Si tu gestor trabaja con Holded, la <a href="/integraciones/holded/">integración con Holded</a> sincroniza los datos automáticamente, eliminando el trabajo de importación manual.</p>
    <p>Tener los datos ordenados al llegar a la campaña de la renta no solo ahorra tiempo: reduce el riesgo de errores y asegura que no te dejas ningún gasto deducible por el camino.</p>
'''
)

print("Articles 11-20 created.")
