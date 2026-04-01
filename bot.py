import telebot
from ai_chat import ai_chat

bot = telebot.TeleBot("8645028727:AAFG-7ljdG1GAuVXUbDtF_QMeavnO_U-F3c")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "UBS da nima gap?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    javob = ai_chat(message.text)
    bot.reply_to(message, javob)
print("Bot ishga tushdi")
bot.infinity_polling()
