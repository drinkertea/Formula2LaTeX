from abc import ABC, abstractmethod
from cmath import log
import logging
from typing import Type
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext, Dispatcher, Handler


def startHandler(update: Update, context: CallbackContext):
    update.message.reply_text("Hi!")


def photoHandler(update: Update, context: CallbackContext):
    update.message.reply_text("Got new photo!")
