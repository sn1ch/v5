from aiogram import types
from data.bars import BARS

markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
markup_menu.add(*[types.KeyboardButton(text=f"{bar['name']} ({bar['address']})") for bar in BARS])


def bar_menu(bar_name: str, bars=BARS):
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_back = types.KeyboardButton('НАЗАД К БАРАМ')
    for bar in bars:
        if bar_name == bar['name']:
            btn_menu = types.KeyboardButton(f"МЕНЮ {bar['name']}")
            btn_actions = types.KeyboardButton(f"АКЦИИ {bar['name']}")
            menu.add(btn_menu, btn_actions)
    menu.add(btn_back)

    return menu


bakunin_menu = bar_menu('КАФЕ БАКУНИН')
kiosk_menu = bar_menu('KIOSK')
rokets_menu = bar_menu('ROCKETS & BISHOPS')
stereo_menu = bar_menu('STEREO pub & pizza')
