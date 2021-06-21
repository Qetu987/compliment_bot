from parser import random_compliment
import telebot
from config import token


def save_id(id):
    if id not in get_ids():
        with open('chat_ids.txt', 'a') as file:
            file.write(str(id) + '\n')


def get_ids():
    with open('chat_ids.txt', 'r') as file:
        data = file.read().split('\n')
        data.pop()
        data = [int(id) for id in data]
        return data


bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я буду присылать тебе комплиментики каждый день, не скучай!')
    bot.send_message(message.chat.id, 'Можешь получить свою дозу прямо сейчас, написав мне что либо')
    save_id(message.chat.id)


@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.send_message(message.chat.id, random_compliment())


bot.polling(none_stop=True)