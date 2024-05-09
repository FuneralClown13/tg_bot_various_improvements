from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from loguru import logger

# Словарь с временем жизни ключа, когда время выходит, ключ удаляется
from fake_db import FakeDB

db = FakeDB()
router = Router()

"""
Реализация троттлинга или удушения

Пользователь получает ключ с временем жизни, 
пока ключ в бд все сообщения пользователя игнорируются
"""

@router.message()
async def message_handler_with_throttling(message: Message):
    """
    Пример использования throttling
    """
    # Получаем id пользователя
    user = message.from_user.id

    # Проверка, есть ли пользователь в словаре
    # Если есть, то его сообщение игнорируется
    if user in db.TTLCACHE:
        logger.info(f'user {user} was THROTTLED ')
        return

    # Если пользователя в словаре нет, то нужно добавить его в словарь
    # Ключ - id пользователя
    # Значение - что угодно, в данном случае тот же id
    db.TTLCACHE[user] = user

    logger.info(f'user {user} said: "{message.text}"')

    # Ответ пользователю
    await message.answer(text=message.text)
