from telegram import Update
from telegram.ext import ContextTypes, Application, CommandHandler
from dotenv import load_dotenv
import os


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет, октагон!")


if __name__ == '__main__':
    load_dotenv()
    application = Application.builder().token(os.getenv('TOKEN')).build()
    application.add_handler(CommandHandler('start', start))
    application.run_polling(allowed_updates=Update.ALL_TYPES)
