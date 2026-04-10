import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config import (
    CORREO_REMITENTE,
    PASSWORD_CORREO,
    SMTP_SERVER,
    SMTP_PORT,
    ASUNTO_CORREO
)

def conectar_servidor():

    print("Conectando al servidor SMTP...")

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=10)

    # Mostrar comunicación con el servidor (para depurar)
    server.set_debuglevel(1)

    # Identificación con el servidor
    server.ehlo()

    print("Iniciando conexión segura TLS...")
    server.starttls()

    # Volver a identificarse después del TLS
    server.ehlo()

    print("Iniciando sesión...")
    server.login(CORREO_REMITENTE, PASSWORD_CORREO)

    print("Conexión establecida")

    return server


def enviar_correo(server, usuario):

    nombre = usuario["Nombre"]
    correo = usuario["email"]
    password = usuario["password"]

    mensaje = f"""
    
Hola {nombre},
Tus credenciales para el Sistema RAV y acompañamiento en nuestro proceso de evolución
Estimado/a [Nombre del Líder],
En nuestro firme propósito de seguir transformando y fortaleciendo nuestra organización, nos complace informarte que ya está habilitada la plataforma para el diligenciamiento del Sistema RAV.
El registro y actualización de información en este sistema va mucho más allá de un trámite administrativo; es un ejercicio indispensable para la evolución de nuestra empresa. Los datos y resultados que obtendremos a través del RAV son la brújula que nos permitirá tomar decisiones estratégicas más acertadas, identificar oportunidades de mejora y asegurar que todos nuestros equipos estén alineados hacia los mismos objetivos. Tu compromiso como líder en esta etapa es el motor que impulsa este cambio.
Para comenzar, a continuación te compartimos tus credenciales únicas de acceso:

Usuario: [Insertar Usuario]
Contraseña: [Insertar Contraseña]
 
Tu red de apoyo: Líderes Habilitadores de Talento Humano
 
Gerencia/Dir/Jefatura	Embajador
Contraloría	Jesica Agudelo
Financiera	Jesica Agudelo
TI	Johana Morales
Auditoria Interna	Johana Morales
TH	Santiago Osorio
CAB	Santiago Osorio
IA	Santiago Osorio
Jurídica	Edwin Alzate
Clientes	Johana Morales
Ger. General	 
Agradecemos profundamente tu liderazgo, tiempo y dedicación en este proceso. Si presentas algún inconveniente técnico con tu acceso, no dudes en contactar directamente a tu embajador.
Sigamos construyendo juntos el futuro de nuestra organización.
Recuerda que la fecha límite es para el lunes 13 de Abril del 2026

Estas son tus credenciales de acceso:

Usuario: {correo}
Contraseña: {password}

Por favor cambia tu contraseña después de ingresar.
"""

    msg = MIMEMultipart()

    msg["From"] = CORREO_REMITENTE
    msg["To"] = correo
    msg["Subject"] = ASUNTO_CORREO

    msg.attach(MIMEText(mensaje, "plain"))

    print(f"Enviando correo a {correo}...")

    server.sendmail(CORREO_REMITENTE, correo, msg.as_string())

    print("Correo enviado correctamente")