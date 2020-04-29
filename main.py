import asyncio
import logging
from aiogram import Bot, Dispatcher, executor
from data.const import TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage

logging.basicConfig(level=logging.INFO)
loop = asyncio.get_event_loop()
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage, loop=loop)

if __name__ == '__main__':
    from handlers.main_handlers import *
    executor.start_polling(dp, skip_updates=True)