from telegram_bot import TelegramSignalBot

def main():
    print("Iniciando el sistema OTC-SIGNAL-PRO2...")
    print("Cargando módulos y conectando con Telegram...")
    bot = TelegramSignalBot()
    bot.run()

if __name__ == "__main__":
    main()
