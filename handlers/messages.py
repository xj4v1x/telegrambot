# Respuestas a mensajes no relacionados con comandos

from telegram import Update
from telegram.ext import ContextTypes

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.strip()
    response = f"No entiendo: {user_message}. Usa /help para más información."
    await update.message.reply_text(response)
