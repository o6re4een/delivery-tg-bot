from aiogram import types, Dispatcher, Bot
import asyncio

from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
import os
import logging
import sys
from bot.handlers.handlers import router
from bot.handlers.menu_handler import menu_router
from bot.handlers.basket_handler import basket_router
from aiogram.utils.chat_action import ChatActionMiddleware
from config import config
from aiogram.fsm.strategy import FSMStrategy

async def main() ->None:
    bot = Bot(token=config.bot_token.get_secret_value())

    dp = Dispatcher(bot=bot, storage=MemoryStorage(), fsm_strategy=FSMStrategy.USER_IN_CHAT)
    dp.include_routers(router, menu_router, basket_router)
    dp.message.middleware(ChatActionMiddleware())

    try:
        await dp.start_polling(bot)
    except Exception as error:
        print(error)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")