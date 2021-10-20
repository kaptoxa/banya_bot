from aiogram import types
from misc import join_cb

from config import GROUP_ID

def get_keyboard():
    markup = types.InlineKeyboardMarkup()
    text = 'Присоединиться'
    url = f'http://t.me/spiskispb2021_bot?start={GROUP_ID}'
#    url = 'http://t.me/gazprom_test_bot'
    button = types.InlineKeyboardButton(text, url=url) #  callback_data=join_cb.new(action='join'))
    markup.row(button)
    return markup


def get_button():
    markup = types.ReplyKeyboardMarkup().row('Добавить участника')
    return markup
