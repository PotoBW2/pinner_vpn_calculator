from ping3 import ping
import sqlite3

conexion = None


def result_ping(url):
    result = ping(url)
    if result:
        return round(result * 1000)
    else:
        return False


def open_connection():
    conexion = sqlite3.connect('databd.db')
    return conexion.cursor(), conexion


def id_servidor(servidor_nombre):
    cursor, conn = open_connection()
    cursor.execute("SELECT id FROM servidor WHERE nombre = '" + servidor_nombre + "'")
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
