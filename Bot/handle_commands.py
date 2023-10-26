from settings import bot
from telebot import types


def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("🕹")
    markup.add(btn)
    bot.send_message(message.chat.id, "Нажми на кнопку", reply_markup=markup)


def user_help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Выбери действие")
    markup.add(btn)
    bot.send_message(message.chat.id,
                     f"Привет, я твой бот-помощник, кладОвщик {message.from_user.first_name},"
                     f" посчитаем баллы? Нажми на петуха.\n"
                     f"Коллеги по расписанию? Жми клоуна",
                     reply_markup=markup
                     )
    bot.send_sticker(
        message.chat.id,
        "CAACAgIAAxkBAAEBUMxlHmKJsybze4CLlXU1yZs0vHSU8QACgQADRA3PF8jAOMgk_BkZMAQ"
    )
