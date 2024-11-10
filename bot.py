import logging

import wikipedia

import wikitest
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '7709399152:AAFSxU6hs1lJiY25-aJgoH_o8NRZXa-MJFM'
wikipedia.set_lang('uz')
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Wikipidia botiga xush kelibsiz!")


@dp.message_handler()
async def sendwiki(message: types.Message):
    try:
        respoond = wikipedia.summary(message.text)
        await message.answer(respoond)

    except:
        await message.answer("Bu mavzuga doir hech narsa topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
