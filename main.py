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

from locales import DICE_BUTTON_TEXTS, get_text

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")

DICE_ANIMATION_SECONDS = 4

dp = Dispatcher()


def main_keyboard(language_code: str | None) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=get_text(language_code, "dice_button"))],
        ],
        resize_keyboard=True,
    )


@dp.message(CommandStart())
async def start_command(message: Message) -> None:
    language_code = message.from_user.language_code if message.from_user else None
    await message.answer(
        get_text(language_code, "start"),
        reply_markup=main_keyboard(language_code),
    )


async def roll_dice(message: Message) -> None:
    language_code = message.from_user.language_code if message.from_user else None
    dice_message = await message.answer_dice(emoji="🎲")
    value = dice_message.dice.value

    await asyncio.sleep(DICE_ANIMATION_SECONDS)
    await message.answer(
        get_text(language_code, "dice_result", value=value),
        reply_markup=main_keyboard(language_code),
    )


@dp.message(Command("dice"))
async def dice_command(message: Message) -> None:
    await roll_dice(message)


@dp.message(F.text.in_(DICE_BUTTON_TEXTS))
async def dice_button(message: Message) -> None:
    await roll_dice(message)


async def main() -> None:
    if not TELEGRAM_BOT_TOKEN:
        raise SystemExit(
            "Ошибка: не найден TELEGRAM_BOT_TOKEN (смотрите .env.example)"
        )

    bot = Bot(
        token=TELEGRAM_BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    logger.info("DiceBot запущен, жду команды...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
