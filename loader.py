from aiogram import Bot, Dispatcher
import config
import logging

from aiogram.utils.exceptions import NetworkError
from requests.exceptions import SSLError
from aiohttp.client_exceptions import ClientConnectorError

try:
    bot = Bot(token=config.TOKEN_BOT, parse_mode="HTML")
    dp = Dispatcher(bot)
    logging.basicConfig(format='----------------\n'
                               u'%(filename)s\n[LINE:%(lineno)d] #%(levelname)-8s\n[%(asctime)s]\n%(message)s',
                        level=logging.INFO, )
except SSLError:
    logging.info(f"SSLError")
except NetworkError:
    logging.info(f"NetworkError")
except ClientConnectorError:
    logging.info(f"ClientConnectorError с NetworkError")
except TimeoutError:
    logging.info(f"TimeoutError")
