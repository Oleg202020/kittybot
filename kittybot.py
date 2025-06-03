import logging
import os

import requests  # Импортируем библиотеку для работы с запросами.
from dotenv import load_dotenv
from telebot import TeleBot, types

load_dotenv()
# Теперь переменная TOKEN, описанная в файле .env,
# доступна в пространстве переменных окружения.

# Укажите токен, 
# который вы получили от @Botfather при создании бот-аккаунта:
bot = TeleBot(token=os.getenv('TOKEN'))
# Укажите id своего аккаунта в Telegram:
# chat_id = 5227518325

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

# Ресурс с котиками
URL = 'https://api.thecatapi.com/v1/images/search'


# Код запроса к thecatapi.com и обработку ответа обернём в функцию:
def get_new_image():
    try:
        response = requests.get(URL)
    except Exception as error:
        logging.error(f'Ошибка при запросе к основному API: {error}')
        new_url = 'https://api.thedogapi.com/v1/images/search'
        response = requests.get(new_url)
    # Сделаем GET-запрос к API;
    # метод json() преобразует полученный ответ JSON в тип данных
    response = response.json()
    # Извлекаем из ответа URL картинки:
    random_cat = response[0].get('url')
    return random_cat


# Добавляем хендлер для команды /newcat:
@bot.message_handler(commands=['newcat'])
def new_cat(message):
    chat = message.chat
    bot.send_photo(chat.id, get_new_image())


@bot.message_handler(commands=['start'])
def wake_up(message):
    # В ответ на команду /start
    # должно быть отправлено сообщение "Спасибо, что включили меня".
    chat_id = message.chat.id
    name = message.from_user.first_name
    # Создаём объект клавиатуры:
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаём объект кнопки:
    button = types.KeyboardButton('/newcat')
    """keyboard.row(  # Первая строка кнопок.
        types.KeyboardButton('Который час?'),  # Создаём первую кнопку в строке.
        types.KeyboardButton('Определи мой ip'),  # Создаём вторую кнопку в строке.
    )
    keyboard.row(  # Вторая строка кнопок.
        types.KeyboardButton('/random_digit'),  # Создаём кнопку в строке.
    )"""
    # Добавляем объект кнопки на клавиатуру:
    keyboard.add(button)
    bot.send_message(
        chat_id=chat_id,
        text=f'Привет, {name}. Посмотри, какого котика я тебе нашёл',
        # Отправляем клавиатуру в сообщении бота: передаём объект клавиатуры
        # в параметр reply_markup объекта send_message.
        # Telegram-клиент "запомнит" и будет отображать её в интерфейсе бота.
        reply_markup=keyboard,
    )
    bot.send_photo(chat_id, get_new_image())


@bot.message_handler(content_types=['text'])
def say_hi(message):
    # Из объекта message получаем данные о чате, из которого пришло сообщение,
    # и сохраняем эти данные в переменную chat.
    chat = message.chat
    # Получаем id чата:
    chat_id = chat.id
    # В ответ на любое текстовое сообщение в тот же чат
    # будет отправлено сообщение 'Привет, я KittyBot!'
    bot.send_message(chat_id=chat_id, text='Привет, я KittyBot!')

# Метод polling() запускает процесс; приложение начнёт
# отправлять регулярные запросы для получения входящих сообщений.


def main():
    bot.polling(none_stop=True)


if __name__ == '__main__':
    main()
