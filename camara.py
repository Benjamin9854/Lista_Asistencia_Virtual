import cv2
from qreader import QReader
import numpy as np 
import time   


def leer_qr():
    cap = cv2.VideoCapture(1)  # Abre la cámara externa (cambia el índice si tienes varias cámaras)
    qreader = QReader()
    start_time = time.time()  # Obtiene el tiempo de inicio

    while(cap.isOpened()):
        ret, frame = cap.read()

        if cv2.waitKey(1) == ord('q') or (time.time() - start_time) > 60: #se rompe el ciclo al presionar la letra q o al pasar 1 minuto
            break
        
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        decode_text = qreader.detect_and_decode(image)

        if len(decode_text) > 0:
            if decode_text != (None,):
                print(f'Dato: {decode_text}')
                cv2.imshow('webCam', frame)
                break
            else:
                print("mala lectura")
                cv2.imshow('webCam', frame)
        else:
            print("sin codigo")
            cv2.imshow('webCam', frame)

    cap.release()
    cv2.destroyAllWindows()

    # Verificar si se superó el tiempo de espera
    if (time.time() - start_time) > 60:
        print("Tiempo de espera superado")
        return None

    return decode_text