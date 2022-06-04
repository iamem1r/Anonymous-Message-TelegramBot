import os

import telebot
from loguru import logger
from setuptools import Command

from src.constants import keyboard
from src.utils.io import write_json

bot_token = os.environ["ANONYMOUS_BOT"]

class Bot:
    """Template for telegram bot.
    """
    def __init__(self):
        self.bot = telebot.TeleBot(bot_token)
        self.echo_all = self.bot.message_handler(func=lambda m: True)(self.echo_all)

    def echo_all(self, message):
        # write_json(message.json, "message.json")
        self.bot.send_message(
            message.chat.id,
            text=message.text,
            reply_markup=keyboard.main)


    def run(self,):
        logger.info("Bot is running...")
        self.bot.infinity_polling()



if __name__ == "__main__":
    logger.info("Bot Started...")
    bot = Bot()
    bot.run()
