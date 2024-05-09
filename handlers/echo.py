from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from fake_db import LEXICON_RU, Lexicon
from keyboards import create_simple_keyboard
from icecream import ic
from cachetools import TTLCache
from loguru import logger

router = Router()
"""
Это хендлеры-заглушки, ловят все сообщения, 
которые не прошли фильтры и отправляют 'пустое' сообщение в ответ
"""

@router.message()
async def process_command_start(message: Message):
    logger.info('echo message')
    await message.answer(text='empty message answer')


@router.callback_query()
async def callback_query_handler(callback: CallbackQuery):
    await callback.answer()
    logger.info('echo callback')
    await callback.message.answer(text='empty callback answer')




