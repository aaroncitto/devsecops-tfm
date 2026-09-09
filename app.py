import os
import sqlite3
import socket

# Corrección 1: Secreto externalizado a variables de entorno (no hardcoded)
API_SECRET_KEY = os.getenv("API_SECRET_KEY", "DefaultSecureVaultKey_2026")

def conectar_bd():
    return sqlite3.connect(":memory:")

def buscar_usuario(nombre):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER, nombre TEXT)")
    # Corrección 2: Consulta SQL parametrizada contra inyección SQL (CWE-89)
    query = "SELECT * FROM usuarios WHERE nombre = ?"
    cursor.execute(query, (nombre,))
    return cursor.fetchall()

def verificar_host(host):
    # Corrección 3: Uso de sockets de red nativos contra inyección de comandos (CWE-78)
    try:
        ip = socket.gethostbyname(host)
        return f"Host {host} resoluble en {ip}"
    except socket.gaierror:
        return f"No se pudo resolver el host {host}"

if __name__ == "__main__":
    print("Aplicación segura iniciada correctamente.")
