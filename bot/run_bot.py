import logging
import os

from dotenv import load_dotenv

from img2latex_bot.bot import Img2LatexBot


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    load_dotenv()
    TOKEN = os.getenv("TOKEN", "")
    ML_URL = os.getenv("ML_URL", "")
    bot = Img2LatexBot(TOKEN)
    if ML_URL:
        bot.update_ml_url(ML_URL)
    bot()
