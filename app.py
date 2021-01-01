import logging

from aiogram.utils.exceptions import NetworkError
from requests.exceptions import SSLError
from aiohttp.client_exceptions import ClientConnectorError
try:
    if __name__ == '__main__':
        from aiogram import executor
        from handlers import dp

        executor.start_polling(dp)
except SSLError:
    logging.info(f"SSLError")
except NetworkError:
    logging.info(f"NetworkError")
except ClientConnectorError:
    logging.info(f"ClientConnectorError с NetworkError")
except TimeoutError:
    logging.info(f"TimeoutError")