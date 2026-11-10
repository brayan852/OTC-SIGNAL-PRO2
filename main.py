import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import time

# 1. Servidor web para mantener contento a Render
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleHandler)
    server.serve_forever()

threading.Thread(target=run_server, daemon=True).start()

# 2. Importar y arrancar tu lógica de Telegram
try:
    import telegram_bot  # O el nombre del archivo donde tengas el código principal de tu bot
except Exception as e:
    print(f"Error al iniciar el bot: {e}")

# Mantener vivo el proceso
while True:
    time.sleep(3600)
