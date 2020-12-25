from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

buy_callback = CallbackData("buy", "item_name", "quantity")

choice = InlineKeyboardMarkup(row_width=4)
choice_cancel = InlineKeyboardMarkup(row_width=1)


go_ya = InlineKeyboardButton(text='Yandex', callback_data="buy:ip_ya:yandex")
choice.insert(go_ya)

go_bg = InlineKeyboardButton(text='Beget', callback_data="buy:ip_bg:bg")
choice.insert(go_bg)

go_rm = InlineKeyboardButton(text='Ramziv', callback_data="buy:ip_ra:ramziv")
choice.insert(go_rm)

go_2ip = InlineKeyboardButton(text='2ip', callback_data="buy:ip_2ip:2ip")
choice.insert(go_2ip)

test = InlineKeyboardButton(text='TestButton', callback_data="buy:test:test_name")
choice.insert(test)

cancel = InlineKeyboardButton(text='Cancel', callback_data="cancel")
choice_cancel.insert(cancel)

# go_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text="GO_KEYBOARD")
#         ]
#     ]
# )