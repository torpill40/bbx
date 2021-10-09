import os

from discord import Intents
from discord.ext.commands import Bot

from discord_slash import SlashCommand

from dotenv import load_dotenv

import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


bot = Bot(command_prefix='!', intents=Intents.all())
slash = SlashCommand(bot, sync_commands=True)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


commands.load(bot, slash)


bot.run(TOKEN)
