from main import send_file

prompt = "C:\Proyectos-Marlenne\WhatsApp-server\whatsapp-mcp\whatsapp-mcp-server\WhatsApp Image 2025-06-02 at 11.32.15.jpeg"
recipient = "5217641291840@s.whatsapp.net"

resultado = send_file(recipient,prompt)

print("Resultado:")
print(resultado)
