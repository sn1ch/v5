from aiogram.dispatcher.filters.state import State, StatesGroup


class Order(StatesGroup):
    bar = State()
    order = State()
    time = State()
    name = State()
    phone = State()
