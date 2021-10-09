from discord import Embed
from discord.ext.commands import Bot, Context

from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle


class InfoCommand:

    def __init__(self, bot: Bot, slash: SlashCommand):
        self.__bot__ = bot
        self.__slash__ = slash
        self.__name__ = "info"

    async def __command__(self, ctx):
        buttons = [
            create_button(style=ButtonStyle.green, label="A green button"),
            create_button(style=ButtonStyle.blue, label="A blue button")
        ]
        action_row = create_actionrow(*buttons)
        embed = Embed(
            title=f"{ctx.bot.user.name}:",
            description="*L'évidence est une évidence.*"
        )
        await ctx.send(embed=embed, components=[action_row])

    def load(self):
        @self.__slash__.slash(name=self.__name__)
        async def info_slash(ctx: SlashContext):
            await self.__command__(ctx)

        @self.__bot__.command(name=self.__name__)
        async def info(ctx: Context):
            await self.__command__(ctx)
            await ctx.message.delete()
