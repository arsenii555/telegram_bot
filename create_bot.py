from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
TOKEN = '5084589506:AAGj3NoSsrkStwaWkXo_--dQ01I5_9nTP3g'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
