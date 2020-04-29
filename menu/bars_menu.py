from aiogram import types
from data.bars import BARS

# choice_bar_menu = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=1)
# choice_bar_menu.add(
#     *[types.InlineKeyboardButton(text=f"{bar['name']} ({bar['address']})", callback_data=bar['name']) for bar in BARS])
"""
МЕНЮ 
"""
bakunin_bar_menu = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_bakunin_bakunin_beers = types.InlineKeyboardButton(text='БАКУНИН КРАФТ', callback_data='bakunin_bakunin')
btn_bakunin_import_beers = types.InlineKeyboardButton(text='ИМПОРТНЫЙ КРАФТ', callback_data='bakunin_import')
btn_bakunin_untappd = types.InlineKeyboardButton(text='UNTAPPD',
                                                 url='https://untappd.com/v/bakunin-beer-cafe-and-boutique/788042')
bakunin_bar_menu.add(btn_bakunin_bakunin_beers, btn_bakunin_import_beers, btn_bakunin_untappd)

bakunin_get_order = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_get_order = types.InlineKeyboardButton(text='СДЕЛАТЬ ЗАКАЗ', callback_data='get_order_bakunin')
bakunin_get_order.add(btn_bakunin_bakunin_beers, btn_bakunin_import_beers, btn_bakunin_untappd, btn_get_order)

kiosk_bar_menu = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_kiosk_bakunin_beers = types.InlineKeyboardButton(text='БАКУНИН КРАФТ', callback_data='kiosk_bakunin')
btn_kiosk_import_beers = types.InlineKeyboardButton(text='ИМПОРТНЫЙ КРАФТ', callback_data='kiosk_import')
btn_kiosk_russian_beers = types.InlineKeyboardButton(text='РОССИЙСКИЙ КРАФТ', callback_data='kiosk_rus')
btn_kiosk_untappd = types.InlineKeyboardButton(text='UNTAPPD', url='https://untappd.com/v/kiosk/6248902')
kiosk_bar_menu.add(btn_kiosk_bakunin_beers, btn_kiosk_import_beers, btn_kiosk_russian_beers, btn_kiosk_untappd)

kiosk_get_order = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_get_order = types.InlineKeyboardButton(text='СДЕЛАТЬ ЗАКАЗ', callback_data='get_order_kiosk')
kiosk_get_order.add(btn_kiosk_bakunin_beers, btn_kiosk_import_beers, btn_kiosk_russian_beers, btn_kiosk_untappd,
                    btn_get_order)

stereo_bar_menu = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_stereo_bakunin_beers = types.InlineKeyboardButton(text='БАКУНИН КРАФТ', callback_data='stereo_bakunin')
btn_stereo_eats_takeaway = types.InlineKeyboardButton(text='ЕДА take away', callback_data='stereo_eat')
btn_stereo_eats_delivery = types.InlineKeyboardButton(text='ЕДА доставка', url='https://stereopizza.ru')
stereo_bar_menu.add(btn_stereo_bakunin_beers, btn_stereo_eats_delivery, btn_stereo_eats_takeaway)

stereo_eat_menu = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_stereo_pizza = types.InlineKeyboardButton(text='ПИЦЦА', callback_data='stereo_pizza')
btn_stereo_pasta = types.InlineKeyboardButton(text='ПАСТА', callback_data='stereo_paste')
btn_stereo_salad = types.InlineKeyboardButton(text='САЛАТЫ', callback_data='stereo_salad')
btn_stereo_soup = types.InlineKeyboardButton(text='СУПЫ', callback_data='stereo_soup')
btn_stereo_breakfast = types.InlineKeyboardButton(text='ЗАВТРАКИ', callback_data='stereo_breakfast')
stereo_eat_menu.add(btn_stereo_pizza, btn_stereo_pasta, btn_stereo_salad, btn_stereo_soup, btn_stereo_breakfast)

stereo_get_order = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_get_order = types.InlineKeyboardButton(text='СДЕЛАТЬ ЗАКАЗ', callback_data='get_order_stereo')
stereo_get_order.add(btn_stereo_bakunin_beers, btn_stereo_eats_delivery, btn_stereo_eats_takeaway, btn_get_order)



rokets_bar_menu = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_rokets_bakunin_beers = types.InlineKeyboardButton(text='БАКУНИН КРАФТ', callback_data='rokets_bakunin')
btn_rokets_eats = types.InlineKeyboardButton(text='ЕДА', callback_data='rokets_eat')
rokets_bar_menu.add(btn_rokets_bakunin_beers, btn_rokets_eats)

rokets_eat_menu = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_rokets_burger = types.InlineKeyboardButton(text='БУРГЕРЫ', callback_data='rokets_burger')
btn_rokets_soup = types.InlineKeyboardButton(text='СУПЫ', callback_data='rokets_soup')
rokets_eat_menu.add(btn_rokets_burger, btn_rokets_soup)

rokets_get_order = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_get_order = types.InlineKeyboardButton(text='СДЕЛАТЬ ЗАКАЗ', callback_data='get_order_rokets')
rokets_get_order.add(btn_rokets_bakunin_beers, btn_rokets_eats, btn_get_order)
