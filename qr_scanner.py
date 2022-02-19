# Telegram
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, Filters, MessageHandler, CallbackContext

# QR код
from pyzbar.pyzbar import decode

# Системные библиотеки
from PIL import Image
import os

# Токен бота (его можно взять у @BotFather)
TOKEN = "1364034013:AAGVKSy-9cc-7Tk2OGN1hbT0DJ7Mfw8LyoI"

def decode_qr(update: Update, context: CallbackContext):
	chat_id = update.message.chat_id

	if update.message.photo:
		id_img = update.message.photo[-1].file_id
	else:
		return

	foto = context.bot.getFile(id_img)

	new_file = context.bot.get_file(foto.file_id)
	new_file.download('qrcode.png')

	try:
		result = decode(Image.open('qrcode.png'))
		context.bot.sendMessage(chat_id=chat_id, text=result[0].data.decode("utf-8"))
		os.remove("qrcode.png")
	except Exception as e:
		context.bot.sendMessage(chat_id=chat_id, text=str(e))

def main():
	updater = Updater(TOKEN, request_kwargs={'read_timeout': 20, 'connect_timeout': 20}, use_context=True)
	dp = updater.dispatcher

	dp.add_handler(MessageHandler(Filters.photo, decode_qr))

	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()
