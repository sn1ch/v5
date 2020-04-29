from main import bot, dp
from data.beers import take_bakunin_beers, MSG_INFO
from data.const import GS_JSON, URL_ROKETS
from data.rokets import BURGER
from menu.bars_menu import rokets_get_order, rokets_eat_menu


async def menu_list(call):
    if call.data == 'rokets_bakunin':
        await bot.answer_callback_query(call.id)
        actual_beer_list = take_bakunin_beers(GS_JSON, URL_ROKETS)
        beers = []
        black_circle = u'\U000026AB'
        for beer in actual_beer_list:
            string = f"{black_circle} *{beer[0].upper()}* _{beer[1].lower()}_ " \
                     f"{beer[2]} {beer[4]} руб.\n{beer[3]}"
            beers.append(string)
        msg = '\n\n'.join(beers)
        await bot.send_message(call.message.chat.id, msg, parse_mode='Markdown')
        await bot.send_message(call.message.chat.id, MSG_INFO,  reply_markup=rokets_get_order)

async def eat_menu(call):
    await bot.answer_callback_query(call.id)
    await bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=rokets_eat_menu)


async def get_burger(call):
    await bot.answer_callback_query(call.id)
    for burger in BURGER:
        try:
            await bot.send_photo(call.from_user.id, photo=burger['image'],
                                 caption=f"*{burger['name']}* - {burger['price']}руб.\n{burger['text']}",
                                 parse_mode='Markdown')
        except:
            msg = f"*{burger['name']}* - {burger['price']}руб.\n{burger['text']}"
            await bot.send_message(call.from_user.id, msg, parse_mode='Markdown')
    await bot.send_message(call.from_user.id, 'Выберите любое блюдо из нашего меню, введите название и количество на '
                                              'этапе заказа (кнопка «сделать заказ»), и мы приготовим его к указанному '
                                              'вами времени.', reply_markup=rokets_get_order)


def register_handlers_rokets(dp: dp):
    dp.register_callback_query_handler(menu_list, lambda call: call.data in ('rokets_bakunin'))
    dp.register_callback_query_handler(eat_menu, lambda call: call.data in ('rokets_eat'))
    dp.register_callback_query_handler(get_burger, lambda call: call.data in ('rokets_burger'))
