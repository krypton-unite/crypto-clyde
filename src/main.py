import discord
# settings.py
from dotenv import load_dotenv
# OR, explicitly providing path to '.env'
from pathlib import Path  # Python 3.6+ only
import os

load_dotenv(dotenv_path=Path(__file__).parent.joinpath('.env'))

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run(os.getenv("DISCORD_BOT_TOKEN"))
