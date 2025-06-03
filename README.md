# 🐾 KittyBot

Telegram-бот, который присылает случайных котиков (или собачку, если котиковый API недоступен).

## Содержание
1. [Возможности](#возможности)
2. [Стек](#стек)
3. [Быстрый старт (локально)](#быстрый-старт-локально)
4. [Структура проекта](#структура-проекта)
5. [Переменные окружения](#переменные-окружения)
6. [Обработка ошибок](#обработка-ошибок)
7. [Логи](#логи)
8. [Развёртывание в Docker](#развёртывание-в-docker-опционально)
9. [Контакты](#контакты)
---

## Возможности
- **/start** — приветствие пользователя, показ клавиатуры с кнопкой **/newcat** и мгновенная отправка первого изображения.  
- **/newcat** — присылает новое случайное изображение котика.  
- Ответ на **любое** текстовое сообщение: &laquo;Привет, я KittyBot!&raquo;.  
- Резервный запрос к TheDogAPI, если TheCatAPI недоступен.  
- Логирование действий и ошибок через `logging`.

## Стек
- **Python 3.11+**
- [`pytelegram‑bot‑api`](https://github.com/eternnoir/pyTelegramBotAPI) (класс `TeleBot`)
- `requests`, `python‑dotenv`
- TheCatAPI и TheDogAPI для изображений

## Быстрый старт (локально)

1. Склонируйте репозиторий и создайте виртуальное окружение:

   ```bash
   git clone git@github.com:Oleg202020/kittybot.git
   cd kittybot
   python -m venv venv
   source venv/Scripts/activate   # Linux/macOS: source venv/bin/activate
   pip install -r requirements.txt
   ```

2. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

3. Получите токен у @BotFather.

4. Создайте файл .env в корне проекта:

    ```env
    # .env
    TOKEN=<ВАШ_ТОКЕН_ЗДЕСЬ>
    ```

5. Запустите:

    ```bash
    python main.py          # или kittybot.py — имя вашего файла
    ```

Бот начнёт опрашивать Telegram и отвечать пользователям.

## Структура проекта
    ```text
    kittybot/
    ├── bot.py              # Основная логика
    ├── requirements.txt    # Зависимости
    ├── .env.example        # Пример переменных окружения
    └── README.md
    ```

## Переменные окружения

| Переменная	| Описание  | 
|---------------|-----------| 
| 'TOKEN'	| Токен, полученный у @BotFather.

## Обработка ошибок

Если запрос к https://api.thecatapi.com/v1/images/search завершается ошибкой, бот автоматически обращается к https://api.thedogapi.com/v1/images/search, чтобы пользователь всё равно получил картинку.

## Логи
Логи выводятся в 'stdout': 2025‑06‑03 10:15:32,123 - root - INFO - Сообщение

Для продакшн‑окружения рекомендуется перенаправлять вывод в файл или систему централизованного логирования.

## Развёртывание в Docker (опционально)

```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "bot.py"]
```

```bash
docker build -t kittybot .
docker run -d --env TOKEN=<TOKEN> kittybot
```

## Контакты

* Автор: Larionov Oleg
* E-mail: jktu2005@yandex.ru
* GitHub: @Oleg202020

Удачного кодинга и пусть в вашем чате будет больше котиков! 🐱