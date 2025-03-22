import discord
from discord.ext import commands
from discord import app_commands
from functions import *



WORLD_CYCLE_DICT = {'duviri':getDuviriCycle,
                    'cetus':getCetusCycle,
                    'earth':getEarthCycle,
                    'cambion':getCambionCycle,
                    'vallis':getVallisCycle,
                    'zariman':getZarimanCycle}

class API(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} Cog loaded')

    async def worldstate_autocomplete(self, ctx: discord.Interaction, current:str)-> list[app_commands.Choice[str]]:
        choices = list(WORLD_CYCLE_DICT.keys())
        return[
            app_commands.Choice(name=choice, value=choice)
            for choice in choices if current.lower() in choice.lower()
        ]
    
    @app_commands.command(name='worldstate', description='get worldstate')
    @app_commands.autocomplete(area=worldstate_autocomplete)
    async def worldstate(self, interaction: discord.Interaction, area: str):
        area = area.casefold()
        worldState = getWorldState()

        if area not in WORLD_CYCLE_DICT.keys():
            await interaction.response.send_message(
                "World state parameter can be: " + ", ".join(WORLD_CYCLE_DICT.keys()),
                ephemeral=True
            )
        else:
            await interaction.response.send_message(WORLD_CYCLE_DICT[area](worldState))

    


    @app_commands.command(name='fissures', description='get current fissures information')
    async def fissures(self, ctx: discord.Interaction, args: str = 'help'):
        worldState = getWorldState()
        msg1 = getFissures(worldState['fissures'], args.split(' ') if args != None else None)
        # await ctx.send(msg1)
        # await ctx.send(msg2)
        await ctx.response.send_message(msg1)

    @app_commands.command(name='sortie', description='get weekly sortie missions')
    async def sortie(self, ctx:discord.Interaction, v: str | None = None):
        worldState = getWorldState()
        msg = getSortie(worldState, True) if v != None else getSortie(worldState)
        await ctx.send(msg)
