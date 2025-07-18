# handlers/start.py

from telegram import Update
from telegram.ext import ContextTypes
from datetime import datetime
import json
import os

USER_FILE = "data/users.json"
ADMIN_ID = 6194108258  # 🔴 এখানে তোমার নিজের ইউজার ID বসাও

def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("🚀 /start command received from:", update.effective_user.username)

    user = update.effective_user
    user_id = str(user.id)
    users = load_users()

    if user_id not in users:
        users[user_id] = {
            "name": user.full_name,
            "username": user.username,
            "joined": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        }
        save_users(users)

        total_users = len(users)
        msg = (
            f"✅ New User Joined\n"
            f"👤 Name: {user.full_name}\n"
            f"🆔 Username: @{user.username or 'None'}\n"
            f"📅 Join Date: {users[user_id]['joined']}\n"
            f"👥 Total Users: {total_users}"
        )
        await context.bot.send_message(chat_id=ADMIN_ID, text=msg)

    await update.message.reply_text("👋 হ্যালো! আপনি বট শুরু করেছেন!")
