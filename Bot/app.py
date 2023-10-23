import telebot
import requests
from telebot import types
from settings import TOKEN, x

bot = telebot.TeleBot(TOKEN)
data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

user_dict = {}


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
    user = message.from_user.id
    first_key = (user, {})
    user_dict.update([first_key])
    if user in user_dict.keys():
        a = ('a', message.text)
        user_dict[user].update([a])
        calc2 = bot.send_message(message.chat.id, "Приемка")
        bot.register_next_step_handler(calc2, next_func2)
    else:
        calc = bot.send_message(message.chat.id, "Сборка")
        bot.register_next_step_handler(calc, next_func)


def next_func2(message):
    user = message.from_user.id
    if user in user_dict.keys():
        b = ('b', message.text)
        user_dict[user].update([b])
        calc3 = bot.send_message(message.chat.id, "Разнос")
        bot.register_next_step_handler(calc3, next_func3)
    else:
        calc2 = bot.send_message(message.chat.id, "Приемка")
        bot.register_next_step_handler(calc2, next_func2)


def next_func3(message):
    user = message.from_user.id
    if user in user_dict.keys():
        c = ('c', message.text)
        user_dict[user].update([c])
        calc3 = bot.send_message(message.chat.id, "Инвент")
        bot.register_next_step_handler(calc3, next_func4)
    else:
        calc3 = bot.send_message(message.chat.id, "Разнос")
        bot.register_next_step_handler(calc3, next_func3)


def next_func4(message):
    user = message.from_user.id
    if user in user_dict.keys():
        d = ('d', message.text)
        user_dict[user].update([d])
        calc3 = bot.send_message(message.chat.id, "Выдача Н")
        bot.register_next_step_handler(calc3, next_func5)
    else:
        calc3 = bot.send_message(message.chat.id, "Инвент")
        bot.register_next_step_handler(calc3, next_func4)


def next_func5(message):
    user = message.from_user.id
    if user in user_dict.keys():
        e = ('e', message.text)
        user_dict[user].update([e])
        calc3 = bot.send_message(message.chat.id, "Выдача Б/У")
        bot.register_next_step_handler(calc3, next_func6)
    else:
        calc3 = bot.send_message(message.chat.id, "Выдача Н")
        bot.register_next_step_handler(calc3, next_func5)


def next_func6(message):
    user = message.from_user.id
    try:
        if user in user_dict.keys():
            f = ('f', message.text)
            user_dict[user].update([f])
        else:
            calc3 = bot.send_message(message.chat.id, "Выдача Б/У")
            bot.register_next_step_handler(calc3, next_func6)

        sq = user_dict[user]
        res = (int(sq['b']) + int(sq['f']))*0.8 + (int(sq['a']) + int(sq['c']) + int(sq['d']) + int(sq['e'])) * 0.5
        bot.send_message(message.chat.id, f"{message.from_user.first_name}, у тебя {res} баллов")
        bot.send_sticker(
            message.chat.id,
            "CAACAgIAAxkBAAEBUNZlHmOwYndrYRwlDajrQTpSFquFFgAChgADRA3PF5hySbZkSauxMAQ"
        )
        del user_dict[user]
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
        del user_dict[user]


def comrade(message):
    try:
        g = message.text
        bot.send_message(message.chat.id, f"Счетоводы на {g} число:\n {x[g]}")
        bot.send_sticker(
            message.chat.id,
            "CAACAgIAAxkBAAEBUjplHqXI5AnG0_-BdsNJQZVOfYDRaAACaQADRA3PF06e1cjIjCI1MAQ"
        )
    except KeyError:
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
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEBV2NlIGmf4yU2Vp1LE5d7v-iGqrCBwAACqwADwZxgDASGdYaYFD_QMAQ")
    send_welcome(message)


if __name__ == "__main__":
    bot.infinity_polling()
