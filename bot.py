import logging
from generator import *
from io import BytesIO
from aiogram import Bot, Dispatcher, executor, types
from PIL import Image
import numpy as np
from aiogram.types.input_file import InputFile
from io import BytesIO
API_TOKEN = 'your token'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends /start or /help command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

path = 'E:\\ggggg.jpg'

@dp.message_handler(content_types=['photo'])
async def photo_handler(message):
    
    bytes = BytesIO()
    await message.photo[-1].download(bytes)
    text = Image_To_Text(bytes)
    bytes.seek(0)
    Text_To_Image_by_text(bytes, text)
    bytes.seek(0)
    await bot.send_photo(message.from_user.id, InputFile(bytes)) 



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

