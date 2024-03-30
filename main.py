from telegram import Update
from telegram.ext import ContextTypes, Application, CommandHandler
from dotenv import load_dotenv
import os

from database_utils import get_random_item, delete_item_by_id, get_item_by_id

load_dotenv()


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет, октагон!")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_message = """Команды бота:
    /site - отправляет в чат ссылку на сайт октагона
    /creator - отправляет в чат ФИО создателя
    /randomItem - возвращает случайный предмет
    /deleteItem ID - удаляет предмет по ID
    /getItemByID ID - возвращает предмет по ID"""
    await update.message.reply_text(help_message)


async def site_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html('<a href="https://students.forus.ru/">Сайт Октагона</a>')


async def creator_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("creator: Игумнов Сергей Васильевич")


async def random_item_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = await get_random_item()
    if result:
        item = result[0]
        response_message = f"({item['id']}) - {item['name']}: {item['desc']}"
    else:
        response_message = "Ошибка: Нет доступных предметов."
    await update.message.reply_text(response_message)


async def delete_item_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        item_id = int(context.args[0])
        success = await delete_item_by_id(item_id)
        response_message = "Предмет удачно удален." if success else "Ошибка: Предмет не найден."
    except (IndexError, ValueError):
        response_message = "Ошибка: Пожалуйста, укажите ID предмета для удаления."
    await update.message.reply_text(response_message)


async def get_item_by_id_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        item_id = int(context.args[0])
        result = await get_item_by_id(item_id)
        if result:
            item = result[0]
            response_message = f"({item['id']}) - {item['name']}: {item['desc']}"
        else:
            response_message = "Ошибка: Предмет не найден."
    except (IndexError, ValueError):
        response_message = "Ошибка: Пожалуйста, укажите ID предмета."
    await update.message.reply_text(response_message)


if __name__ == '__main__':
    application = Application.builder().token(os.getenv('TOKEN')).build()
    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('site', site_command))
    application.add_handler(CommandHandler('creator', creator_command))
    application.add_handler(CommandHandler('randomItem', random_item_command))
    application.add_handler(CommandHandler('deleteItem', delete_item_command))
    application.add_handler(CommandHandler('getItemByID', get_item_by_id_command))
    application.run_polling(allowed_updates=Update.ALL_TYPES)
