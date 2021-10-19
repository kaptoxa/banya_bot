from aiogram import types
from misc import join_cb

def get_keyboard():
    markup = types.InlineKeyboardMarkup()
    text = 'Присоединиться'
#    url = 'http://t.me/spiskispb2021_bot'
    url = 'http://t.me/gazprom_test_bot'
    button = types.InlineKeyboardButton(text, url=url) #  callback_data=join_cb.new(action='join'))
    markup.row(button)
    return markup
