from aiogram.dispatcher.filters.state import StatesGroup, State

class Observer(StatesGroup):

    photo = State()
    description = State()