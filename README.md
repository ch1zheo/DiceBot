# DiceBot

Простой Telegram-бот на **aiogram 3.x**, который бросает игральную кость и через 4 секунды (пока играет анимация в Telegram) присылает результат текстом.

# Что делает бот

- `/start` - приветственное сообщение

- `/dice` - бросает кубик, ждёт 4 секунд (длительность анимации) и пишет выпавшее значение

- Также, `ReplyKeyboard` кнопка команды /dice

# Требования

- Python 3.10+

- Токен Telegram-бота от [@BotFather](https://t.me/BotFather)

# Структура проекта

DiceBot/

├── DiceBot.py

├── requirements.txt

├── .env

├── LICENSE

└── README.md

# Установка

1. Получение токена бота

   I. Напишите [@BotFather](https://t.me/BotFather) в Telegram

   II. Отправьте команду `/newbot` и следуйте инструкциям

   III. Скопируйте выданный токен вида `123456789:AAExampleTokenString`

Внимание! Перед запуском не забудьте открыть терминал в папке проекта и активировать окружение (venv\Scripts\activate для Windows, source /venv/bin/activate для Linux, macOS)

# Windows

1. Установите Python:

   - Скачайте с [python.org](https://www.python.org/downloads/) (версия 3.10+)

   - При установке **обязательно** поставьте галочку **"Add Python to PATH"**

2. Откройте PowerShell (или CMD) в папке проекта и создайте виртуальное окружение:

   - python -m venv venv

   - venv\Scripts\activate

3. Установите зависимости:

   - pip install -r requirements.txt

4. Создайте файл `.env`, скопируйте содержимое файла default.env.example в созданный файл.

5. Откройте `.env` в блокноте и вставьте свой токен:

   - TELEGRAM_BOT_TOKEN=ваш_токен_сюда

6. Запустите бота:

   - python main.py

# Linux (Ubuntu/Debian Based)

1. Установите Python и venv:

   - sudo apt update

   - sudo apt install python3 python3-venv python3-pip

2. Перейдите в папку проекта и создайте виртуальное окружение:

   - python3 -m venv venv

   - source venv/bin/activate

3. Установите зависимости:

   - pip install -r requirements.txt

4. Создайте файл `.env`, скопируйте содержимое файла default.env.example в созданный файл.

5. Запустите бота:

   - python main.py

# macOS

1. Установите Python, проще всего через [Homebrew](https://brew.sh):

   - brew install python

2. Перейдите в папку проекта и создайте виртуальное окружение:

   - python3 -m venv venv

   - source venv/bin/activate

3. Установите зависимости:

   - pip install -r requirements.txt

4. Создайте файл `.env`, скопируйте содержимое файла default.env.example в созданный файл.

5. Запустите бота:

   - python main.py

- Проверка работы

1. Найдите своего бота в Telegram по имени, которое вы задали в BotFather

2. Отправьте `/start` - должно прийти приветствие

3. Отправьте `/dice` или нажмите на кнопку ниже клавиатуры - бот кинет кубик, подождёт 4 секунды и напишет выпавшее число

- Остановка бота

Нажмите `Ctrl + C` в терминале, где запущен `DiceBot.py`.

# Возможные проблемы

- **`ERROR: TELEGRAM_BOT_TOKEN is not set`** - токен не найден. Проверьте, что файл `.env` лежит в той же папке, что и `DiceBot.py`, и что переменная называется именно `TELEGRAM_BOT_TOKEN`.

- **`ModuleNotFoundError: No module named 'aiogram'`** - виртуальное окружение не активировано или зависимости не установлены. Повторите шаги активации `venv` и `pip install -r requirements.txt`.

- **Бот не отвечает** - убедитесь, что скрипт запущен и в терминале нет ошибок; проверьте, что токен скопирован полностью, без лишних пробелов.

# Что изменилось в V2.1

1. Добавлена ReplyKeyboard-кнопка с командой **`/dice`**

# Важная информация

Если вы нашли баг, спокойно фиксите, но обязательно скажите о баге автору!

MIT License - используйте как хотите но указывайте автора.

Автор - Ch1zheo