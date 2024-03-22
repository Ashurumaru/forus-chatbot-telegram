from telegram import Update
from telegram.ext import ContextTypes, Application, CommandHandler
from dotenv import load_dotenv
import os


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет, октагон!")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_message = """Команды бота:
    /site - отправляет в чат ссылку на сайт октагона
    /creator - отправляет в чат ФИО создателя
    """
    await update.message.reply_text(help_message)


async def site_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html('<a href="https://students.forus.ru/">Сайт Октагона</a>')


async def creator_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("creator: Игумнов Сергей Васильевич")


if __name__ == '__main__':
    load_dotenv()
    application = Application.builder().token(os.getenv('TOKEN')).build()
    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('site', site_command))
    application.add_handler(CommandHandler('creator', creator_command))
    application.run_polling(allowed_updates=Update.ALL_TYPES)
