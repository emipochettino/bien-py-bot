import telebot
import os
from random import randrange

RITO_TOKEN = os.environ['RITO_TOKEN']

if RITO_TOKEN is None:
    raise Exception("RITO_TOKEN not set")

answers = [
    "bien pa vo pa?",
    "bieeeeeeeen pa vo pa?",
    "feró pa vo pa?",
    "ahí andamo pa vo pa?",
]

RITO_TOKEN = os.environ['RITO_TOKEN']
bot = telebot.TeleBot(RITO_TOKEN)

@bot.message_handler(regexp="(?i)(vo pa)|(ola pa)|(bien pa)")
def answer_bien_pa(message):
    bot.reply_to(message, answers[randrange(0, len(answers) - 1)])
    print("name: [{}] lastname: [{}] username: [{}] said: {}".format(message.from_user.first_name, message.from_user.last_name, message.from_user.username, message.text))


bot.polling()
