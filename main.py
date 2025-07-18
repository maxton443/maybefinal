from telegram.ext import ApplicationBuilder, CommandHandler
from handlers.start import start_command
from handlers.menu import menu_handler
from handlers.admin import admin_handler
import asyncio

TOKEN = "7773509344:AAFS6Pfbgtz48NQ2januQoLjDhs-eZ_w1w0"  # এখানে তোমার টোকেন

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("menu", menu_handler))
app.add_handler(CommandHandler("admin", admin_handler))

print("✅ Bot started polling...")  # এই লাইন যোগ করলাম

if __name__ == "__main__":
    asyncio.run(app.run_polling())
