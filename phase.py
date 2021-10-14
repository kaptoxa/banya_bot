from aiogram.dispatcher.filters.state import State, StatesGroup


class Phase(StatesGroup):

    START = State()
    ADD_NAME = State()
