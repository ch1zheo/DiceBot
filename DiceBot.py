# DiceBot - основной файл с логикой
import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")

# Таймер отправки сообщения после отправки стикера 4 секунды
# ровно столько сколько идёт анимация кубика
DICE_ANIMATION_SECONDS = 4

dp = Dispatcher()

@dp.message(CommandStart())
async def start_command(message: Message) -> None:
    await message.answer(
        "Привет! Я DiceBot 🎲\n"
        "Введите /dice чтобы бросить кубик!"
    )

@dp.message(Command("dice"))
async def dice_command(message: Message) -> None:
    """Подбрасывает кубик и после паузы (анимация кубика) высылает текст с числом."""
    dice_message = await message.answer_dice(emoji="🎲")
    value = dice_message.dice.value  # 1–6, знаем сразу после отправки

    await asyncio.sleep(DICE_ANIMATION_SECONDS)
    await message.answer(f"Вам выпало {value}!")

async def main() -> None:
    if not TELEGRAM_BOT_TOKEN:
        raise SystemExit(
            "Ошибка: не найдет TELEGRAM_BOT_TOKEN (смотрите .env.example)"
        )

    bot = Bot(
        token=TELEGRAM_BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    logger.info("DiceBot запущен, жду команды...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
