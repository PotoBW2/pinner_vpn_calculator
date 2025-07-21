import time as timein
from ping3 import ping
import sqlite3
from datetime import date, time, timedelta, datetime
import os
import platform

conexion = None


def result_ping(url, servidor):
    hora = timein.strftime("%H:%M")
    fecha = date.today()
    bandera = existe_ping(servidor, hora)
    if bandera:
        id_viejo, ping_viejo = obtener_id_ping(servidor, hora)
        result = ping(url)
        if result:
            if result < ping_viejo:
                eliminar_ping_por_id(id_viejo)
                crear_ping(servidor, round(result * 1000), hora, fecha)
    else:
        result = ping(url)
        if result:
            crear_ping(servidor, round(result * 1000), hora, fecha)


def open_connection():
    conexion = sqlite3.connect('databd.db')
    return conexion.cursor(), conexion


def id_servidor(servidor_nombre, vpn):
    cursor, conn = open_connection()
    cursor.execute("SELECT id FROM servidor WHERE nombre = '" + servidor_nombre + "' AND vpn = " + str(vpn))
    registros = cursor.fetchall()
    if len(registros) > 0:
        for registro in registros:
            return registro[0]
    else:
        return None
    conn.close()


def id_vpn(vpn_nombre):
    cursor, conn = open_connection()
    cursor.execute("SELECT id FROM vpn WHERE nombre = '" + vpn_nombre + "'")
    registros = cursor.fetchall()
    if len(registros) > 0:
        for registro in registros:
            return registro[0]
    else:
        return None
    conn.close()


def crear_vpn(vpn_nombre):
    cursor, conn = open_connection()
    cursor.execute("INSERT INTO vpn (nombre) VALUES ('" + vpn_nombre + "')")
    conn.commit()
    conn.close()


def crear_servidor(nombre, vpn):
    cursor, conn = open_connection()
    cursor.execute("INSERT INTO servidor (nombre, vpn) VALUES ('" + nombre + "', " + str(vpn) + ")")
    conn.commit()
    conn.close()


def datos_vpn():
    cursor, conn = open_connection()
    cursor.execute("SELECT id,nombre FROM vpn")
    registros = cursor.fetchall()
    resp = []
    for registro in registros:
        resp.append({"id": registro[0], "nombre": registro[1]})
    return resp
    conn.close()


def datos_servidor(vpn):
    cursor, conn = open_connection()
    cursor.execute("SELECT id,nombre FROM servidor WHERE vpn =" + str(vpn))
    registros = cursor.fetchall()
    resp = []
    for registro in registros:
        resp.append({"id": registro[0], "nombre": registro[1]})
    return resp
    conn.close()


def crear_ping(servidor, ping, hora, fecha):
    cursor, conn = open_connection()
    cursor.execute("INSERT INTO ping (servidor, ping, hora, fecha) VALUES (" + str(servidor) + ", " + str(
        ping) + ",'" + str(hora) + "','" + str(fecha) + "')")
    conn.commit()
    conn.close()


def existe_ping(servidor, hora):
    cursor, conn = open_connection()
    cursor.execute("SELECT id FROM ping WHERE servidor =" + str(servidor) + " AND hora = '" + str(hora) + "'")
    registros = cursor.fetchall()
    if len(registros) > 0:
        return True
    else:
        return False
    conn.close()


def eliminar_ping_por_fecha(servidor):
    fecha = date.today()
    cursor, conn = open_connection()
    cursor.execute("DELETE FROM ping WHERE fecha = '" + str(fecha) + "'")
    conn.commit()
    conn.close()


def min_to_number(min):
    return round(min / 60, 2)


def datos_grafica(servidor):
    x = []
    y = []
    hora = time(hour=0, minute=0)
    fecha_hora = datetime.combine(datetime.today(), hora)
    bandera = fecha_hora + timedelta(days=1)
    cursor, conn = open_connection()
    while fecha_hora < bandera:
        cursor.execute("SELECT ping FROM ping WHERE servidor =" + str(servidor) + " AND hora='" + str(
            hora.strftime("%H:%M")) + "'")
        registros = cursor.fetchall()
        if len(registros) > 0:
            for registro in registros:

                y.append(registro[0])
        else:
            y.append(None)
        x.append(hora.hour + min_to_number(hora.minute))
        fecha_hora = fecha_hora + timedelta(minutes=1)
        hora = fecha_hora.time()
    conn.close()
    return x, y


def nombre_servidor(id, vpn):
    cursor, conn = open_connection()
    cursor.execute("SELECT nombre FROM servidor WHERE id = '" + str(id) + "' AND vpn = '" + str(vpn) + "'")
    registros = cursor.fetchall()
    for registro in registros:
        return registro[0]
    conn.close()


def nombre_vpn(id):
    cursor, conn = open_connection()
    cursor.execute("SELECT nombre FROM vpn WHERE id = '" + str(id) + "'")
    registros = cursor.fetchall()
    for registro in registros:
        return registro[0]
    conn.close()


def obtener_id_ping(servidor, hora):
    cursor, conn = open_connection()
    cursor.execute(
        "SELECT id,ping FROM ping WHERE servidor =" + str(servidor) + " AND hora='" + hora + "'")
    registros = cursor.fetchall()
    for registro in registros:
        return registro[0], registro[1]


def eliminar_ping_por_id(id):
    cursor, conn = open_connection()
    cursor.execute("DELETE FROM ping WHERE id = " + str(id))
    conn.commit()
    conn.close()
