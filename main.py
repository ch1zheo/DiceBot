# DiceBot - основной файл с логикой
import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")

# Таймер отправки сообщения после отправки стикера 4 секунды,
# ровно столько сколько идёт анимация кубика
DICE_ANIMATION_SECONDS = 4

dp = Dispatcher()

# Reply-кнопка отправляет боту ровно тот текст, что на ней написан -
# отдельного "callback"-значения, как у inline-кнопок, тут нет.
# Поэтому красивый текст кнопки ловим отдельным фильтром ниже (F.text ==).
DICE_BUTTON_TEXT = "Нажми чтобы бросить кубик! 🎲"

# Клавиатура-меню с кнопкой броска кубика.
# resize_keyboard - чтобы кнопки были компактными, а не на весь экран.
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=DICE_BUTTON_TEXT)],
    ],
    resize_keyboard=True,
)

@dp.message(CommandStart())
async def start_command(message: Message) -> None:
    await message.answer(
        "Привет! Я DiceBot 🎲\n"
        "Нажмите кнопку ниже или введите /dice, чтобы бросить кубик!",
        reply_markup=main_keyboard,
    )

async def roll_dice(message: Message) -> None:
    """Подбрасывает кубик и после паузы (анимация кубика) высылает текст с числом."""
    dice_message = await message.answer_dice(emoji="🎲")
    value = dice_message.dice.value  # 1–6, знаем сразу после отправки

    await asyncio.sleep(DICE_ANIMATION_SECONDS)
    await message.answer(f"Вам выпало {value}!", reply_markup=main_keyboard)

@dp.message(Command("dice"))
async def dice_command(message: Message) -> None:
    """Срабатывает на команду /dice, введённую вручную."""
    await roll_dice(message)

@dp.message(F.text == DICE_BUTTON_TEXT)
async def dice_button(message: Message) -> None:
    """Срабатывает на нажатие кнопки меню (шлёт текст кнопки как обычное сообщение)."""
    await roll_dice(message)

async def main() -> None:
    if not TELEGRAM_BOT_TOKEN:
        raise SystemExit(
            "Ошибка: не найден TELEGRAM_BOT_TOKEN (смотрите default.env.example)"
        )

    bot = Bot(
        token=TELEGRAM_BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    logger.info("DiceBot запущен, жду команды...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())