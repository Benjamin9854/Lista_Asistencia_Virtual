import pandas as pd
import gspread
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from gspread.exceptions import APIError

def crear_lista(datos, nombre_archivo_excel):
    df = pd.DataFrame(datos)

    # Guardar el DataFrame en un archivo de Excel
    df.to_excel(nombre_archivo_excel, index=False)

    # Autenticación de Google Drive utilizando google-auth
    creds = service_account.Credentials.from_service_account_file("credenciales.json", scopes=["https://www.googleapis.com/auth/drive"])

    # Crear un cliente de gspread
    cliente = gspread.Client(auth=creds)

    # Subir el archivo Excel a Google Drive
    drive_service = build('drive', 'v3', credentials=creds)
    file_metadata = {
        'name': nombre_archivo_excel,
        'parents': ['1fEhgAeYwfYQs3gkgJQiZvK0nE1XivqUL']  #El ID de la carpeta de Google Drive deseada
    }
    media = MediaFileUpload(nombre_archivo_excel, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    uploaded_file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()

    # # Abrir la hoja de cálculo de Google Drive utilizando gspread
    # try:
    #     sheet = cliente.open_by_key(uploaded_file['id'])
    #     print(f"El archivo {nombre_archivo_excel} se ha guardado en Google Drive y se ha convertido en una hoja de cálculo de Google Sheets.")
    # except APIError as e:
    #     print(f"Error al abrir la hoja de cálculo en Google Sheets: {e}") 
