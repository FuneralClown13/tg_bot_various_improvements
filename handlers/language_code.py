from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from loguru import logger
from fake_db import FakeDB

db = FakeDB()
router = Router()

"""
хэндлеры для команд /ru & /en
выбор локализации
"""


@router.message(Command(commands='ru'))
async def message_handler_shadow_ban(message: Message):
    """
    Ловим команду /ru, записываем в бд
    :param message: Message
    """
    db.CACHE[f'{message.from_user.id}:language_code'] = 'ru'
    msg = f'set language_code ru for {message.from_user.id}'
    logger.info(msg)
    await message.answer(text=msg)


@router.message(Command(commands='en'))
async def message_handler_shadow_ban(message: Message):
    """
    Ловим команду /en, записываем в бд
    :param message: Message
    """
    db.CACHE[f'{message.from_user.id}:language_code'] = 'en'
    msg = f'set language_code en for {message.from_user.id}'
    logger.info(msg)
    await message.answer(text=msg)
