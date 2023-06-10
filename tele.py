
import telegram
from telegram.ext import Updater, CommandHandler
import asyncio
# Telegram bot token
TOKEN = '5980407331:AAGGSEclyd0RxLCX_opDhyDIU4VuyYqNGC4'

# Chat ID of the user to notify
USER_CHAT_ID = '790629803'

# Create a Telegram bot instance
bot = telegram.Bot(token=TOKEN)


async def call():
    suspect = "captured_frame.jpg"
    await bot.send_photo(chat_id=USER_CHAT_ID, photo=open(suspect, 'rb'))
    await bot.send_message(chat_id=USER_CHAT_ID, text='WARNING!!! Intruder Detected in your vehicle.')
    
if __name__ == '__main__':
    asyncio.run(call())
    



