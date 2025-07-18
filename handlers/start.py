from telegram import Update
from telegram.ext import ContextTypes
from datetime import datetime
import json
import os

USER_FILE = "data/users.json"
ADMIN_ID = 6194108258  # নিজের টেলিগ্রাম আইডি বসাও

def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = str(user.id)
    users = load_users()

    is_new = user_id not in users
    if is_new:
        users[user_id] = {
            "name": user.full_name,
            "username": user.username,
            "joined": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        }
        save_users(users)

        msg = (
            f"✅ New User Joined\n"
            f"👤 Name: {user.full_name}\n"
            f"🆔 Username: @{user.username or 'None'}\n"
            f"📅 Join Date: {users[user_id]['joined']}\n"
            f"👥 Total Users: {len(users)}"
        )
        await context.bot.send_message(chat_id=ADMIN_ID, text=msg)

    await update.message.reply_text("👋 স্বাগতম! আপনি বট চালু করেছেন।")
