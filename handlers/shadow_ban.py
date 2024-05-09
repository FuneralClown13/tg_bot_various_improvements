from aiogram import Router, F
from aiogram.filters import CommandStart, Command, BaseFilter
from aiogram.types import Message, CallbackQuery
from loguru import logger
from fake_db import FakeDB

db = FakeDB()
router = Router()
"""
Реализация shadow ban
"""


@router.message(Command(commands='ban'))
async def message_handler_shadow_ban(message: Message):
    """
    Ловим команду /ban, баним по id
    Теперь все его сообщения НЕ могут пройти в следующие роутеры и хендлеры
    :param message: Message
    """
    # Добавляем в бд user id
    db.CACHE[message.from_user.id] = 'ban'
    logger.info(db.CACHE)
    msg = f'{message.from_user.id} was banned'
    logger.info(msg)
    # Сообщаем ему радостную новость
    await message.answer(text=msg)


@router.message(Command(commands='unban'))
async def message_handler_shadow_ban(message: Message):
    """
    Ловим команду /unban, удаляем пользователя из списка забаненных
    Теперь все его сообщения могут пройти в следующие роутеры и хендлеры
    :param message: Message
    """
    # Удаляем пользователя из бд
    db.CACHE.pop(message.from_user.id)
    msg = f'{message.from_user.id} was unbanned'
    logger.info(msg)
    await message.answer(text=msg)


class IsBanned(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in db.CACHE


@router.message(IsBanned())
async def message_handler_shadow_ban(message: Message):
    logger.info('message_shadow_ban')
    return
