import logging
import time

from telebot import TeleBot
from telebot.types import Message

from django.conf import settings
# from django.core.management import BaseCommand
from django.core.management.base import BaseCommand
from django.utils import timezone

from webbolid.models import Plist

# =============== Enable logging  ==============================
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("start bot")

bot = TeleBot(settings.BOT_TOKEN, threaded=False)


@bot.message_handler(commands=['start', 'help', 'cancel'])
def handle_user_without_verification(msg: Message):
    bot.send_message(
        msg.chat.id,
        'Добро пожаловать!\n'
    )


@bot.message_handler(commands=['plist'])
def get_plist(msg: Message):
    plist = Plist.objects.all()
    bot.send_message(msg.chat.id, f'{plist}')
    # logger.info(plist)
    # time.sleep(15)


class Command(BaseCommand):
    help = "run bot"

    def handle(self, *args, **options):
        bot.polling()

# class Command(BaseCommand):
#     help = 'Displays current time'
#
#     def handle(self, *args, **kwargs):
#         time = timezone.now().strftime('%X')
#         self.stdout.write("It's now %s" % time)
