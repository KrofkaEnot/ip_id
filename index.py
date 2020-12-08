import logging
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_BOT, ID_USER_TELEGRAM
import ip_ident
import ip_help

API_TOKEN = TOKEN_BOT
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def auth(func):
    """Проверка отправителя сообщения. Разрешён только один отправитель."""

    async def wrapper(message):
        if message['from']['id'] != ID_USER_TELEGRAM:
            return await message.reply("Доступ запрещён", reply=False)
        return await func(message)

    return wrapper


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Информационно аналитическая система\n"
                         "управления доступом.\n\n"
                         "Поддержка осущевствляется @winsys\n\n"
                         "/ip_help")


@dp.message_handler(commands=['ip_help'])
@auth
async def send_welcome(message: types.Message):
    await message.answer(ip_help.help_ip_commands())


@dp.message_handler(commands=['ip_ya'])
@auth
async def send_welcome(message: types.Message):
    await message.answer(ip_ident.ip_yandex())


@dp.message_handler(commands=['ip_bg'])
@auth
async def send_welcome(message: types.Message):
    await message.answer(ip_ident.ip_beget())


@dp.message_handler(commands=['ip_ra'])
@auth
async def send_welcome(message: types.Message):
    await message.answer(ip_ident.ip_ramziv())


@dp.message_handler(commands=['ip_2ip'])
@auth
async def send_welcome(message: types.Message):
    await message.answer(ip_ident.ip_2ip())


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    await bot.send_message(message.chat.id, 'Команда ' + message.text + ' мне не знакома.')
    # await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
