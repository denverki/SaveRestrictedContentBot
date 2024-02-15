#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 18910664
API_HASH = "3884d9cc5d521bb478f5bc8b8ccbec33"
BOT_TOKEN = "6351561304:AAHWhXB9lHfw-R6B4tSxyaw-EE5PaTBoxsw"
SESSION = "BQEgjcgAMuLPOwebYJRR4TkXYaiY8t8uQQvn2jFxbqR-TfD03GRuYb8P3XYPoF06Tkp50JQQgOu9xW2up_DELs-po39NYHvNyjjJ_d8W_pqSgV9EksBtWrI8aSBZZfJoKdBLOxxwBxiEwCHdzS2hhMnuRC9N969u1tfAon660CiquJkY5fHjlyJIWqZP0PfFe9kZMbJLFkuwYLFdA2gsHIcV2hEprYvcVXcSZd88BZtnZfM6Wns40vXpcyUGQh2oCcvG7SDG0WBwozjn0p9Tuk4nZ5DK0fHdaxO6g8ndwdB6O_qrd9ufoxqhX0V8rKxvIpRMCEMqNw09jH6ZS4Dd9KYr7mPBMgAAAAAksN1QAA"
FORCESUB = "saverrre"
AUTH = 615570768
bot = "@Seex_mexfexbot"
userbot = "@Seex_mexfexbot"
try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
