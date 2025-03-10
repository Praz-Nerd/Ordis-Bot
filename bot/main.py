import discord, os
from discord.ext import commands
from dotenv import load_dotenv
from api import API


# worldState = functions.getWorldState()
# print(functions.getDuviriCycle(worldState['duviriCycle']))

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.add_cog(API(bot))

@bot.command()
async def hello(ctx, arg = 'user'):
    await ctx.send(f'Hello, {arg}!')

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    exit()

#api.bind(bot)
bot.run(BOT_TOKEN)

