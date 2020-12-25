from time import sleep
from config import ID_USER
from handlers.terminal.log_in_terminal import in_terminal_print
from keyboards.inline.choice_buttons import choice_cancel


def auth(func):
    """Проверка отправителя сообщения. Разрешён только один отправитель."""

    async def wrapper(message):
        if str(message['from']['id']) != ID_USER:
            in_terminal_print(message)
            sleep(3)
            return await message.reply(f"Идентификационные данные не значатся в базе данных!\n\n"
                                       f"Your ID: {message['from']['id']}\n\n"
                                       f"Your First Name: {message['from']['first_name']}\n\n"
                                       f"Your User Name: @{message['from']['username']}\n\n"
                                       f"Your Language: {message['from']['language_code']}", reply=False)
        return await func(message)

    return wrapper


def auth_call(func):
    """Проверка отправителя сообщения. Разрешён только один отправитель."""

    async def wrapper(call, callback_data):
        if str(call['from']['id']) != ID_USER:
            return await call.message.bot.edit_message_text(chat_id=call.message.chat.id,
                                                            message_id=call.message.message_id,
                                                            text=f"Доступ закрыт", reply_markup=choice_cancel)
        return await func(call, callback_data)

    return wrapper
