from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from logging import getLogger

logger = getLogger()

class AccessMiddleware(BaseMiddleware):
    def __init__(self, access_ids):
        self.access_ids = set(int(id) for id in access_ids.split())
        super().__init__()

    async def on_pre_process_message(self, message: types.ContentType.TEXT, _):
        logger.info(f'on_pre_process_mes {message.from_user.id}')

        if message.text.startswith('/list'):
            logger.info('it is /list!')
            if int(message.from_user.id) not in self.access_ids: 
                await message.answer("Команду list могут использовать только администраторы группы.")
                raise CancelHandler()
