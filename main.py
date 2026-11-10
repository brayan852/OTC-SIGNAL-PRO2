import os
import time
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

# 1. Servidor web obligatorio para satisfacer el puerto de Render
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleHandler)
    server.serve_forever()

# Iniciar servidor web en segundo plano
threading.Thread(target=run_server, daemon=True).start()
print("Servidor web iniciado en el puerto de Render.")

# 2. Función para arrancar tu bot de Telegram en paralelo
def run_telegram_bot():
    try:
        # Importa tu script del bot (si tu archivo principal del bot se llama diferente, cámbialo aquí)
        import telegram_bot 
    except Exception as e:
        print(f"Error al iniciar el bot de Telegram: {e}")

# Arrancar el bot en un segundo hilo para que no bloquee el servidor web
threading.Thread(target=run_telegram_bot, daemon=True).start()

# Mantener la aplicación viva indefinidamente
while True:
    time.sleep(3600)
