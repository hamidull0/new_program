from aiogram import executor, types, Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage


BOT_TOKEN = "6632162742:AAHSKV2q9HJO5Lm1oVR28CJpEypRLz4L-hA"
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Assalomu alaykum")


@dp.message_handler(commands="help")
async def start(message: types.Message):
    await message.answer("Operator bilan bog'lanish uchun ....")


@dp.message_handler(commands="number")
async def start(message: types.Message):
    await message.answer("Nomer: 94 653 53 15")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)