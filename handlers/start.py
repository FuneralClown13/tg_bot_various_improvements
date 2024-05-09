from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from fake_db import Lexicon, FakeDB
from keyboards import create_simple_keyboard

router = Router()
db = FakeDB()

"""
Обработка команды /start
При старте бота берется его язык системы и выбирается в качестве предпочтительного
Если язык отсутствует в бд, берется английский язык



В данном боте, для примера реализаций эта команда будет отправлять inline keyboard
"""

@router.message(CommandStart())
async def process_command_start(message: Message):
    language_code = db.CACHE.get(f'{message.from_user.id}:language_code', message.from_user.language_code)
    msg = Lexicon().get_translations(language_code)['/start']
    await message.answer(text=msg,
                         reply_markup=create_simple_keyboard(message.from_user.id, language_code))
