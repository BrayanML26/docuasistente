"""Genera las políticas ficticias de Brayan Lab (HTML) para el proyecto DocuAsistente."""

CSS = """<style>
@page{size:Letter;margin:0.9in}
body{font-family:Georgia,serif;font-size:11pt;line-height:1.45;color:#111}
h1{font-size:18pt;margin:0 0 4pt}
.meta{color:#555;font-size:9.5pt;margin-bottom:14pt;border-bottom:1px solid #999;padding-bottom:8pt}
h2{font-size:12.5pt;margin:16pt 0 4pt}
table{border-collapse:collapse;width:100%;margin:6pt 0}
td,th{border:1px solid #888;padding:4pt 6pt;font-size:10pt;text-align:left}
th{background:#eee}
</style>"""

DOCS = {
    "Politica_Vacaciones_BrayanLab": (
        "Política de Vacaciones y Permisos",
        "POL-RH-001 · Versión 2.1 · Vigente desde el 1 de enero de 2026 · Área responsable: Capital Humano",
        """
<h2>1. Objetivo</h2>
<p>Establecer las reglas para solicitar, aprobar y disfrutar las vacaciones y permisos de los colaboradores de Brayan Lab, asegurando la continuidad de las operaciones.</p>
<h2>2. Alcance</h2>
<p>Aplica a todos los colaboradores con contrato por tiempo indefinido. Los colaboradores en período de prueba (primeros 3 meses) no pueden disfrutar vacaciones, salvo autorización de la Dirección General.</p>
<h2>3. Días de vacaciones según antigüedad</h2>
<table><tr><th>Antigüedad</th><th>Días laborables por año</th></tr>
<tr><td>De 1 a 5 años</td><td>14 días</td></tr>
<tr><td>De 5 a 10 años</td><td>18 días</td></tr>
<tr><td>Más de 10 años</td><td>22 días</td></tr></table>
<p>Adicionalmente, cada colaborador recibe <b>1 día libre en la semana de su cumpleaños</b>, que debe tomarse dentro de esa misma semana y no es acumulable.</p>
<h2>4. Solicitud y aprobación</h2>
<p>Las vacaciones deben solicitarse por el portal de Capital Humano con al menos <b>15 días calendario de anticipación</b>. Solicitudes de 5 días o menos requieren aprobación del supervisor directo; solicitudes de más de 5 días requieren además la aprobación del Gerente del área. El supervisor tiene un plazo máximo de 3 días laborables para responder; si no responde, la solicitud se escala automáticamente al Gerente.</p>
<h2>5. Acumulación</h2>
<p>Se pueden acumular como máximo <b>5 días</b> de un año al siguiente. Los días acumulados deben disfrutarse antes del 31 de marzo del año siguiente; de lo contrario se pierden, salvo que la empresa haya negado las vacaciones por necesidad operativa.</p>
<h2>6. Períodos restringidos</h2>
<p>No se aprueban vacaciones durante la última semana de cada trimestre (cierre contable) ni del 15 al 31 de diciembre para el equipo de Soporte, excepto en casos de fuerza mayor.</p>
<h2>7. Permisos especiales remunerados</h2>
<table><tr><th>Motivo</th><th>Días</th></tr>
<tr><td>Matrimonio del colaborador</td><td>5 días</td></tr>
<tr><td>Nacimiento de hijo (padre)</td><td>2 días</td></tr>
<tr><td>Fallecimiento de familiar de primer grado</td><td>3 días</td></tr>
<tr><td>Mudanza</td><td>1 día por año</td></tr>
<tr><td>Exámenes universitarios</td><td>Hasta 4 medios días por semestre</td></tr></table>
<h2>8. Contacto</h2>
<p>Para dudas sobre esta política, escribir a capitalhumano@brayanlab.com.</p>
""",
    ),
    "Politica_Gastos_Viaje_BrayanLab": (
        "Política de Gastos de Viaje y Viáticos",
        "POL-FIN-004 · Versión 1.3 · Vigente desde el 15 de marzo de 2026 · Área responsable: Finanzas",
        """
<h2>1. Objetivo</h2>
<p>Definir los gastos de viaje que la empresa cubre, los límites diarios y el proceso de reembolso.</p>
<h2>2. Autorización previa</h2>
<p>Todo viaje debe ser aprobado por el Gerente del área antes de comprar boletos. Los viajes internacionales requieren también la aprobación del Director de Finanzas. Los boletos aéreos se compran con al menos <b>10 días de anticipación</b>, en clase económica. Vuelos de más de 8 horas pueden reservarse en clase económica premium.</p>
<h2>3. Viáticos diarios (alimentación y transporte local)</h2>
<table><tr><th>Destino</th><th>Límite diario</th></tr>
<tr><td>Dentro de República Dominicana (fuera de la ciudad de residencia)</td><td>RD$ 3,500</td></tr>
<tr><td>Centroamérica y el Caribe</td><td>USD 75</td></tr>
<tr><td>Estados Unidos y Canadá</td><td>USD 110</td></tr>
<tr><td>Europa</td><td>EUR 100</td></tr></table>
<h2>4. Hospedaje</h2>
<p>El límite de hospedaje por noche es de <b>USD 150</b> en Estados Unidos y Europa, y <b>USD 110</b> en el resto de destinos. Se prefieren los hoteles con convenio corporativo. Airbnb solo se permite para estadías de más de 7 noches.</p>
<h2>5. Gastos no reembolsables</h2>
<p>Bebidas alcohólicas, multas de tránsito, minibar, servicios de spa, mejoras de categoría de vuelo no autorizadas y gastos de acompañantes.</p>
<h2>6. Reembolso</h2>
<p>El colaborador debe enviar el reporte de gastos con todas las facturas (con RNC cuando el gasto sea en República Dominicana) en un plazo máximo de <b>5 días laborables</b> después de regresar. Finanzas reembolsa en un máximo de <b>10 días laborables</b> por transferencia. Gastos sin factura de hasta RD$ 500 (o USD 10) pueden reembolsarse con una declaración firmada, con un máximo de 3 por viaje.</p>
<h2>7. Anticipos</h2>
<p>Se puede solicitar un anticipo de hasta el <b>70%</b> de los viáticos estimados, con 5 días laborables de anticipación. El anticipo no utilizado se devuelve dentro de los 5 días laborables posteriores al regreso.</p>
<h2>8. Contacto</h2>
<p>finanzas@brayanlab.com</p>
""",
    ),
    "Politica_Trabajo_Remoto_BrayanLab": (
        "Política de Trabajo Remoto",
        "POL-RH-007 · Versión 1.0 · Vigente desde el 1 de junio de 2026 · Área responsable: Capital Humano y Tecnología",
        """
<h2>1. Modalidades</h2>
<p>Brayan Lab ofrece tres modalidades: <b>presencial</b>, <b>híbrida</b> (mínimo 2 días por semana en oficina: martes y jueves) y <b>remota</b> (solo para posiciones aprobadas por la Dirección General).</p>
<h2>2. Elegibilidad</h2>
<p>Para optar por la modalidad híbrida o remota se requiere haber completado el período de prueba de 3 meses y tener una evaluación de desempeño igual o superior a "Cumple expectativas".</p>
<h2>3. Horario y disponibilidad</h2>
<p>El horario núcleo es de <b>9:00 a.m. a 3:00 p.m. (hora de República Dominicana, UTC-4)</b>, durante el cual el colaborador debe estar disponible en Teams. Fuera del horario núcleo, se permite flexibilidad siempre que se cumplan 40 horas semanales.</p>
<h2>4. Equipo y conectividad</h2>
<p>La empresa entrega laptop, audífonos con micrófono y un monitor adicional. Se otorga un subsidio mensual de internet de <b>RD$ 1,500</b> para colaboradores en modalidad remota y de RD$ 800 para modalidad híbrida. El equipo es propiedad de la empresa y debe devolverse al terminar la relación laboral.</p>
<h2>5. Seguridad de la información</h2>
<p>Es obligatorio conectarse por VPN para acceder a sistemas internos, usar autenticación multifactor (MFA) y no trabajar desde redes Wi-Fi públicas sin VPN. Se prohíbe guardar información de clientes en dispositivos personales. Los incidentes de seguridad deben reportarse a seguridad@brayanlab.com en un plazo máximo de 2 horas.</p>
<h2>6. Trabajo desde otro país</h2>
<p>Se permite trabajar temporalmente desde otro país hasta <b>30 días por año</b>, con aprobación del Gerente y de Capital Humano, informando la ubicación con al menos 10 días de anticipación.</p>
<h2>7. Revocación</h2>
<p>La empresa puede revocar la modalidad remota o híbrida con un aviso de 15 días si no se cumplen los objetivos o las normas de esta política.</p>
""",
    ),
}

for fname, (title, meta, body) in DOCS.items():
    html = (
        f"<!doctype html><html lang='es'><head><meta charset='utf-8'><title>{title}</title>{CSS}</head>"
        f"<body><h1>{title}</h1><div class='meta'>Brayan Lab (empresa ficticia para pruebas) · {meta}</div>{body}</body></html>"
    )
    with open(f"{fname}.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("ok", fname)
