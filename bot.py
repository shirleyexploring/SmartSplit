import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from ocr_utils import extract_text_from_image, extract_total_amount

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

RECEIPT_DIR = "receipts"
os.makedirs(RECEIPT_DIR, exist_ok=True)

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo_file = await update.message.photo[-1].get_file()
    file_path = os.path.join(RECEIPT_DIR, f"{update.message.message_id}.jpg")
    await photo_file.download_to_drive(file_path)

    text = extract_text_from_image(file_path)
    amount = extract_total_amount(text)

    await update.message.reply_text(f"🧾 Extracted total: {amount}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    photo_handler = MessageHandler(filters.PHOTO, handle_photo)
    app.add_handler(photo_handler)
    app.run_polling()
