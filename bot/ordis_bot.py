from discord.ext import commands
from api import API

class OrdisBot(commands.Bot):
    async def setup_hook(self):
        await self.add_cog(API(self))
        

