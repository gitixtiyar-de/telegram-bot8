
import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton


TOKEN = "8709726619:AAGddqmDnsBqlITg1KofTxRzkISxUTJ57Os"


async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    # Javob tugmalari
    quiz_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="A) Toshkent"),
                KeyboardButton(text="B) Samarqand")
            ],
            [
                KeyboardButton(text="C) Buxoro"),
                KeyboardButton(text="D) Andijon")
            ]
        ],
        resize_keyboard=True
    )

    # /start komandasi
    @dp.message(CommandStart())
    async def start_handler(message: Message):
        await message.answer(
            "🎮 Quiz botiga xush kelibsiz!\n\n"
            "❓ Savol: O'zbekistonning poytaxti qaysi shahar?",
            reply_markup=quiz_keyboard
        )

    # To'g'ri javob
    @dp.message(F.text == "A) Toshkent")
    async def correct_answer(message: Message):
        await message.answer(
            "🎉 To'g'ri javob!\n"
            "O'zbekistonning poytaxti — Toshkent. 🇺🇿"
        )

    # Noto'g'ri javoblar
    @dp.message(
        F.text.in_({
            "B) Samarqand",
            "C) Buxoro",
            "D) Andijon"
        })
    )
    async def wrong_answer(message: Message):
        await message.answer(
            "❌ Noto'g'ri javob.\n"
            "Yana urinib ko'ring! 😊"
        )

    print("Bot ishga tushdi...")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

