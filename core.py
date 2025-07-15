from utils import result_ping, id_servidor, id_vpn, crear_vpn, crear_servidor, datos_vpn
import keyboard
import time
import threading

print("***************************************************************************************************************")
print("* Lista de VPNs                                                                                               *")
print("***************************************************************************************************************")
datos = datos_vpn()
for dato in datos_vpn():
    texto = "* " + str(dato["id"]) + " - " + str(dato["nombre"])
    repeticiones = 110 - len(texto)
    while repeticiones > 0:
        texto = texto + " "
        repeticiones = repeticiones - 1
    texto = texto + "*"
    print(texto)
print("***************************************************************************************************************")
bandera_vpn = True
while bandera_vpn:
    selecion_vpn = input(" Seleccione la VPN o introduzca el nombre de la VPN para introducirla en el sistema: ")
    try:
        number_vpn = int(selecion_vpn)
        if number_vpn in [id["id"] for id in datos]:
            vpn = number_vpn
            bandera_vpn = False
        else:
            print(
                "***************************************************************************************************************")
            print(
                "*** ERROR: NO HA INTRODUCIDO EL NÚMERO DEL SERVIDOR CORRECTAMENTE                                           ***")
            print(
                "***************************************************************************************************************")
    except:
        crear_vpn(selecion_vpn)
        vpn = id_vpn(selecion_vpn)
        bandera_vpn = False
print("El id es: " + str(vpn))
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

# condicion_de_parada = True
# def accion_repetitiva():
#     while condicion_de_parada:
#         result_ping("www.granma.cu")
#         time.sleep(1)
# hilo = threading.Thread(target=accion_repetitiva)
# hilo.start()
#
# print("ESPACIO para detener el programa...")
#
# while True:
#     if keyboard.is_pressed('space'):
#         condicion_de_parada = False
#         print("\nPrograma detenido por el usuario")
#         break
