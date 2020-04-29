from main import bot, dp
from aiogram import types
from data.beers import take_import_beers, take_bakunin_beers, MSG_INFO
from data.const import GS_JSON, URL_STEREO
from data.stereo import PIZZA
from menu.bars_menu import stereo_get_order, stereo_eat_menu


async def menu_list(call):
    if call.data == 'stereo_bakunin':
        await bot.answer_callback_query(call.id)
        actual_beer_list = take_bakunin_beers(GS_JSON, URL_STEREO)
        beers = []
        black_circle = u'\U000026AB'
        for beer in actual_beer_list:
            string = f"{black_circle} *{beer[0].upper()}* _{beer[1].lower()}_ " \
                     f"{beer[2]} {beer[4]} руб.\n{beer[3]}"
            beers.append(string)
        msg = '\n\n'.join(beers)
        await bot.send_message(call.message.chat.id, msg, parse_mode='Markdown', reply_markup=stereo_get_order)
        await bot.send_message(call.message.chat.id, MSG_INFO,  reply_markup=stereo_get_order)


async def eat_menu(call):
    await bot.answer_callback_query(call.id)
    await bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=stereo_eat_menu)


async def get_pizza(call):
    await bot.answer_callback_query(call.id)
    for pizza in PIZZA:
        try:
            await bot.send_photo(call.from_user.id, photo=pizza['image'],
                                 caption=f"*{pizza['name']}* - {pizza['price']}руб.\n{pizza['text']}",
                                 parse_mode='Markdown')
        except:
            msg = f"*{pizza['name']}* - {pizza['price']}руб.\n{pizza['text']}"
            await bot.send_message(call.from_user.id, msg, parse_mode='Markdown')
    await bot.send_message(call.from_user.id, 'Выберите любое блюдо из нашего меню, введите название и количество на '
                                              'этапе заказа (кнопка «сделать заказ»), и мы приготовим его к указанному '
                                              'вами времени.', reply_markup=stereo_get_order)


def register_handlers_stereo(dp: dp):
    dp.register_callback_query_handler(menu_list, lambda call: call.data == 'stereo_bakunin')
    dp.register_callback_query_handler(eat_menu, lambda call: call.data == 'stereo_eat')
    dp.register_callback_query_handler(get_pizza, lambda call: call.data == 'stereo_pizza')
