from aiogram import Bot, Dispatcher, executor, types
from aiogram import *
from aiogram.types import *
import logging


logging.basicConfig(level=logging.INFO)
TOKEN = "1566152078:AAFn5Gy6C4tDvQwp-vHrQmHAdsC73PuNgVg"
admin_id = 959339948

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    if message['from'].id == admin_id:
        await message.answer(f"Hi, admin")
    else:
        await message.answer(f"Привет, {message['from'].first_name}!")


@dp.message_handler()
async def process_start_command(message: types.Message):
    if message.reply_to_message == None:
        if '/start' not in message.text:
            await bot.forward_message(admin_id, message.from_user.id, message.message_id)
    else:
        if message['from'].id == admin_id:
            if message.reply_to_message.forward_from.id:
                await bot.send_message(message.reply_to_message.forward_from.id, message.text)
        else:
            await message.answer('Нельзя отвечать на сообщения.')


@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(message):
    await bot.forward_message(admin_id, message.from_user.id, message.message_id)


@dp.message_handler(content_types=['document'])
async def handle_docs_photo(message):
    await bot.forward_message(admin_id, message.from_user.id, message.message_id)

if __name__ == '__main__':
    print("starting")
executor.start_polling(dp)