import requests  # Импортируем библиотеку для работы с запросами.
from telebot import TeleBot

bot = TeleBot(token='6928510449:AAG10-RlKfOdMRw2sZlQT3sLfjAgSMhD3S8')

URL = 'https://api.thecatapi.com/v1/images/search'
chat_id = 5227518325
# Сделаем GET-запрос к API;
# метод json() преобразует полученный ответ JSON в тип данных, понятный Python.
response = requests.get(URL).json()
# Извлекаем из ответа URL картинки:
random_cat_url = response[0].get('url')

text = 'Вам телеграмма!'
# Отправка сообщения
bot.send_message(chat_id, text)
# Передаём chat_id и URL картинки в метод для отправки фото:
bot.send_photo(chat_id, random_cat_url)
