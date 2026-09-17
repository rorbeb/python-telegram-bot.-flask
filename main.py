import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = os.environ["BOT_TOKEN"]
MY_ID = int(os.environ["MY_ID"])

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        await context.bot.send_message(
            chat_id=MY_ID,
            text=f"📩 Новый вопрос:\n\n{update.message.text}"
        )

bot = Application.builder().token(TOKEN).build()
bot.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message))

print("Бот запущен!")
bot.run_polling()