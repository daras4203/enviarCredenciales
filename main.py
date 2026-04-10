import time

from leerExcel import cargar_usuarios
from correo import conectar_servidor, enviar_correo

def main():

    print("Cargando usuarios...")
    usuarios = cargar_usuarios()

    print(f"Se encontraron {len(usuarios)} usuarios\n")

    print("Conectando al servidor de correo...")
    server = conectar_servidor()

    enviados = 0

    for usuario in usuarios:

        try:

            enviar_correo(server, usuario)

            enviados += 1

            print(f"[{enviados}/{len(usuarios)}] Correo enviado a {usuario['correo']}")

        except Exception as e:

            print(f"Error enviando a {usuario['correo']} → {e}")

        time.sleep(1)

    server.quit()

    print("\nProceso finalizado")


if __name__ == "__main__":
    main()