import os

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

import rain_api


load_dotenv()
bot = Bot(os.getenv("TELEGRAM_TOKEN"))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm RainBot!\nPowered by aiogram.")


@dp.message_handler()
async def send_clouds(message: types.Message):
    await message.answer(message.text)
    rain_api.get_clouds_image()
    with open('media/clouds/now.gif', 'rb') as clouds:
        await message.answer_document(clouds)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
