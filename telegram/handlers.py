from config import telegram_token_api
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram import types
from aiogram.enums import ChatAction
from aiogram.types import FSInputFile, Message
import os
from youtube.youtube_loader import download_audio_as_mp3
# создаем объект bot
bot = Bot(token=telegram_token_api)
dp = Dispatcher()

@dp.message()
async def convert_url_to_mp3(message: types.Message):
    url = message.text

    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT
    )
    try:
        file_path, title = download_audio_as_mp3(url)
        res = FSInputFile(path = file_path, filename=title)
        await bot.send_audio(message.chat.id, audio=res)
    except Exception as e:
        await message.reply('Произошла ошибка!')
    finally:
    # Удаляем файл после отправки, даже если произошла ошибка
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Файл {file_path} удален после отправки.")