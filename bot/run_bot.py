import logging
import os
from typing import Any
from dotenv import load_dotenv

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from img2latex_bot.handlers import startHandler, photoHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Img2LatexBot:
    def __init__(self, token: str) -> None:
        self.updater = Updater(token)
        self.add_handlers()

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.updater.start_polling()
        self.updater.idle()

    def add_handlers(self):
        self.updater.dispatcher.add_handler(CommandHandler("start", startHandler))
        self.updater.dispatcher.add_handler(MessageHandler(Filters.photo, photoHandler))


if __name__ == "__main__":
    load_dotenv()
    TOKEN = os.getenv("TOKEN")
    bot = Img2LatexBot(TOKEN)
    bot()
