import asyncio
import logging
from aiogram import Bot

from bot_config import bot, dp, database


async def on_startup(bot: Bot):
    database.create_tables()


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
