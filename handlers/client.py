from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db


#@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Приветствую! Я виртуальный помощник пицерии', reply_markup=kb_client)

#@dp.message_handler(commands=['Режим_работы'])
async def open_hours(message : types.Message):
    await bot.send_message(message.from_user.id, 'Пн-Пт с 10:00 до 21:00, Сб-Вс с 10:00 до 23:00')

#@dp.message_handler(commands=['Расположение'])
async def place(message : types.Message):
    await bot.send_message(message.from_user.id, 'ул. Навагинская 14')#, reply_markup=ReplyKeyboardRemove())

#@dp.message_handler(commands=['Меню'])
async def menu(message : types.Message):
    await sqlite_db.sql_read(message)

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(open_hours, commands=['Режим_работы'])
    dp.register_message_handler(place, commands=['Расположение'])
    dp.register_message_handler(menu, commands=['Меню'])
