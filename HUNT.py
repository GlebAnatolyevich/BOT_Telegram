import aiohttp
from aiogram import Bot, Dispatcher
from aiogram.utils import executor

import config

bot = Bot(token=config.token,
          proxy='socks5://116.203.53.174:1008',
          proxy_auth=aiohttp.BasicAuth(login='telegram',
                                       password='telegram'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message):
    await bot.send_message(message.chat.id, "Привет, я искуственный интилект Илья!")


if __name__ == '__main__':
    executor.start_polling(dp)
