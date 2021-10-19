from config import TELEGRAM_API_KEY

import logging

from aiogram import Bot, Dispatcher, executor, md, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils.callback_data import CallbackData
from middlewares import AccessMiddleware

from phase import Phase
from members import MembersList
from config import *





logging.basicConfig(level=logging.INFO)

bot = Bot(TELEGRAM_API_KEY)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())


dp.middleware.setup(AccessMiddleware(ACCESS_IDs))

join_cb = CallbackData('join', 'action')

members = MembersList()
