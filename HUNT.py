import config
import telebot
from telebot import apihelper
bot = telebot.TeleBot(config.token)
apihelper.proxy = {'https':'https//95.110.194.245:54871'}


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет, я искуственный интилект Илья!")


