import logging
from gtts import gTTS
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher as OldDispatcher
from dotenv import load_dotenv
import os

load_dotenv()

API_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = OldDispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Салам!\nМен ЭхоБот!\nКызматкерлик аркылу айып келди.")


@dp.message_handler()
async def echo(message: types.Message):
    tts = gTTS(message.text, lang='ru')  # Используем русский язык в gTTS
    tts.save(f'{message.from_user.id}.mp3')

    # Отправляем аудио-сообщение через метод send_audio
    with open(f'{message.from_user.id}.mp3', 'rb') as voice:
        await bot.send_audio(message.chat.id, voice)


if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
