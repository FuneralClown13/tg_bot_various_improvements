import os
import dotenv
from dataclasses import dataclass


@dataclass
class Bot:
    # Токен для доступа к телеграм-боту
    token: str


@dataclass
class Config:
    bot: Bot


def load_config() -> Config:
    """
    Загрузка конфига
    :return: экземпляр класса Config
    """
    dotenv.load_dotenv()
    bot_token = os.getenv('BOT_TOKEN')
    return Config(bot=Bot(token=bot_token))
