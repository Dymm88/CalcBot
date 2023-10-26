import os
import telebot
import requests
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

user_dict = {}


comrade_dict = {
    "1": "",
    "2": "",
    "3": "",
    "4": "",
    "5": "",
    "6": "Дима, Миша",
    "7": "Егор, Саня",
    "8": "Егор",
    "9": "Саня, Дима, Даня",
    "10": "Дима, Даня",
    "11": "Миша, Даня",
    "12": "Миша",
    "13": "Саня, Миша",
    "14": "Егор, Даня",
    "15": "Егор",
    "16": "Саня, Дима",
    "17": "Дима",
    "18": "Миша, Даня",
    "19": "Миша",
    "20": "Егор, Миша",
    "21": "Саня, Дима",
    "22": "Егор",
    "23": "Саня, Даня",
    "24": "Дима",
    "25": "Даня",
    "26": "Какие-то петушки",
    "27": "Егор, Миша",
    "28": "Егор, Саня",
    "29": "Дима",
    "30": "Даня",
    "31": "Дима",
}

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
