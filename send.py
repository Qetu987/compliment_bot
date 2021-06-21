import telebot
from parser import random_compliment
from config import token


def get_ids():
    with open('chat_ids.txt', 'r') as file:
        data = file.read().split('\n')
        data.pop()
        data = [int(id) for id in data]
        return data


bot = telebot.TeleBot(token)


for id in get_ids():
    try:
        bot.send_message(id, random_compliment())
    except:
        print('no chat')