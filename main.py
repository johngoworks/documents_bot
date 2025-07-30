import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN
from data_manager import SecureDataManager

# Настройка логирования (без персональных данных)
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Глобальные объекты
data_manager = SecureDataManager()
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


async def cleanup_task():
    """Фоновая задача очистки"""
    while True:
        try:
            data_manager.cleanup_expired_sessions()
            await asyncio.sleep(1800)  # 30 минут
        except Exception as e:
            logger.error(f"Cleanup task error: {e}")
            await asyncio.sleep(300)  # 5 минут при ошибке


async def main():
    """Главная функция"""
    logger.info("Starting DocBot...")

    # Запускаем фоновую очистку
    cleanup_task_handle = asyncio.create_task(cleanup_task())

    try:
        # Регистрация роутеров
        from handlers.onboarding import onboarding_router
        from handlers.stamp_transfer import stamp_transfer_router
        from handlers.main_menu import main_menu
        from handlers.select_region_and_mvd import select_region_router
        from handlers.passport_manual import passport_manual_router

        dp.include_router(main_menu)
        dp.include_router(onboarding_router)
        dp.include_router(stamp_transfer_router)
        dp.include_router(select_region_router)
        dp.include_router(passport_manual_router)

        await dp.start_polling(bot)
    finally:
        cleanup_task_handle.cancel()
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
