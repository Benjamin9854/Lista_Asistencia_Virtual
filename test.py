from lista_asistencia_2 import crear_lista
from program_rut import buscar_rut
from program_nombre import obtener_nombre
import time 
import os

start_time = time.time()  # Obtiene el tiempo de inicio
while True:
    tiempo = True
    datos = {
    "Nombre": [],
    "RUT": []
    }

    if (time.time() - start_time) > 20: #se rompe el ciclo al pasar 1 minuto
        print("paso 20 segundos")
        tiempo = False
        break

    rut = buscar_rut()
    if rut != None:
        #Obtener Nombre
        nombre = obtener_nombre(rut)

        #Agrego los datos en un dataframe
        datos["Nombre"].append(nombre)
        datos["RUT"].append(rut)
        break
    
if tiempo:
    nombre_tabla = "prueba_2023-12-14.xlsx"
    crear_lista(datos, nombre_tabla)

    # Eliminar el archivo después de haberlo utilizado
    os.remove(nombre_tabla)