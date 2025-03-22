from discord.ext import commands
from api import API

class OrdisBot(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)

    async def setup_hook(self):
        await self.add_cog(API(self))
        list = await self.tree.sync(guild=None)
        print(f'Synced commnads:{len(list)}')
        

