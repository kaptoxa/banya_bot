from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.callback_data import CallbackData

from logging import getLogger
from misc import dp, bot, members
from phase import Phase
from keyboards import get_keyboard

logger = getLogger()


@dp.message_handler(text_startswith='/list', state='*')
async def cmd_start(message: types.Message, state: FSMContext):
    words = message.text.split()
    if len(words) < 3:
        return

    command, limit, *text = message.text.split()
    if not limit.isdigit():
        await message.answer('Количество мест должно быть числом!')
        return

    members.new(' '.join(text), int(limit))
    await message.answer(members.get(), reply_markup=get_keyboard())
    await Phase.START.set()
