import os
from dotenv import load_dotenv

# Carga las variables de entorno locales si existe un archivo .env
load_dotenv()

# Token del bot de Telegram configurado en Render
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TELEGRAM_TOKEN:
    raise ValueError("No se encontró la variable TELEGRAM_TOKEN en el entorno.")
