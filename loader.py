from aiogram import Bot, Dispatcher
import config
import logging

bot = Bot(token=config.TOKEN_BOT, parse_mode="HTML")
dp = Dispatcher(bot)
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.INFO,)