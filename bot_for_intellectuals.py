import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Bot is running')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

bot.run('MTAyNzAxNjM2MTU1MTA4OTY2NA.GCs8sR.76nTEaTRwUgzfeY7KDqitk12zF5DK2yBdbZttU')