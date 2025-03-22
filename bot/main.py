import discord, os
from discord.ext import commands
from dotenv import load_dotenv
from ordis_bot import OrdisBot


load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
intents = discord.Intents.default()
intents.message_content = True
bot = OrdisBot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.tree.command(name='hello', description='Greetings')
async def hello(interaction: discord.Interaction, arg: str):
    users = arg.split(' ')
    await interaction.response.send_message(f'Hello, {users}!')
    
@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    exit()


bot.run(BOT_TOKEN)