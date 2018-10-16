#!/usr/bin/env python
import os
import re

import telegram
from flask import Flask, request

from dotenv import load_dotenv
load_dotenv()


params = ['Название компании', 'Описание вакансии',
          'Технологии', 'Офис или удаленка', 'Тип работы', 'Ссылка', 'Зарплатная вилка']


def split_text(text):
    return text.split('\n===============\n')


def add_hashtag(text):
    regex = re.compile('\w+')
    my_list = regex.findall(text)
    hashtag_list = ["#" + word for word in my_list]
    return ', '.join(hashtag_list)


def generate_message(params, values):
    message = '#вакансия\n\n'
    for param, value in zip(params, values):
        if (param == 'Технологии' or param == 'Офис или удаленка' or param == 'Тип работы'):
            value = add_hashtag(value)
        message = message + param + ': ' + value + '\n'
    return message


app = Flask(__name__)


@app.route('/')
def print_hello():
    return "Test message"


@app.route('/post', methods=['POST'])
def print_data():
    values = split_text(request.data.decode('utf-8'))
    # bot = telegram.Bot(os.getenv('BOT_KEY'))
    message = generate_message(params, values)
    print(message)
    # bot.send_message(chat_id=os.getenv('CHAT_ID'), text=message)
    return message


if __name__ == '__main__':
    app.run()
