from time import sleep
from aiogram import types
from aiogram.types import CallbackQuery

from handlers.ip import ip_ident
from handlers.return_answers import time_date_print
from handlers.terminal.log_in_terminal import in_terminal_print
from handlers.users.auth import auth, auth_call
from keyboards.inline.choice_buttons import buy_callback, choice
from loader import dp
import logging


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    in_terminal_print(message)
    sleep(2)
    await message.answer("Информационная система"
                         " управления доступом.\n\n"
                         "(c) @winsys\n\n"
                         "/ip_help")


@dp.message_handler(commands=['ip_help'])
@auth
async def speak_go(message):
    in_terminal_print(message)
    logging.info(f"call = {message}")
    await message.answer(text=f"{time_date_print()}", reply_markup=choice)


# @dp.callback_query_handler(buy_callback.filter(item_name="test"))
# @auth_call
# async def test_def(call: CallbackQuery, callback_data: dict):
#     print(f'{time_date_print()}')
#     logging.info(call)


@dp.callback_query_handler(buy_callback.filter(item_name="ip_ya"))
@auth_call
async def handlers_yandex(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    quantity = callback_data.get("quantity")
    logging.info(f"Запрос: {call.from_user}")
    await call.message.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                             text=f"По результатам {quantity} ответ {ip_ident.ip_yandex()}",
                                             reply_markup=choice)


@dp.callback_query_handler(buy_callback.filter(item_name="ip_bg"))
@auth_call
async def handlers_beget(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    quantity = callback_data.get("quantity")
    logging.info(f"Запрос: {call.from_user}")
    await call.message.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                             text=f"По результатам {quantity} ответ {ip_ident.ip_beget()}",
                                             reply_markup=choice)


@dp.callback_query_handler(buy_callback.filter(item_name="ip_ra"))
@auth_call
async def handlers_remziv(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    quantity = callback_data.get("quantity")
    logging.info(f"Запрос: {call.from_user}")
    await call.message.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                             text=f"По результатам {quantity} ответ {ip_ident.ip_ramziv()}",
                                             reply_markup=choice)


@dp.callback_query_handler(buy_callback.filter(item_name="ip_2ip"))
@auth_call
async def handlers_2ip(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    quantity = callback_data.get("quantity")
    logging.info(f"Запрос: {call.from_user}")
    await call.message.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                             text=f"По результатам {quantity} ответ {ip_ident.ip_2ip()}",
                                             reply_markup=choice)


@dp.callback_query_handler(text='cancel')
async def cancel_buying(call: CallbackQuery):
    logging.info(f"Запрос: {call.from_user}")
    await call.answer("Доступ ограничен, пардонте!", show_alert=True)
    await call.message.edit_reply_markup()
