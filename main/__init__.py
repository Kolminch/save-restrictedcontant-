#ChauhanMahesh/Vasusen/DroneBots/COL

import sys, time, logging
from decouple import config
from telethon import TelegramClient
from telethon.sessions import StringSession

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Basics
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
SESSION = config("SESSION", default=None)

client = TelegramClient(StringSession(SESSION) , APP_ID, API_HASH)
try:
    client.start()
except BaseException:
    print("Userbot Error ! Have you added a STRING_SESSION in deploying??")
    sys.exit(1)

Drone = TelegramClient('Drone', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
