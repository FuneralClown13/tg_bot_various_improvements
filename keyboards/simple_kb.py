from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from fake_db import Lexicon
from time import time

def create_simple_keyboard(user_id, language_code) -> InlineKeyboardMarkup:
    payload = f'{time()}:{user_id}'
    buttons = {
        f'{payload}:btn1': Lexicon().get_translations(language_code)['btn1'],
        f'{payload}:btn2': Lexicon().get_translations(language_code)['btn2'],
        f'{payload}:btn3': Lexicon().get_translations(language_code)['btn3'],

    }
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Добавляем в билдер ряд с кнопками
    for data, text in buttons.items():
        kb_builder.row(InlineKeyboardButton(
            text=text,
            callback_data=data))

    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()
