from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from main import bot, dp, storage
# from menu.main_menu import markup_menu, order_menu, order_phone_menu, order_check_menu
from menu.main_menu import order_menu, order_phone_menu, order_check_menu
from menu.menus import markup_menu, stereo_menu, bakunin_menu, kiosk_menu, rokets_menu
from menu.bars_menu import rokets_bar_menu, kiosk_bar_menu, bakunin_bar_menu, stereo_bar_menu, \
    stereo_eat_menu
from data.actions import ACTIONS
from button_filter import Button, Button_list
from handlers.bakunin_handlers import register_handlers_bakunin
from handlers.kiosk_handlers import register_handlers_kiosk
from handlers.order_handlers import register_handlers_order
from handlers.stereo_handlers import register_handlers_stereo
from handlers.rokets_handlers import register_handlers_rokets


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    print(message)
    await message.reply('Привет! Я бот пивоварни Бакунин!', reply_markup=markup_menu)


@dp.message_handler(Button_list(('КАФЕ БАКУНИН (2-я Советская, 25А)', 'KIOSK (Маяковского, 23)',
                                 'ROCKETS & BISHOPS (Гороховая, 26)', 'STEREO pub & pizza (Пискаревский проспект, 1)')))
async def choice_bar(message: types.Message):
    if message.text == 'КАФЕ БАКУНИН (2-я Советская, 25А)':
        msg = 'Привет, это меню КАФЕ БАКУНИН'
        await bot.send_message(message.chat.id, msg, reply_markup=bakunin_menu)
    elif message.text == 'STEREO pub & pizza (Пискаревский проспект, 1)':
        msg = 'Привет, это меню STEREO pub & pizza (Пискаревский проспект, 1)'
        await bot.send_message(message.chat.id, msg, reply_markup=stereo_menu)
    elif message.text == 'ROCKETS & BISHOPS (Гороховая, 26)':
        msg = 'Привет, это меню ROCKETS & BISHOPS'
        await bot.send_message(message.chat.id, msg, reply_markup=rokets_menu)
    elif message.text == 'KIOSK (Маяковского, 23)':
        msg = 'Привет, это меню KIOSK'
        await bot.send_message(message.chat.id, msg, reply_markup=kiosk_menu)


@dp.message_handler(
    Button_list(('АКЦИИ КАФЕ БАКУНИН', 'АКЦИИ STEREO pub & pizza', 'АКЦИИ KIOSK', 'АКЦИИ ROCKETS & BISHOPS')))
async def send_actions(message: types.Message):
    msg = ACTIONS[message.text]
    await bot.send_message(message.chat.id, msg)


@dp.message_handler(Button_list(('НАЗАД К БАРАМ', 'НАЗАД')))
async def back_to_choice_bar(message: types.Message):
    await message.answer('Выберите бар', reply_markup=markup_menu)


@dp.message_handler(
    Button_list(('МЕНЮ КАФЕ БАКУНИН', 'МЕНЮ ROCKETS & BISHOPS', 'МЕНЮ KIOSK', 'МЕНЮ STEREO pub & pizza')))
async def bar_menu(message: types.Message):
    if message.text == 'МЕНЮ КАФЕ БАКУНИН':
        await message.answer('Выбери раздел КАФЕ БАКУНИН', reply_markup=bakunin_bar_menu)
    elif message.text == 'МЕНЮ ROCKETS & BISHOPS':
        await message.answer('Выбери раздел ROCKETS & BISHOPS', reply_markup=rokets_bar_menu)
    elif message.text == 'МЕНЮ KIOSK':
        await message.answer('Выбери раздел KIOSK', reply_markup=kiosk_bar_menu)
    elif message.text == 'МЕНЮ STEREO pub & pizza':
        await message.answer('Выбери раздел STEREO pub & pizza', reply_markup=stereo_bar_menu)


register_handlers_bakunin(dp)
register_handlers_kiosk(dp)
register_handlers_stereo(dp)
register_handlers_order(dp)
register_handlers_rokets(dp)


@dp.message_handler(content_types='photo')
async def a(message: types.PhotoSize):
    print(message)
    print('cerf')
