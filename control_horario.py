import datetime
from program_rut import buscar_rut
from program_nombre import obtener_nombre
    

def hora_escanear():
    datos = {
    "Nombre": [],
    "RUT": []
    }

    while True:
        # Obten la fecha actual
        fecha_actual = datetime.date.today()
        # Obten la hora actual
        hora_actual = datetime.datetime.now().time()

        # Comprueba si la fecha actual es un lunes
        if fecha_actual.weekday() == 0:
            # Verifica si la hora es valida
            while(True):
                if datetime.time(9, 40) <= hora_actual <= datetime.time(10, 0) or datetime.time(11, 20) <= hora_actual <= datetime.time(11, 40) or datetime.time(14, 30) <= hora_actual <= datetime.time(14, 50) or datetime.time(19, 20) <= hora_actual <= datetime.time(19, 40):
                    #Obtener RUT
                    rut = buscar_rut()
                    if rut != None:
                        #Obtener Nombre
                        nombre = obtener_nombre(rut)

                        #Agrego los datos en un dataframe
                        datos["Nombre"].append(nombre)
                        datos["RUT"].append(rut)
                else:
                    return datos
            
        # Comprueba si la fecha actual es un martes
        elif fecha_actual.weekday() == 1:
            while(True):
                # Verifica si la hora es valida
                if datetime.time(8, 0) <= hora_actual <= datetime.time(8, 20) or datetime.time(9, 40) <= hora_actual <= datetime.time(10, 0) or datetime.time(11, 20) <= hora_actual <= datetime.time(11, 40) or datetime.time(14, 30) <= hora_actual <= datetime.time(14, 50) or datetime.time(16, 10) <= hora_actual <= datetime.time(16, 30):
                    #Obtener RUT
                    rut = buscar_rut()
                    if rut != None:
                        #Obtener Nombre
                        nombre = obtener_nombre(rut)

                        #Agrego los datos en un dataframe
                        datos["Nombre"].append(nombre)
                        datos["RUT"].append(rut)
                else:
                    return datos
            
        # Comprueba si la fecha actual es un miercoles
        elif fecha_actual.weekday() == 2:
            while(True):
                # Verifica si la hora es valida
                if datetime.time(8, 0) <= hora_actual <= datetime.time(8, 20) or datetime.time(9, 40) <= hora_actual <= datetime.time(10, 00) or datetime.time(11, 20) <= hora_actual <= datetime.time(11, 40) or datetime.time(16, 10) <= hora_actual <= datetime.time(16, 30):
                    #Obtener RUT
                    rut = buscar_rut()
                    if rut != None:
                        #Obtener Nombre
                        nombre = obtener_nombre(rut)

                        #Agrego los datos en un dataframe
                        datos["Nombre"].append(nombre)
                        datos["RUT"].append(rut)
                else:
                    return datos
            
        # Comprueba si la fecha actual es un jueves
        elif fecha_actual.weekday() == 3:
            while(True):
                # Verifica si la hora es valida
                if datetime.time(12, 50) <= hora_actual <= datetime.time(13, 20) or datetime.time(16, 10) <= hora_actual <= datetime.time(16, 30) or datetime.time(17, 50) <= hora_actual <= datetime.time(18, 10) or datetime.time(19, 20) <= hora_actual <= datetime.time(19, 40):
                    #Obtener RUT
                    rut = buscar_rut()
                    if rut != None:
                        #Obtener Nombre
                        nombre = obtener_nombre(rut)

                        #Agrego los datos en un dataframe
                        datos["Nombre"].append(nombre)
                        datos["RUT"].append(rut)
                else:
                    return datos
            
        # Comprueba si la fecha actual es un viernes
        elif fecha_actual.weekday() == 4:
            while(True):
                # Verifica si la hora es valida
                if datetime.time(9, 40) <= hora_actual <= datetime.time(10, 0) or datetime.time(11, 20) <= hora_actual <= datetime.time(11, 40) or datetime.time(12, 50) <= hora_actual <= datetime.time(13, 20) or datetime.time(16, 10) <= hora_actual <= datetime.time(16, 30) or datetime.time(19, 20) <= hora_actual <= datetime.time(19, 40):
                    #Obtener RUT
                    rut = buscar_rut()
                    if rut != None:
                        #Obtener Nombre
                        nombre = obtener_nombre(rut)

                        #Agrego los datos en un dataframe
                        datos["Nombre"].append(nombre)
                        datos["RUT"].append(rut)
                else:
                    return datos
        else:
            return datos



def buscar_nombre_tabla():
    # Obten la fecha actual
    fecha_actual = datetime.date.today()

    # Obten la hora actual
    hora_actual = datetime.datetime.now().time()

    # Comprueba si la fecha actual es un lunes
    if fecha_actual.weekday() == 0:
        # Verifica que hora es para poner el nombre de la asignatura
        if datetime.time(9, 40) <= hora_actual <= datetime.time(11, 10):
            nombre_tabla = "Taller_de_Mantenimiento"
        elif datetime.time(11, 20) <= hora_actual <= datetime.time(12, 50):
            nombre_tabla = "Interfaz_de_Usuario"
        elif datetime.time(14, 30) <= hora_actual <= datetime.time(16, 0):
            nombre_tabla = "Estructura_de_Datos"
        elif datetime.time(19, 20) <= hora_actual <= datetime.time(22, 20):
            nombre_tabla = "Base_de_Datos_(computacion_analisis)"
        else:
            return None
    
    # Comprueba si la fecha actual es un martes
    elif fecha_actual.weekday() == 1:
        # Verifica que hora es para poner el nombre de la asignatura
        if datetime.time(8, 0) <= hora_actual <= datetime.time(9, 30):
            nombre_tabla = "Programacion_I"
        elif datetime.time(9, 40) <= hora_actual <= datetime.time(11, 10):
            nombre_tabla = "Introduccion_SO"
        elif datetime.time(11, 20) <= hora_actual <= datetime.time(12, 50):
            nombre_tabla = "Estructura_de_Datos"
        elif datetime.time(14, 30) <= hora_actual <= datetime.time(16, 0):
            nombre_tabla = "Matematicas_Cs._Computacion"
        elif datetime.time(16, 10) <= hora_actual <= datetime.time(19, 20):
            nombre_tabla = "Base_de_Datos_II"
        else:
            return None

    # Comprueba si la fecha actual es un miercoles
    elif fecha_actual.weekday() == 2:
        # Verifica que hora es para poner el nombre de la asignatura
        if datetime.time(9, 40) <= hora_actual <= datetime.time(11, 10):
            nombre_tabla = "Programacion_I"
        elif datetime.time(11, 20) <= hora_actual <= datetime.time(12, 50):
            nombre_tabla = "Interfaz_de_Usuario"
        elif datetime.time(16, 10) <= hora_actual <= datetime.time(17, 40):
            nombre_tabla = "Introduccion_SO"
        else:
            return None

    # Comprueba si la fecha actual es un jueves
    elif fecha_actual.weekday() == 3:
        # Verifica que hora es para poner el nombre de la asignatura
        if datetime.time(12, 50) <= hora_actual <= datetime.time(14, 20):
            nombre_tabla = "Herramientas_de_Programacion"
        elif datetime.time(16, 10) <= hora_actual <= datetime.time(19, 20):
            nombre_tabla = "Base_de_Datos_II"
        elif datetime.time(19, 30) <= hora_actual <= datetime.time(23, 50):
            nombre_tabla = "Taller_de_integracion_de_sistemas"
        else:
            return None
    
    # Comprueba si la fecha actual es un viernes
    elif fecha_actual.weekday() == 4:
        # Verifica que hora es para poner el nombre de la asignatura
        if datetime.time(9, 40) <= hora_actual <= datetime.time(11, 10):
            nombre_tabla = "Estructura_de_Datos"
        elif datetime.time(11, 20) <= hora_actual <= datetime.time(12, 50):
            nombre_tabla = "Programacion_I"
        elif datetime.time(12, 50) <= hora_actual <= datetime.time(14, 20):
            nombre_tabla = "Herramientas_de_Programacion"
        elif datetime.time(16, 10) <= hora_actual <= datetime.time(17, 40):
            nombre_tabla = "Introduccion_SO"
        elif datetime.time(19, 20) <= hora_actual <= datetime.time(23, 50):
            nombre_tabla = "Taller_de_integracion_de_sistemas"
        else:
            return None

    else:
        return None

    nombre_tabla += "_"+str(fecha_actual)+".xlsx"
    return nombre_tabla