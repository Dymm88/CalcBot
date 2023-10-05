import telebot
import requests
from telebot import types
from settings import *

bot = telebot.TeleBot(TOKEN)
data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton("🐓")
    btn2 = types.KeyboardButton("🤡")
    btn3 = types.KeyboardButton("🤑")
    markup.row(btn1, btn2)
    markup.row(btn3)
    bot.send_message(
        message.chat.id,
        f"здорово, кладОвщик {message.from_user.first_name},"
        f" посчитаем баллы? Нажми на петуха.\n"
        f"Коллеги по расписанию? Жми клоуна",
        reply_markup=markup
    )
    bot.send_sticker(
        message.chat.id,
        "CAACAgIAAxkBAAEBUMxlHmKJsybze4CLlXU1yZs0vHSU8QACgQADRA3PF8jAOMgk_BkZMAQ"
    )


@bot.message_handler(content_types=["text"])
def calc(message):
    if message.text == "🐓":
        calc = bot.send_message(message.chat.id, "Сборка")
        bot.register_next_step_handler(calc, next_func)
    elif message.text == "🤡":
        ans = bot.send_message(message.chat.id, "Какой день?")
        bot.register_next_step_handler(ans, comrade)
    elif message.text == "🤑":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        btn_usd = types.KeyboardButton("💸")
        btn_eur = types.KeyboardButton("💶")
        markup.row(btn_usd, btn_eur)
        money = bot.send_message(message.chat.id, "Выбери валюту", reply_markup=markup)
        bot.register_next_step_handler(money, convert)


def next_func(message):
    global a
    a = message.text
    calc2 = bot.send_message(message.chat.id, "Приемка")
    bot.register_next_step_handler(calc2, next_func2)


def next_func2(message):
    global b
    b = message.text
    calc3 = bot.send_message(message.chat.id, "Разнос")
    bot.register_next_step_handler(calc3, next_func3)


def next_func3(message):
    global c
    c = message.text
    calc4 = bot.send_message(message.chat.id, "Инвент")
    bot.register_next_step_handler(calc4, next_func4)


def next_func4(message):
    global d
    d = message.text
    calc5 = bot.send_message(message.chat.id, "выдача Н")
    bot.register_next_step_handler(calc5, next_func5)


def next_func5(message):
    global e
    e = message.text
    calc6 = bot.send_message(message.chat.id, "выдача Б/У")
    bot.register_next_step_handler(calc6, res)


def res(message):
    try:
        global f
        f = message.text
        res = ((int(b) + int(f)) * 0.8 +
               (int(a) + int(c) + int(d) + int(e)) * 0.5)
        bot.send_message(message.chat.id, f"У тебя {res} баллов")
        bot.send_sticker(
            message.chat.id,
            "CAACAgIAAxkBAAEBUNZlHmOwYndrYRwlDajrQTpSFquFFgAChgADRA3PF5hySbZkSauxMAQ"
        )
    except ValueError:
        bot.send_message(
            message.chat.id,
            f"Цифры вводи, {message.from_user.first_name},"
            f" совсем Ебанько???"
        )
        bot.send_sticker(
            message.chat.id,
            "CAACAgIAAxkBAAEBUNRlHmOX6atHGhb4QbTbPlGDccS5TgACgwADRA3PF-t8ZIYBnSqzMAQ"
                         )


def comrade(message):
    try:
        g = message.text
        bot.send_message(message.chat.id, f"Счетоводы на {g} число:\n {x.get(g)}")
        bot.send_sticker(
            message.chat.id,
            "CAACAgIAAxkBAAEBUjplHqXI5AnG0_-BdsNJQZVOfYDRaAACaQADRA3PF06e1cjIjCI1MAQ"
        )
    except ValueError:
        bot.send_message(
            message.chat.id,
            f"Ты что ввёл,совсем цифры забыл, или Ебаклак???"
                )
        bot.send_sticker(
            message.chat.id,
            "CAACAgIAAxkBAAEBUNRlHmOX6atHGhb4QbTbPlGDccS5TgACgwADRA3PF-t8ZIYBnSqzMAQ"
        )


def convert(message):
    mon = message.text
    if mon == "💸":
        bot.send_message(
            message.chat.id,
            f"{data['Valute']['USD']['Name']} {data['Valute']['USD']['Value']}"
        )
    if mon == "💶":
        bot.send_message(
            message.chat.id,
            f"{data['Valute']['EUR']['Name']} {data['Valute']['EUR']['Value']}"
        )


bot.infinity_polling()
