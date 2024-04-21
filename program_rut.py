import re
from camara import leer_qr    

def buscar_rut():
    #obtener URL con el QR
    link = leer_qr()
    link = str(link)
    print(f"{link}")

    #Conprobar si se obtuvo el URL
    if link == None:
        return None
    else:
        # Utiliza una expresión regular para encontrar el texto entre "RUN=" y "&"
        match = re.search(r'RUN=(.*?)&', link)

        # Comprueba si se encontró una coincidencia
        if match:
            texto_extraido = match.group(1)
            return formatear_rut(texto_extraido)
        else:
            print("No se encontraron coincidencias")
            return None


def formatear_rut(rut):
    # Dividir el RUT en parte antes del dígito verificador y el dígito verificador
    rut_parte_numerica = rut[:-1]
    digito_verificador = rut[-1]

    # Formatear la parte numérica del RUT con puntos y agregar el dígito verificador
    rut_formateado = f"{rut_parte_numerica[:2]}.{rut_parte_numerica[2:5]}.{rut_parte_numerica[5:]}{digito_verificador}"

    return rut_formateado