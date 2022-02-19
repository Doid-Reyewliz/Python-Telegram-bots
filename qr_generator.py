# TelegramBotAPI
import telebot

# QR code
import pyqrcode

import time

# Токен бота (его можно взять у @BotFather)
token="1497360982:AAGDg94IAYWmG0eMxdDp4gVzosnG-GGHcmM"
bot=telebot.TeleBot(token)

# создание команды /start
@bot.message_handler(commands=['start'])
def start_message(msg):
    # делает вид что бот печатает сообщение
    bot.send_chat_action(msg.chat.id, 'typing')
    # вывод сообщения после поманды /start 
    bot.send_message(msg.chat.id,'Hey There,\n Use /qr_code to generate QR CODE ')

# создание команды /qr_code
@bot.message_handler(commands=['qr_code'])
def qr_code_handler(message):   
    # делает вид что бот печатает сообщение
    bot.send_chat_action(message.chat.id, 'typing')
    # вывод сообщения после поманды /qr_code
    sent = bot.send_message(message.chat.id, "Send Text or Url")
    # отправляет текст в "def qrcode"
    bot.register_next_step_handler(sent, qrcode)

def qrcode(message):
    # импорт сообщения
    url=pyqrcode.create(message.text)
    url.png('qrcode.png',scale=15)
    # отправляет картинку 
    bot.send_chat_action(message.chat.id, 'upload_document')
    bot.send_document(message.chat.id,open('qrcode.png','rb' ))

while True:
	try:
        # нужен только для обхода падения бота путем перезапуска его
		bot.infinity_polling(True)
	except Exception:
		time.sleep(1)
