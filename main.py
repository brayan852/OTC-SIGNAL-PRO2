import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# Servidor web falso para que Render detecte el puerto y no cierre el bot
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleHandler)
    server.serve_forever()

# Ejecutar el servidor en segundo plano
threading.Thread(target=run_server, daemon=True).start()
