import asyncio
import logging
from aiogram import Bot

from bot_config import bot, dp, database
from handlers.start import start_router
from handlers.home_word import home_router


async def on_startup(bot: Bot):
    database.create_tables()


async def main():
    dp.include_router(start_router)
    dp.include_router(home_router)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
