from lista_asistencia_2 import crear_lista
from control_horario import buscar_nombre_tabla, hora_escanear
import os

while True:
    #se pone a escanear codigos durante el horario pertinente
    datos = hora_escanear()
    #Si NO hay alumnos escaneados no se crea la lista
    if not datos:
        pass
    #Si hay alumnos escaneados se crea la lista
    else:
        nombre_tabla = buscar_nombre_tabla()
        if nombre_tabla != None:
            crear_lista(datos, nombre_tabla)
            # Eliminar el archivo después de haberlo utilizado
            os.remove(nombre_tabla)
        datos = None

