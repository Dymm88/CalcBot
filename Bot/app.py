from settings import bot
from utils import (
    next_func, next_func2, next_func3, choice_menu,
    next_func4, next_func5, next_func6, choice_button,
    exchange, collab
)
from handle_commands import start, user_help


@bot.message_handler(commands=['start'])
def send_welcome(message):
    start(message)


@bot.message_handler(commands=['help'])
def user_answer(message):
    user_help(message)


@bot.message_handler(content_types=["text"])
def calc(message):
    choice_menu(message)
    choice_button(message)


def handle_next_step(message):
    next_func(message)
    next_func2(message)
    next_func3(message)
    next_func4(message)
    next_func5(message)
    next_func6(message)


def comrade(message):
    collab(message)


def convert(message):
    exchange(message)


if __name__ == "__main__":
    bot.infinity_polling()
