from loader import bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage


async def on_shutdown(dp):
    await bot.close()


if __name__ == '__main__':
    storage = MemoryStorage()
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_shutdown=on_shutdown)