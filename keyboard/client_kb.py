from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/меню')
b4 = KeyboardButton('Поделиться_номером', request_contact=True)
b5 = KeyboardButton('Поделиться местоположением', request_location=True)
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(b1, b2, b3).row(b4, b5)