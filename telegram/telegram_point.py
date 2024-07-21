import asyncio
from handlers import dp, bot


# главная функция запуска бота
async def main():
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
   # запускаем в режиме асинхронности
   asyncio.run(main())





