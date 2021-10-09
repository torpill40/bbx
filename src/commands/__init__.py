from .utility import InfoCommand

from discord.ext.commands import Bot

from discord_slash import SlashCommand


def load(bot: Bot, slash: SlashCommand):
    InfoCommand(bot, slash).load()
