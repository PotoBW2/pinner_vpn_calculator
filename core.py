from utils import result_ping, id_servidor, id_vpn, crear_vpn, crear_servidor, datos_vpn, datos_servidor, \
    eliminar_ping_por_fecha, \
    datos_grafica, nombre_vpn, nombre_servidor
import keyboard
import time
import threading
import matplotlib.pyplot as plt

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
print(" ")
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
print("  ")
print("  ")
print("  ")
print("***************************************************************************************************************")
print("* PINEANDO. PARA DETENER PRECIONE F12                                                                         *")
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
    print(" ")
    print(" ")
    print(" ")
    resp = input("¿Desea mantener los ping obtenidos hoy para este servidor y esta VPN? (s/n): ")
    if resp in ["n", "no", 0, False, None, "N", "No", "nO", "NO"]:
        eliminar_ping_por_fecha()
        print(
            "***************************************************************************************************************")
        print(
            "*** Pings obtenidos hoy eliminados satisfactoriamente                                                       ***")
        print(
            "***************************************************************************************************************")
        bandera = False
    elif resp in ["s", "si", 1, True, "Si", "SI", "sI", "sí", "S", "Sí", "SÍ", "sÍ", "y", "Y", "Yes", "yes"]:
        bandera = False
    else:
        print(
            "***************************************************************************************************************")
        print(
            "*** ERROR: DEBE RESPONDER CORRECTAMENTE LA PREGUNTA (s/n).                                                  ***")
        print(
            "***************************************************************************************************************")
        print(" ")
        print(" ")
        print(" ")

nom_vpn = nombre_vpn(vpn)
nom_servidor = nombre_servidor(servidor, vpn)
bandera = True
while bandera:
    resp = input('¿Desea exportar la grafica del Servidor "' + nom_servidor + '" del VPN "' + nom_vpn + '"? (s/n): ')
    if resp in ["n", "no", 0, False, None, "N", "No", "nO", "NO"]:
        print(" ")
        print(" ")
        print(" ")
        print(
            "***************************************************************************************************************")
        print(
            "*** Gracias por usar nuestro software                                    By PotoBW                          ***")
        print(
            "***************************************************************************************************************")
        bandera = False
    elif resp in ["s", "si", 1, True, "Si", "SI", "sI", "sí", "S", "Sí", "SÍ", "sÍ", "y", "Y", "Yes", "yes"]:
        bandera = False
        x, y = datos_grafica(6)
        plt.figure(figsize=(8, 6))
        plt.plot(x, y,
                 marker='None',
                 linestyle='-',
                 color='blue',
                 label='Ping')
        # plt.xlim(0, 24)
        plt.xticks([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24],
                   ['0:00', '2:00', '4:00', '6:00', '8:00', '10:00', '12:00', '14:00', '16:00', '18:00', '20:00',
                    '22:00', '24:00'])
        plt.title('Pings del Servidor "' + nom_servidor + '" del VPN "' + nom_vpn + '"', fontsize=14)
        plt.xlabel("Horario", fontsize=12)
        plt.ylabel("Milisegundos", fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        plt.savefig(nom_servidor + '_' + nom_vpn + '.png', dpi=300, bbox_inches='tight')
        plt.show()
        print(" ")
        print(" ")
        print(" ")
        print(
            "***************************************************************************************************************")
        print(
            "*** Grafica exportada satisfactoriamente. Gracias por usar nuestro software              By PotoBW          ***")
        print(
            "***************************************************************************************************************")
        time.sleep(60)
    else:
        print(
            "***************************************************************************************************************")
        print(
            "*** ERROR: DEBE RESPONDER CORRECTAMENTE LA PREGUNTA (s/n).                                                  ***")
        print(
            "***************************************************************************************************************")
