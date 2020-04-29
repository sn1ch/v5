from main import bot, dp
from data.beers import take_import_beers, take_bakunin_beers, take_russian_beers, MSG_INFO
from data.const import GS_JSON, URL_KIOSK
from menu.bars_menu import kiosk_get_order


async def menu_list(call):
    if call.data == 'kiosk_bakunin':
        await bot.answer_callback_query(call.id)
        actual_beer_list = take_bakunin_beers(GS_JSON, URL_KIOSK)
        beers = []
        black_circle = u'\U000026AB'
        for beer in actual_beer_list:
            string = f"{black_circle} *{beer[0].upper()}* _{beer[1].lower()}_ " \
                     f"{beer[2]} {beer[4]} руб.\n{beer[3]}"
            beers.append(string)
        msg = '\n\n'.join(beers)
        await bot.send_message(call.message.chat.id, msg, parse_mode='Markdown')
        await bot.send_message(call.message.chat.id, MSG_INFO,  reply_markup=kiosk_get_order)
    elif call.data == 'kiosk_import':
        actual_beer_list = take_import_beers(GS_JSON, URL_KIOSK)
        beers = []
        black_circle = u'\U000026AB'
        for beer in actual_beer_list:
            string = f"{black_circle} *{beer[0].upper()}* _{beer[1].lower()}_ " \
                     f"{beer[2]} {beer[4]} руб.\n{beer[3]}"
            beers.append(string)
        msg = '\n\n'.join(beers)
        await bot.send_message(call.message.chat.id, msg, parse_mode='Markdown')
        await bot.send_message(call.message.chat.id, MSG_INFO,  reply_markup=kiosk_get_order)
    elif call.data == 'kiosk_rus':
        actual_beer_list = take_russian_beers(GS_JSON, URL_KIOSK)
        beers = []
        black_circle = u'\U000026AB'
        for beer in actual_beer_list:
            string = f"{black_circle} *{beer[0].upper()}* _{beer[1].lower()}_ " \
                     f"{beer[2]} {beer[4]} руб.\n{beer[3]}"
            beers.append(string)
        msg = '\n\n'.join(beers)
        await bot.send_message(call.message.chat.id, msg, parse_mode='Markdown')
        await bot.send_message(call.message.chat.id, MSG_INFO,  reply_markup=kiosk_get_order)


def register_handlers_kiosk(dp: dp):
    dp.register_callback_query_handler(menu_list,
                                       lambda call: call.data in ('kiosk_bakunin', 'kiosk_import', 'kiosk_rus'))
