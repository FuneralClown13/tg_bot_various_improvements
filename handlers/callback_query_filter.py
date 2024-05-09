from aiogram import Router
from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery
from loguru import logger
import time

router = Router()

"""
Пример реализации устаревания клавиатуры
"""

class IsMessageOutdated(BaseFilter):
    """
    Класс фильтр для демонстрации фильтрации callback keyboards по времени их жизни
    """
    def __init__(self, ttl_keyboard=5):
        """

        :param ttl_keyboard: время жизни клавиатуры в секундах
        """
        self.ttl_keyboard = ttl_keyboard

    async def __call__(self, callback: CallbackQuery) -> bool:
        """

        :param callback: CallbackQuery
        :return: True, если фильтр пройден
        """
        # Парсим callback на части: payload + data
        date, user_id, data = callback.data.split(':')

        # Проверяем, что клавиатура не устарела, время в секундах
        if (time.time() - float(date)) < self.ttl_keyboard:
            logger.info('IsMessageOutdated was passes')
            # Если прошло меньше времени, возвращаем True, фильтр пройден
            return True
        logger.info('IsMessageOutdated was not passes, the keyboard was outdated')
        return False


@router.callback_query(IsMessageOutdated(ttl_keyboard=10))
async def callback_query_handler(callback: CallbackQuery):
    await callback.answer()
    # Парсим callback на части: payload + data
    date, user_id, data = callback.data.split(':')
    logger.info(f'date {date}, user_id {user_id}, data {data}')
    # Отправляем пользователю ответ в виде callback data в качестве примера
    await callback.message.answer(text=data)
