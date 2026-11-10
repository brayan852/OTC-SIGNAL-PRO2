import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import time

# 1. Servidor web falso para satisfacer los requisitos de puertos de Render
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleHandler)
    server.serve_forever()

# Arrancar el servidor web en segundo plano
threading.Thread(target=run_server, daemon=True).start()

print("Servidor web encendido correctamente en Render.")

# 2. Cargar y mantener la ejecución del bot de Telegram
try:
    import telegram_bot
except Exception as e:
    print(f"Error cargando el bot: {e}")

# Bucle infinito para evitar que el proceso finalice de forma prematura
while True:
    time.sleep(3600)
