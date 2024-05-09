from .lexicon_ru import LEXICON_RU
from .lexicon_en import LEXICON_EN


class Lexicon:
    """
    Класс-синглтон для доступа к словарям локализации
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.__lexicon = {
            'ru': LEXICON_RU,
            'en': LEXICON_EN,
        }

    def get_translations(self, language_code):
        return self.__lexicon.get(language_code, LEXICON_EN)
