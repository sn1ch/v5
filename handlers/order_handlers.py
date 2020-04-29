from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from main import bot, dp
from menu.main_menu import order_menu, order_phone_menu, order_check_menu, back_menu
from menu.menus import markup_menu
from data.const import ORDER_CHAT_BAKUNIN, ORDER_CHAT_KIOSK, ORDER_CHAT_STEREO, ORDER_CHAT_ROKETS
from state import Order


async def start_order(call: types.callback_query, state: FSMContext):
    if call.data == 'get_order_bakunin':
        msg = '*Внимание!* Возможен только самовывоз.\nЗаказ можно забрать по адресу: ' \
              'ул. 2-я Советская 25А, с 13 до 22 часов. Оплата только по _банковской карте_!\n\n' \
              'Напишите нам, что и в каком количестве вы хотите заказать, а также в какое время вам будет' \
              ' удобно забрать заказ. Мы свяжемся с вами для подтверждения заказа!'
        await bot.send_message(call.message.chat.id, msg, parse_mode='Markdown', reply_markup=back_menu)
        # await bot.send_message(call.message.chat.id, 'Напиши чего и сколько хочешь заказать', reply_markup=back_menu)
        await Order.bar.set()
        await state.update_data(bar=ORDER_CHAT_BAKUNIN)
    elif call.data == 'get_order_kiosk':
        msg = '*Внимание!* Возможен только самовывоз.\nЗаказ можно забрать по адресу: ' \
              'ул.Маяковского 23, с 13 до 22 часов. Оплата только по _банковской карте_!\n\n' \
              'Напишите нам, что и в каком количестве вы хотите заказать, а также в какое время вам будет ' \
              'удобно забрать заказ. Мы свяжемся с вами для подтверждения заказа!'
        await bot.send_message(call.message.chat.id, msg, parse_mode='Markdown', reply_markup=back_menu)
        await Order.bar.set()
        await state.update_data(bar=ORDER_CHAT_KIOSK)
    elif call.data == 'get_order_stereo':
        msg = '*Внимание!* Возможен только самовывоз.\nЗаказ можно забрать по адресу: ' \
              'пр.Пискаревский, 1, с 9:30 до 23:30 часов (пиво только до 22:00). Оплата только по' \
              '_банковской карте_!\n\n' \
              'Напишите нам, что и в каком количестве вы хотите заказать, а также в какое время вам будет' \
              ' удобно забрать заказ. В сообщении вы можете оставить предзаказ как на крафтовое пиво, так и на' \
              ' неаполитанскую пиццу и любое другое блюдо из меню Stereo Pub & Pizza.\n\n' \
              'Мы свяжемся с вами для подтверждения заказа!'
        await bot.send_message(call.message.chat.id, msg, parse_mode='Markdown', reply_markup=back_menu)
        await Order.bar.set()
        await state.update_data(bar=ORDER_CHAT_STEREO)
    elif call.data == 'get_order_rokets':
        msg = '*Внимание!* Возможен только самовывоз.\nЗаказ можно забрать по адресу: ' \
              'ул.Гороховая 26, с 13 до 22 часов. Оплата только по _банковской карте_!\n\n' \
              'Напишите нам, что и в каком количестве вы хотите заказать, а также в какое время ' \
              'вам будет удобно забрать заказ. В сообщении вы можете оставить предзаказ как на крафтовое пиво, ' \
              'так и на бургеры и любое другое блюдо из меню Rockets & Bishops.\n\n' \
              'Мы свяжемся с вами для подтверждения заказа!'
        await bot.send_message(call.message.chat.id, msg, parse_mode='Markdown', reply_markup=back_menu)
        await Order.bar.set()
        await state.update_data(bar=ORDER_CHAT_ROKETS)
    await Order.order.set()


async def get_order(message: types.Message, state: FSMContext):
    if message.text != 'НАЗАД':
        order = message.text
        await state.update_data(order=order)
        await message.answer(f'Когда придете за заказом?\n', reply_markup=back_menu,
                             parse_mode='Markdown')
        await Order.time.set()
    elif message.text == 'НАЗАД':
        await state.reset_state()
        await message.reply('Главное меню', reply_markup=markup_menu)


async def get_time(message: types.Message, state: FSMContext):
    if message.text not in ['НАЗАД', None, 'ВЕРНО']:
        time = message.text
        await state.update_data(time=time)
        await message.answer(f'Как вас зовут?\nСейчас: _{message.from_user.first_name}_', reply_markup=order_menu,
                             parse_mode='Markdown')
        await Order.name.set()
    elif message.text == 'ВЕРНО':
        time = 'в ближайшее время'
        await state.update_data(time=time)
        await message.answer(f'Как вас зовут?\nСейчас: _{message.from_user.first_name}_', reply_markup=order_menu,
                             parse_mode='Markdown')
        await Order.name.set()
    elif message.text == 'НАЗАД':
        await state.reset_state()
        await message.reply('Главное меню', reply_markup=markup_menu)


async def get_name(message: types.Message, state: FSMContext):
    if message.text not in ['НАЗАД', None, 'ВЕРНО']:
        name = message.text
        await state.update_data(name=name)
        await message.answer('Введите свой контактный телефон', reply_markup=order_phone_menu)
        await Order.phone.set()
    elif message.text == 'ВЕРНО':
        name = message.from_user.first_name
        await state.update_data(name=name)
        await message.answer('Введите свой контактный телефон', reply_markup=order_phone_menu)
        await Order.phone.set()
    elif message.text == 'НАЗАД':
        await state.reset_state()
        await message.reply('Главное меню', reply_markup=markup_menu)


async def get_phone(message: types.Message, state: FSMContext):
    try:
        phone = message.contact.phone_number
        await state.update_data(phone=phone)
        await message.answer('Вот ваш заказ, все верно?')
        data = await state.get_data()
        msg = f"{data.get('order')}\nЗаберу: {data.get('time')}\n{data.get('name')}\n{data.get('phone')}"
        await message.answer(text=msg, reply_markup=order_check_menu)
    except AttributeError:
        if message.text != 'НАЗАД' and message.text != 'ЗАКАЗ ВЕРЕН':
            phone = message.text
            await state.update_data(phone=phone)
            await message.answer('Вот ваш заказ, все верно?')
            data = await state.get_data()
            msg = f"{data.get('order')}\nЗаберу: {data.get('time')}\n{data.get('name')}\n{data.get('phone')}"
            await message.answer(text=msg, reply_markup=order_check_menu)
    if message.text == 'НАЗАД':
        await state.reset_state()
        await message.reply('Главное меню', reply_markup=markup_menu)
    elif message.text == 'ЗАКАЗ ВЕРЕН':
        data = await state.get_data()
        msg = f" Поступил новый заказ:\n{data.get('bar')[1]}\n{data.get('order')}\nЗаберут: {data.get('time')}\n" \
              f"{data.get('name')}\n{data.get('phone')}"
        await state.reset_state(with_data=False)
        await bot.send_message(data.get('bar')[0], msg, parse_mode='Markdown')
        await message.answer('Ваш заказ принят в обработку, наш сотрудник свяжется в вами в ближайшее время',
                             reply_markup=markup_menu)


def register_handlers_order(dp: dp):
    dp.register_callback_query_handler(start_order, lambda call: call.data in (
        'get_order_bakunin', 'get_order_kiosk', 'get_order_stereo', 'get_order_rokets'))
    dp.register_message_handler(get_order, state=Order.order)
    dp.register_message_handler(get_time, state=Order.time)
    dp.register_message_handler(get_name, state=Order.name)
    dp.register_message_handler(get_phone, state=Order.phone, content_types=['contact', 'text'])
