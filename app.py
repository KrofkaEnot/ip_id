from aiogram.utils.exceptions import NetworkError
from requests.exceptions import SSLError

from handlers.return_answers import time_date_print

try:
    if __name__ == '__main__':
        from aiogram import executor
        from handlers import dp

        executor.start_polling(dp)
except SSLError:
    print(f"SSLError в {time_date_print()}")
except NetworkError:
    print(f"NetworkError в {time_date_print()}")


# import logging
# from time import sleep, localtime
#
# from aiogram import Bot, Dispatcher, executor, types
# from aiogram.types import CallbackQuery
#
# from aiogram.utils.exceptions import NetworkError
# from requests.exceptions import SSLError
#
# from choice import choice, buy_callback
# from config import TOKEN_BOT, ID_USER
# import ip_ident
# import ip_help
#
# ID_USER_TELEGRAM = ID_USER
# logging.basicConfig(level=logging.INFO)
#
#

#
# def auth(func):
#     """Проверка отправителя сообщения. Разрешён только один отправитель."""
#
#     async def wrapper(message):
#         if str(message['from']['id']) != ID_USER_TELEGRAM:
#             in_terminal_print(message)
#             sleep(3)
#             return await message.reply(f"Ваши идентификационные данные не значатся в нашей базе данных:\n\n"
#                                        f"Your ID: {message['from']['id']}\n\n"
#                                        f"Your First Name: {message['from']['first_name']}\n\n"
#                                        f"Your User Name: {message['from']['username']}\n\n"
#                                        f"Your Language: {message['from']['language_code']}", reply=False)
#         return await func(message)
#
#     return wrapper
#
#
# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     in_terminal_print(message)
#     sleep(2)
#     await message.answer("Информационная система.\n\n"
#                          "(c) @winsys\n\n"
#                          "/ip_help")
#
#
# @dp.message_handler(commands=['ip_help'])
# @auth
# async def send_ip_help(message: types.Message):
#     await message.answer(ip_help.help_ip_commands())
#
#
#
# @dp.message_handler(commands=['ip_ya'])
# @auth
# async def send_ip_ya(message: types.Message):
#     await message.answer(ip_ident.ip_yandex())
#
#
# @dp.message_handler(commands=['ip_bg'])
# @auth
# async def send_ip_bg(message: types.Message):
#     await message.answer(ip_ident.ip_beget())
#
#
# @dp.message_handler(commands=['ip_ra'])
# @auth
# async def send_ip_ra(message: types.Message):
#     await message.answer(ip_ident.ip_ramziv())
#
#
# @dp.message_handler(commands=['ip_2ip'])
# @auth
# async def send_ip_2ip(message: types.Message):
#     await message.answer(ip_ident.ip_2ip())
#
#
#
#
# try:
#     if __name__ == '__main__':
#         executor.start_polling(dp, skip_updates=True)
# except SSLError:
#     print(f"SSLError в {time_date_print()}")
# except NetworkError:
#     print(f"NetworkError в {time_date_print()}")
