from aiogram import Router, F
from aiogram.types import Message

start_router = Router()

@start_router.message(F.text == "/start")
async def start_command(message: Message):
    await message.answer("hello!")



