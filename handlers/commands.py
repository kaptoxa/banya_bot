from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.callback_data import CallbackData

from logging import getLogger
from misc import dp, bot, members
from phase import Phase
from keyboards import get_keyboard

from config import GROUP_ID
logger = getLogger()


@dp.message_handler(text_startswith='/list', state='*')
async def cmd_start(message: types.Message, state: FSMContext):
    logger.info(f" group id : {message.chat.id} : {type(message.chat.id)}")
    words = message.text.split()
    if len(words) < 3:
        return

    command, limit, *text = message.text.split()
    if not limit.isdigit():
        await message.answer('Количество мест должно быть числом!')
        return

    logger.info(f"members list {message.message_id}")
    members.new(' '.join(text), int(limit), message.message_id, message.chat.id)
    text = members.get()
    logger.info(f"{text} to {message.chat.id}")
#    await message.answer(text, reply_markup=get_keyboard())
    res = await bot.send_message(GROUP_ID, text, reply_markup=get_keyboard())
    members.tmid = res.message_id
    await Phase.START.set()