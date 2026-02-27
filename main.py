import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = "8557283415:AAEWmvxipGRQsJFaTWn98uR4kQvMA_nWX5U"
disp = Dispatcher()


@disp.message(Command("start"))
async def startMethod(message: Message):
    await message.answer("Bot active")


async def main():
    bot = Bot(token=BOT_TOKEN)

    await disp.start_polling(bot)
