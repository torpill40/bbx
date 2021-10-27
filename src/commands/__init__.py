from .utility import InfoCommand
from .maths import TrigoCommand

from discord.ext.commands import Bot

from discord_slash import SlashCommand


def load(bot: Bot, slash: SlashCommand):
    InfoCommand(bot, slash).load()
    TrigoCommand(bot, slash).load()
