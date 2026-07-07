# DiceBot Main Script
import asyncio
import logging
import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")

# Timer before displaying the result as text -
# exactly the duration of the dice animation in Telegram
DICE_ANIMATION_SECONDS = 5


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Hello! i'm DiceBot 🎲\n"
        "Type /dice to roll the die!"
    )


async def dice_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Rolls the die and, after a pause (while the animation plays), writes the result."""
    message = await update.message.reply_dice(emoji="🎲")
    value = message.dice.value  # 1–6, known immediately

    await asyncio.sleep(DICE_ANIMATION_SECONDS)
    await update.message.reply_text(f"You got {value}!")


def main() -> None:
    if not TELEGRAM_BOT_TOKEN:
        raise SystemExit(
            "ERROR: TELEGRAM_BOT_TOKEN is not set in .env (see .env.example)"
        )

    app: Application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("dice", dice_command))

    logger.info("DiceBot started, waiting for commands...")
    app.run_polling()


if __name__ == "__main__":
    main()
