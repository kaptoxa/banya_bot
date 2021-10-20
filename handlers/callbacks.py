from aiogram import types, md
from aiogram.dispatcher import FSMContext
from misc import bot, dp, join_cb, members
from keyboards import get_keyboard, get_button
from phase import Phase
from config import GROUP_ID

from logging import getLogger

logger = getLogger()



@dp.message_handler(state=Phase.ADD_NAME)
async def say_name(message: types.Message, state: FSMContext):
    logger.info(f"add name from {message.from_user.id}")
    inviter = message.from_user.first_name + ' ' + message.from_user.last_name
    name = f"{message.text} (записал {inviter})"
    if members.add(message.from_user.id, name):
        logger.info(f"try to delete {members.tgid}:{members.tmid}")
        await bot.delete_message(GROUP_ID, members.tmid)
        res = await bot.send_message(GROUP_ID, members.get(), reply_markup=get_keyboard())
        members.tmid = res.message_id
        await message.answer('Участник добавлен.', reply_markup=get_button())
    else:
        await message.answer('Вы уже зарегистрировались на 2 доступных вам места.', reply_markup=get_button())
    await Phase.START.set()


@dp.message_handler(text_startswith='Добавить', state='*')
@dp.message_handler(text_startswith='/start', state='*')
async def cmd_start(message: types.Message, state: FSMContext):
    logger.info(f"join from {message.from_user.first_name}")
    logger.info(f'count: {len(members.members)}, limit: {members.limit}')

    if members.full():
        await message.answer('Мест нет.', reply_markup=get_button())
    else:
        await Phase.ADD_NAME.set()
        await message.answer('Введите имя человека для добавления его в список:', reply_markup=types.ReplyKeyboardRemove())
