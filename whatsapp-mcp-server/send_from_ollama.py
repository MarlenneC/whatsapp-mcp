import base64
import re
import mysql.connector
import os
import tempfile
from main import send_file

# === Configuración DB ===
mysql_config = {
    "host": "localhost",
    "user": "kreston_ti_chatbsg",
    "password": "Kreston2025$$",
    "database": "ChatBSG",
    "port": 3306
}

# === Paso 1: Conectar a la BD ===
conn = mysql.connector.connect(**mysql_config)
cursor = conn.cursor()

# === Paso 2: Buscar el último registro con base64 en el campo answer ===
query = """
 SELECT answer 
 FROM query_history 
 WHERE answer LIKE '%data:image/%;base64,%' 
 ORDER BY timestamp DESC 
 LIMIT 1
 """

cursor.execute(query)
row = cursor.fetchone()

if not row:
    print("❌ No se encontró ninguna imagen base64 en la tabla.")
else:
    answer_html = row[0]

    # === Paso 3: Extraer base64 con regex ===
    match = re.search(r'data:image/(\w+);base64,([A-Za-z0-9+/=]+)', answer_html)
    if match:
        image_type = match.group(1)  # ej. png, jpg
        image_base64 = match.group(2)

        # === Paso 4: Guardar imagen temporal ===
        temp_dir = tempfile.gettempdir()
        image_path = os.path.join(temp_dir, f"imagen_chatbsg.{image_type}")

        with open(image_path, "wb") as f:
            f.write(base64.b64decode(image_base64))

        print(f"✅ Imagen guardada en: {image_path}")

        # === Paso 5: Enviar por WhatsApp ===
        recipient = "5212228037800@s.whatsapp.net"
        # 5212227112807@s.whatsapp.net
        resultado = send_file(recipient, image_path)

        print("✅ Resultado del envío:")
        print(resultado)
    else:
        print("❌ No se encontró base64 válido en el campo answer.")

# === Cierre de conexión ===
cursor.close()
conn.close()
