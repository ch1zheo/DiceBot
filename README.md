# DiceBot

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Version 2.2.1](https://img.shields.io/badge/Version-2.2.1-blue)](CHANGELOG.md)
[![Telegram / aiogram 3](https://img.shields.io/badge/Telegram-aiogram%203-2CA5E0?logo=telegram&logoColor=white)](https://docs.aiogram.dev/)
[![Maintenance](https://img.shields.io/badge/Maintenance-Active-brightgreen)](https://github.com/ch1zheo/DiceBot)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

<details>
<summary>🇬🇧 English</summary>

A simple Telegram bot built with **aiogram 3.x**. It rolls a die and, after 4 seconds (while the Telegram animation plays), sends the result as text. The bot picks the reply language from the Telegram client: Russian clients get Russian, everyone else gets English.

## What the bot does

- `/start` — welcome message

- `/dice` — rolls a die, waits 4 seconds (the animation length) and sends the rolled value

- A `ReplyKeyboard` button that does the same as `/dice`

- Automatic language selection: Russian for Russian-language Telegram clients, English otherwise

## Requirements

- Python 3.10+

- A Telegram bot token from [@BotFather](https://t.me/BotFather)

## Project structure

```text
DiceBot/
├── .github/
│   └── workflows/
│       └── ci.yml
├── locales/
│   ├── __init__.py
│   ├── en.py
│   └── ru.py
├── .env.example
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── main.py
├── README.md
└── requirements.txt
```

## Installation

1. Download the project:

   ```bash
   git clone https://github.com/ch1zheo/DiceBot.git
   cd DiceBot
   ```

   No Git? Download the ZIP archive from the repository page and unpack it.

2. Get a bot token:

   I. Message [@BotFather](https://t.me/BotFather) on Telegram

   II. Send `/newbot` and follow the instructions

   III. Copy the issued token, which looks like `123456789:AAExampleTokenString`

3. Set up and run the bot for your system:

   - [Windows](#windows)

   - [Linux (Ubuntu/Debian Based)](#linux-ubuntudebian-based)

   - [macOS](#macos)

### Windows

1. Install Python:

   - Download it from [python.org](https://www.python.org/downloads/) (version 3.10+)

   - During installation, **make sure** to tick **"Add Python to PATH"**

2. Open PowerShell (or CMD) in the project folder and create a virtual environment:

   ```powershell
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install the dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

4. Create the `.env` file from the example:

   ```powershell
   Copy-Item .env.example .env
   ```

5. Open `.env` in a text editor and paste your token:

   - TELEGRAM_BOT_TOKEN=your_token_here

6. Run the bot:

   ```powershell
   python main.py
   ```

### Linux (Ubuntu/Debian Based)

1. Install Python and venv:

   ```bash
   sudo apt update
   sudo apt install python3 python3-venv python3-pip
   ```

2. Go to the project folder and create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create the `.env` file from the example:

   ```bash
   cp .env.example .env
   ```

5. Open `.env` in a text editor and paste your token:

   - TELEGRAM_BOT_TOKEN=your_token_here

6. Run the bot:

   ```bash
   python3 main.py
   ```

### macOS

1. Install Python, most easily with [Homebrew](https://brew.sh):

   ```bash
   brew install python
   ```

2. Go to the project folder and create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create the `.env` file from the example:

   ```bash
   cp .env.example .env
   ```

5. Open `.env` in a text editor and paste your token:

   - TELEGRAM_BOT_TOKEN=your_token_here

6. Run the bot:

   ```bash
   python3 main.py
   ```

## Testing it

1. Find your bot in Telegram by the name you set in BotFather

2. Send `/start` — you should receive a greeting

3. Send `/dice` or press the button below the input field — the bot rolls a die, waits 4 seconds and sends the rolled number

- Stopping the bot

Press `Ctrl + C` in the terminal where `main.py` is running.

## Troubleshooting

- **`ERROR: TELEGRAM_BOT_TOKEN is not set`** — the token was not found. Check that `.env` is in the same folder as `main.py` and that the variable is named exactly `TELEGRAM_BOT_TOKEN`.

- **`ModuleNotFoundError: No module named 'aiogram'`** — the virtual environment is not active or the dependencies are not installed. Repeat the venv activation steps and `pip install -r requirements.txt`.

- **The bot does not respond** — make sure the script is running and the terminal shows no errors; check that the token was copied completely, without extra spaces.

## Contributing

If you find a bug, fix it and open a pull request. See [CONTRIBUTING.md](CONTRIBUTING.md) for the workflow and add a note to [CHANGELOG.md](CHANGELOG.md).

## 📜 License

This project is distributed under the MIT license. See [LICENSE](LICENSE) for details.

Author: Ch1zheo

</details>

<details>
<summary>🇷🇺 Русский</summary>

Простой Telegram-бот на **aiogram 3.x**, который бросает игральную кость и через 4 секунды (пока играет анимация в Telegram) присылает результат текстом. Язык ответа бот определяет по языку Telegram-клиента: для русскоязычных клиентов — русский, для остальных — английский.

## Что делает бот

- `/start` — приветственное сообщение

- `/dice` — бросает кубик, ждёт 4 секунды (длительность анимации) и пишет выпавшее значение

- Кнопка `ReplyKeyboard`, которая делает то же самое, что и `/dice`

- Автоопределение языка: русский для русскоязычных клиентов Telegram, английский для всех остальных

## Требования

- Python 3.10+

- Токен Telegram-бота от [@BotFather](https://t.me/BotFather)

## Структура проекта

```text
DiceBot/
├── .github/
│   └── workflows/
│       └── ci.yml
├── locales/
│   ├── __init__.py
│   ├── en.py
│   └── ru.py
├── .env.example
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── main.py
├── README.md
└── requirements.txt
```

## Установка

1. Скачайте проект:

   ```bash
   git clone https://github.com/ch1zheo/DiceBot.git
   cd DiceBot
   ```

   Нет Git? Скачайте ZIP-архив со страницы репозитория и распакуйте его.

2. Получите токен бота:

   I. Напишите [@BotFather](https://t.me/BotFather) в Telegram

   II. Отправьте команду `/newbot` и следуйте инструкциям

   III. Скопируйте выданный токен вида `123456789:AAExampleTokenString`

3. Настройте и запустите бота для своей системы:

   - [Windows](#windows-1)

   - [Linux (Ubuntu/Debian Based)](#linux-ubuntudebian-based-1)

   - [macOS](#macos-1)

### Windows

1. Установите Python:

   - Скачайте с [python.org](https://www.python.org/downloads/) (версия 3.10+)

   - При установке **обязательно** поставьте галочку **"Add Python to PATH"**

2. Откройте PowerShell (или CMD) в папке проекта и создайте виртуальное окружение:

   ```powershell
   python -m venv venv
   venv\Scripts\activate
   ```

3. Установите зависимости:

   ```powershell
   pip install -r requirements.txt
   ```

4. Создайте файл `.env` из примера:

   ```powershell
   Copy-Item .env.example .env
   ```

5. Откройте `.env` в блокноте и вставьте свой токен:

   - TELEGRAM_BOT_TOKEN=ваш_токен_сюда

6. Запустите бота:

   ```powershell
   python main.py
   ```

### Linux (Ubuntu/Debian Based)

1. Установите Python и venv:

   ```bash
   sudo apt update
   sudo apt install python3 python3-venv python3-pip
   ```

2. Перейдите в папку проекта и создайте виртуальное окружение:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

4. Создайте файл `.env` из примера:

   ```bash
   cp .env.example .env
   ```

5. Откройте `.env` в блокноте и вставьте свой токен:

   - TELEGRAM_BOT_TOKEN=ваш_токен_сюда

6. Запустите бота:

   ```bash
   python3 main.py
   ```

### macOS

1. Установите Python, проще всего через [Homebrew](https://brew.sh):

   ```bash
   brew install python
   ```

2. Перейдите в папку проекта и создайте виртуальное окружение:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

4. Создайте файл `.env` из примера:

   ```bash
   cp .env.example .env
   ```

5. Откройте `.env` в блокноте и вставьте свой токен:

   - TELEGRAM_BOT_TOKEN=ваш_токен_сюда

6. Запустите бота:

   ```bash
   python3 main.py
   ```

## Проверка работы

1. Найдите своего бота в Telegram по имени, которое вы задали в BotFather

2. Отправьте `/start` — должно прийти приветствие

3. Отправьте `/dice` или нажмите на кнопку ниже клавиатуры — бот кинет кубик, подождёт 4 секунды и напишет выпавшее число

- Остановка бота

Нажмите `Ctrl + C` в терминале, где запущен `main.py`.

## Возможные проблемы

- **`ERROR: TELEGRAM_BOT_TOKEN is not set`** — токен не найден. Проверьте, что файл `.env` лежит в той же папке, что и `main.py`, и что переменная называется именно `TELEGRAM_BOT_TOKEN`.

- **`ModuleNotFoundError: No module named 'aiogram'`** — виртуальное окружение не активировано или зависимости не установлены. Повторите шаги активации `venv` и `pip install -r requirements.txt`.

- **Бот не отвечает** — убедитесь, что скрипт запущен и в терминале нет ошибок; проверьте, что токен скопирован полностью, без лишних пробелов.

## Участие в разработке

Если вы нашли баг, спокойно фиксите, но обязательно скажите о баге автору. Порядок работы описан в [CONTRIBUTING.md](CONTRIBUTING.md), а запись об изменении добавьте в [CHANGELOG.md](CHANGELOG.md).

## 📜 Лицензия

Этот проект распространяется под лицензией MIT. Подробности смотрите в файле [LICENSE](LICENSE).

Автор: Ch1zheo

</details>
