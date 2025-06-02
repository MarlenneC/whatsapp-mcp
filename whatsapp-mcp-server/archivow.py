from main import send_file
import requests
import mimetypes
import os
from typing import Dict, Any


WHATSAPP_API_BASE_URL = "http://localhost:8080/api" # Ajusta si es necesario

def send_file(recipient: str, media_path: str) -> Dict[str, Any]:
    try:
        if not recipient:
            return {"success": False, "message": "Recipient must be provided"}
 
        if not media_path or not os.path.isfile(media_path):
            return {"success": False, "message": f"Media file not found: {media_path}"}
 
        # Detectar tipo MIME
        mime_type, _ = mimetypes.guess_type(media_path)
        mime_type = mime_type or "application/octet-stream"
 
        # Cargar archivo con tipo MIME correcto
        with open(media_path, 'rb') as file_data:
            files = {
                'file': (os.path.basename(media_path), file_data, mime_type)
            }
            data = {
                'recipient': recipient
            }
        
        url = f"{WHATSAPP_API_BASE_URL}/send"
        data = {
            "recipient": recipient,
            "media_path": archivo,
        }
        response = requests.post(url, json=data)

        if response.status_code == 200:
            result = response.json()
            return {"success": result.get("success", False), "message": result.get("message", "No message")}
        else:
            return {"success": False, "message": f"HTTP {response.status_code}: {response.text}"}
 
    except requests.RequestException as e:
        return {"success": False, "message": f"Request error: {e}"}

recipient = "5212228037800@s.whatsapp.net"
archivo = r"C:\Proyectos-Marlenne\WhatsApp-server\whatsapp-mcp\whatsapp-mcp-server\GuiadeProveedor_CargaFacturas (1).pdf"

nombre_archivo = os.path.basename(archivo)

if os.path.isfile(archivo):
    print("📄 Nombre del archivo:", nombre_archivo)  # Opcional, para ver el nombre
    resultado = send_file(recipient, archivo)  # Aquí sigue yendo 'archivo' porque es la ruta completa
    print("✅ Resultado del envío:", resultado)
else:
    print("❌ Archivo no encontrado:", archivo)
