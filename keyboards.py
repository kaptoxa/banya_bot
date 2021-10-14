from aiogram import types
from misc import join_cb

def get_keyboard():
    markup = types.InlineKeyboardMarkup()
    text = ''
    url = 'http://t.me/spiskispb2021_bot'
    button = types.InlineKeyboardButton(text, url=url) #  callback_data=join_cb.new(action='join'))
    markup.row(button)
    return markup
