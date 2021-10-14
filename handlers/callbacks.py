from aiogram import types, md
from aiogram.dispatcher import FSMContext
from misc import bot, dp, join_cb, members
from keyboards import get_keyboard
from phase import Phase

from logging import getLogger

logger = getLogger()


@dp.callback_query_handler(join_cb.filter(action='join'), state=Phase.START)
async def join_click(query: types.CallbackQuery, callback_data: dict, state: FSMContext):
    logger.info(f"join from {query.from_user.first_name}")
    logger.info(f'count: {len(members.members)}, limit: {members.limit}')

    if members.full():
        await query.message.answer('Местов немае!')
    else:
        await Phase.ADD_NAME.set()
        await query.message.answer('Введите имя человека для добавления его в список:')


@dp.message_handler(state=Phase.ADD_NAME)
async def say_name(message: types.Message, state: FSMContext):
    logger.info(f"add name from {message.from_user.id}")
    inviter = query.from_user.first_name + ' ' + query.from_user.last_name
    name = f"{message.text} (записал {inviter})"
    if members.add(query.from_user.id, name):
        await query.message.edit_text(members.get(), reply_markup=get_keyboard())
    else:
        await query.message.answer('Вы уже зарегистрировались на 2 доступных вам места.')
    await Phase.START.set()
