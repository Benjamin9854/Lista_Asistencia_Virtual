import subprocess
import os
import sqlite3

def ejecutar_programa1(rut):
    comando = ["python3", "nombre_rut_firma.py", "--ruts", rut]
    resultado = subprocess.check_output(comando, universal_newlines=True)
    return resultado.strip()


def obtener_nombre(rut_a_procesar: str):
    # Ejecutar el primer programa y capturar el resultado
    ejecutar_programa1(rut_a_procesar)
    return obtener_nombre_por_rut(rut_a_procesar)


def consulta_database(rut):
    # Conectar a la base de datos
    conexion = sqlite3.connect('ruts.db')
    cursor = conexion.cursor()

    # Consulta SQL para obtener el nombre por el RUT
    consulta = "SELECT nombre FROM ruts WHERE rut = ?"
    cursor.execute(consulta, (rut,))

    # Obtener el resultado
    resultado = cursor.fetchone()

    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()

    # Si se encontró un resultado, devolver el nombre, de lo contrario, devolver None
    return resultado[0] if resultado else None


def obtener_nombre_por_rut(rut_buscado: str):
    # Uso de la función para obtener el nombre para un RUT específico
    nombre_obtenido = consulta_database(rut_buscado)

    # Bloque try...finally para asegurarse de cerrar la conexión y borrar la base de datos
    try:
        # Conectar a la base de datos
        conexion = sqlite3.connect('ruts.db')
        cursor = conexion.cursor()

        # Borrar la base de datos
        cursor.execute("DROP TABLE IF EXISTS ruts")

        # Confirmar la operación y cerrar la conexión
        conexion.commit()
    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
        conexion.close()

    # Eliminar el archivo de la base de datos
    os.remove('ruts.db')

    if nombre_obtenido is not None:
        return nombre_obtenido
    else:
        return None
