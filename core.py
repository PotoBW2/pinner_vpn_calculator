from utils import result_ping, id_servidor, id_vpn, crear_vpn, crear_servidor, datos_vpn, datos_servidor, eliminar_ping
import keyboard
import time
import threading

print("***************************************************************************************************************")
print("* Lista de VPNs                                                                                               *")
print("***************************************************************************************************************")
datos = datos_vpn()
for dato in datos:
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
                "*** ERROR: NO HA INTRODUCIDO EL NÚMERO DEL VPN CORRECTAMENTE                                                ***")
            print(
                "***************************************************************************************************************")
    except:
        crear_vpn(selecion_vpn)
        vpn = id_vpn(selecion_vpn)
        bandera_vpn = False
print(" ")
print("***************************************************************************************************************")
print("* Lista de Servidores                                                                                         *")
print("***************************************************************************************************************")
datos = datos_servidor(vpn)
for dato in datos:
    texto = "* " + str(dato["id"]) + " - " + str(dato["nombre"])
    repeticiones = 110 - len(texto)
    while repeticiones > 0:
        texto = texto + " "
        repeticiones = repeticiones - 1
    texto = texto + "*"
    print(texto)
print("***************************************************************************************************************")
bandera_servidor = True
while bandera_servidor:
    selecion_servidor = input(
        " Seleccione un servidor o introduzca el nombre de un servidor para introducirlo en el sistema: ")
    try:
        number_servidor = int(selecion_servidor)
        if number_servidor in [id["id"] for id in datos]:
            servidor = number_servidor
            bandera_servidor = False
        else:
            print(
                "***************************************************************************************************************")
            print(
                "*** ERROR: NO HA INTRODUCIDO EL NÚMERO DEL SERVIDOR CORRECTAMENTE                                           ***")
            print(
                "***************************************************************************************************************")
    except:
        crear_servidor(selecion_servidor, vpn)
        servidor = id_servidor(selecion_servidor, vpn)
        bandera_servidor = False
print("***************************************************************************************************************")
print("* PINEANDO. PARA DETENER PRECIONE F12                                                                    *")
print("***************************************************************************************************************")
condicion_de_parada = True


def accion_repetitiva():
    while condicion_de_parada:
        result_ping("www.granma.cu", servidor)
        time.sleep(60)


hilo = threading.Thread(target=accion_repetitiva)
hilo.start()

while True:
    if keyboard.is_pressed('F12'):
        condicion_de_parada = False
        break
bandera = True
while bandera:
    resp = input("¿Desea mantener los ping obtenidos hoy para este servidor y esta VPN? (s/n): ")
    if resp in ["n", "no", 0, False, None, "N", "No", "nO", "NO"]:
        eliminar_ping()
        print(
            "***************************************************************************************************************")
        print(
            "*** Pings obtenidos hoy eliminados satisfactoriamente                                                       ***")
        print(
            "***************************************************************************************************************")
        bandera = False
        time.sleep(60)
    elif resp in ["s", "si", 1, True, "Si", "SI", "sI", "sí", "S", "Sí", "SÍ", "sÍ", "y", "Y", "Yes", "yes"]:
        bandera = False
    else:
        print(
            "***************************************************************************************************************")
        print(
            "*** ERROR: DEBE RESPONDER CORRECTAMENTE LA PREGUNTA (s/n).                                                  ***")
        print(
            "***************************************************************************************************************")


