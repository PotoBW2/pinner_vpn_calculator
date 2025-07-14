from utils import result_ping, id_servidor, id_vpn, crear_vpn, crear_servidor
import keyboard
import time

servidor = "us-1"
vpn = "protonVPN-OpenVPN"

id_serv = id_servidor(servidor)
if not id_serv:
    print("No existe el servidor")
    id__vpn = id_vpn(vpn)
    if not id__vpn:
        print("No existe esa VPN")
        crear_vpn(vpn)
        print("VPN creada con exito")
        id__vpn = id_vpn(vpn)
    crear_servidor(servidor, id__vpn)
    print("Servidor creado con exito")
    id_serv = id_servidor(servidor)


def accion_repetitiva():
    print(result_ping("www.granma.cu"))
    time.sleep(1)


print("Prkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkku78888888888888888888888888b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b b sdeeeeeeeeeeeez ESPACIO para detener el programa...")

while True:
    accion_repetitiva()
    if keyboard.is_pressed('space'):
        print("\nPrograma detenido por el usuario")
        break
