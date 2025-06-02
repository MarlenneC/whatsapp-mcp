import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import os
import uuid
import tempfile
from bs4 import BeautifulSoup
import imgkit
from main import send_file  # Asegúrate de que esta función esté bien definida

# 1. Conectarse a la base de datos y obtener el HTML con <table>
def obtener_html_tabla():
    conn = mysql.connector.connect(
        host="localhost",
        user="kreston_ti_chatbsg",
        password="Kreston2025$$",
        database="ChatBSG",
        port=3306
    )
    cursor = conn.cursor()
    cursor.execute("SELECT answer FROM query_history WHERE answer LIKE '%<table%' ORDER BY id DESC LIMIT 1;")
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def guardar_html_como_imagen(html, nombre_archivo="tabla_estilizada.png"):
    output_dir = "temp_images"
    os.makedirs(output_dir, exist_ok=True)
    ruta_salida = os.path.join(output_dir, f"{uuid.uuid4()}_{nombre_archivo}")
    ruta_salida_abs = os.path.abspath(ruta_salida)

    opciones = {
        'format': 'png',
        'encoding': "UTF-8"
    }

    imgkit.from_string(html, ruta_salida_abs, options=opciones)
    return ruta_salida_abs

html_tabla = obtener_html_tabla()

if html_tabla:
    imagen = guardar_html_como_imagen(html_tabla)

    if os.path.exists(imagen):
        resultado = send_file("5212228037800@s.whatsapp.net", imagen)
        #resultado = send_file("5212225585997@s.whatsapp.net", imagen)
        
        print("Resultado del envío:")
        print(resultado)
    else:
        print("❌ El archivo de imagen no se generó correctamente:", imagen)
else:
    print("❌ No se encontró ninguna tabla HTML en la base de datos.")

"""if html_tabla:
    imagen = guardar_html_como_imagen(html_tabla)
    resultado = send_file("5212228037800@s.whatsapp.net", imagen)
    print("Resultado del envío:")
    print(resultado)
else:
    print("❌ No se encontró ninguna tabla HTML en la base de datos.")"""