from main import bot, dp
from data.beers import take_import_beers, take_bakunin_beers, MSG_INFO
from data.const import GS_JSON, URL_BAKUNIN
from menu.bars_menu import bakunin_get_order
import db.models
from db.models import Beer

db = db.models.DBCommands()


async def menu_list(call):
    if call.data == 'bakunin_bakunin':
        await bot.answer_callback_query(call.id)
        actual_beer_list = take_bakunin_beers(GS_JSON, URL_BAKUNIN)
        beers = []
        black_circle = u'\U000026AB'
        for beer in actual_beer_list:
            string = f"{black_circle} *{beer[0].upper()}* _{beer[1].lower()}_ " \
                     f"{beer[2]} {beer[4]} руб.\n{beer[3]}"
            # b = await db.add_new_beer(name=beer[0], style=beer[1], price=beer[4], volume=beer[2], text=beer[3])
            beers.append(string)
        msg_beers = '\n\n'.join(beers)
        await bot.send_message(call.message.chat.id, msg_beers, parse_mode='Markdown')
        await bot.send_message(call.message.chat.id, MSG_INFO,  reply_markup=bakunin_get_order)
    # if call.data == 'bakunin_bakunin':
    #     await bot.answer_callback_query(call.id)
    #     await db.get_beers()
    elif call.data == 'bakunin_import':
        actual_beer_list = take_import_beers(GS_JSON, URL_BAKUNIN)
        beers = []
        black_circle = u'\U000026AB'
        for beer in actual_beer_list:
            string = f"{black_circle} *{beer[0].upper()}* _{beer[1].lower()}_ " \
                     f"{beer[2]} {beer[4]} руб.\n{beer[3]}"
            beers.append(string)
        msg = '\n\n'.join(beers)
        await bot.send_message(call.message.chat.id, msg, parse_mode='Markdown')
        await bot.send_message(call.message.chat.id, MSG_INFO,  reply_markup=bakunin_get_order)


async def menu_list2(call):
    if call.data == 'bakunin_bakunin':
        await bot.answer_callback_query(call.id)
        await db.get_beers()



def register_handlers_bakunin(dp: dp):
    dp.register_callback_query_handler(menu_list, lambda call: call.data in ('bakunin_bakunin', 'bakunin_import'))
    # dp.register_callback_query_handler(menu_list2, lambda call: call.data in ('bakunin_bakunin', 'bakunin_impor;/;t'))
