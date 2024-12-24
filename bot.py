from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from handlers.commands import start, help_command
from handlers.messages import handle_message
from config import BOT_TOKEN

def main():
    # Construye la aplicación del bot
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Manejo de comandos
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    # Manejo de mensajes genéricos
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Inicia el bot
    print("Bot está corriendo...")
    app.run_polling()

if __name__ == "__main__":
    main()