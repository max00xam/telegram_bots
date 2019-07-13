from telethon import TelegramClient, events
import re

api_id = ######
api_hash = "####################################"
token = "############################################"

bot = TelegramClient('hello_world_bot', api_id, api_hash).start(bot_token=token)

@bot.on(events.NewMessage)
async def new_cmd(event):
    if re.search(r'^(?:hi|hello)(?:.\s(.+))?', event.text, re.IGNORECASE):
        await event.respond('Hi, welcome to hello_world_bot.')

def main():
    """Start the bot."""
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()
