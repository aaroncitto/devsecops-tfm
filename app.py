import os
import sqlite3

API_SECRET_KEY = "SUPER_SECRET_KEY_12345"

def ejecutar_ping(host):
    os.system("ping -c 1 " + host)

def buscar_usuario(nombre):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    query = "SELECT * FROM usuarios WHERE nombre = '" + nombre + "'"
    cursor.execute(query)
    return cursor.fetchall()
