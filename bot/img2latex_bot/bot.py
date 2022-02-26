
from io import BytesIO
import logging
from typing import Any

import requests

from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


class Img2LatexBot:

    ML_URL = "localhost:8000/predict"

    def __init__(self, token: str) -> None:
        self.updater = Updater(token)
        self._add_handlers()

    @classmethod
    def update_ml_url(cls, url):
        cls.ML_URL = url

    def __call__(self) -> Any:
        self.updater.start_polling()
        self.updater.idle()

    def _add_handlers(self):
        self.updater.dispatcher.add_handler(CommandHandler("help", self.help_handler))
        self.updater.dispatcher.add_handler(MessageHandler(Filters.photo, self.photo_handler))

    @staticmethod
    def help_handler(update: Update, context: CallbackContext):
        update.message.reply_text("Welcome to Image2Latex bot! Send me a picture with fromula and I produce a Latex code for it")

    @staticmethod
    def photo_handler(update: Update, context: CallbackContext):
        update.message.reply_text("Got new image! Processing 🤖")

        file = context.bot.get_file(update.message.photo[-1].file_id)
        f = BytesIO(file.download_as_bytearray())
        files = {"file": f}
        try:
            response = requests.post(Img2LatexBot.ML_URL, files=files)
            latex_code = response.json()["data"]["pred"]
            update.message.reply_text(latex_code)
        except Exception as e:
            logging.error(f"Something bad happens while processing image: {e}")
            update.message.reply_text("Something went wrong 😞\n Please, try later..." )
