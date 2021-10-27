from discord import Embed
from discord.ext.commands import Bot, Context

from discord_slash import SlashCommand, SlashContext, ComponentContext
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle


class TrigoCommand:

    def __init__(self, bot: Bot, slash: SlashCommand):
        self.__bot__ = bot
        self.__slash__ = slash
        self.__name__ = "trigo"

    async def __command__(self, ctx):
        buttons = [
            create_button(style=ButtonStyle.green, label=f"C'est évident !", custom_id="patate"),
            create_button(style=ButtonStyle.red, label=f"Oui, c'est évident...", custom_id="gnagnagna")
        ]
        action_row = create_actionrow(*buttons)
        embed = Embed(
            title=f"Formule de trigonométrie:",
            description=f"*\"Ces formules sont évidentes, elles doivent être connues ou pouvoir être retrouvées en 30 "
                        f"secondes\".* "
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

        @self.__bot__.event
        async def on_component(ctx: ComponentContext):
            await ctx.send(content=f"You selected {ctx.custom_id}")
