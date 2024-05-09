import asyncio
from aiogram import Bot, Dispatcher
from loguru import logger
from config import Config, load_config
from handlers import echo, throttling, shadow_ban, start, language_code, callback_query_filter


# Функция конфигурирования и запуска бота
async def main():
    logger.info('Запуск бота')
    # Загружаем конфиг в переменную config
    config: Config = load_config()
    logger.info('Конфиг загружен')
    # Инициализируем бот и диспетчер
    bot = Bot(token=config.bot.token)
    logger.info('Инициализирован bot')
    # dispatcher - главный роутер
    dp = Dispatcher()
    logger.info('Инициализирован dispatcher')

    # Регистрируем роутеры
    dp.include_router(start.router)
    dp.include_router(shadow_ban.router)
    dp.include_router(language_code.router)

    dp.include_router(throttling.router)

    dp.include_router(callback_query_filter.router)

    dp.include_router(echo.router)
    logger.info('Роутеры зарегистрированы')

    # Пропускаем накопившиеся апдейты
    await bot.delete_webhook(drop_pending_updates=True)
    logger.info('Апдейты пропущены')
    #  и запускаем polling
    logger.info('Бот запущен')
    await dp.start_polling(bot)




if __name__ == '__main__':
    asyncio.run(main())
