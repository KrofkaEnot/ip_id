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
