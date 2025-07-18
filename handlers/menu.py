from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["📊 Total Users", "ℹ️ About"]]
    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("👇 অপশনগুলো বেছে নিন:", reply_markup=markup)
