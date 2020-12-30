from aiogram import Bot, Dispatcher
import config
import logging

bot = Bot(token=config.TOKEN_BOT, parse_mode="HTML")
dp = Dispatcher(bot)
logging.basicConfig(format='----------------\n'
                           u'%(filename)s\n[LINE:%(lineno)d] #%(levelname)-8s\n[%(asctime)s]\n%(message)s',
                    level=logging.INFO,)
