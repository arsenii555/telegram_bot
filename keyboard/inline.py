from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = '5084589506:AAGj3NoSsrkStwaWkXo_--dQ01I5_9nTP3g'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

answ = dict()

urlkb = InlineKeyboardMarkup(row_width=2)
urlButton1 = InlineKeyboardButton(text='Ссылка', url='hhtps://google.com')
urlButton2 = InlineKeyboardButton(text='Ссылка2', url='hhtps://google.com')
x = [InlineKeyboardButton(text='Ссылка3', url='hhtps://google.com'),
     InlineKeyboardButton(text='Ссылка4', url='hhtps://google.com'),
     InlineKeyboardButton(text='Ссылка5', url='hhtps://google.com')]
urlkb.add(urlButton1, urlButton2).row(*x).insert(
    InlineKeyboardButton(text='Ссылка2', url='hhtps://google.com'))


@dp.message_handler(commands='Ссылки')
async def url_command(message: types.Message):
    await message.answer('Ссылочки', reply_markup=urlkb)


inkb = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(text='Like', callback_data='like_1'), InlineKeyboardButton(text='Dislike', callback_data='like_-1'))

@dp.message_handler(commands='test')
async def test_commands(message : types.Message):
    await message.answer('За то чтобы била ИГЭ па барьба', reply_markup=inkb)

@dp.callback_query_handler(Text(startswith='like_'))
async def www_call(callback : types.CallbackQuery):
    result = int(callback.data.split('_')[1])
    if f'{callback.from_user.id}' not in answ:
        answ[f'{callback.from_user.id}'] = result
        await callback.answer('Вы проголосовали')
    else:
        await callback.answer('Вы уже проголосовали', show_alert=True)


executor.start_polling(dp, skip_updates=True)


