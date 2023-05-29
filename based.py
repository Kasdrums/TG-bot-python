import telebot

bot = telebot.TeleBot('6012929682:AAFrCLLbHuoh9szVIihZnmOf5u1PACLFH78'
)

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Здорово, Меченный')
    
bot.polling(none_stop=True)