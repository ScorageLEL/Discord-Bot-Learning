import discord
import os
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

token = os.getenv('TOKEN')

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

@bot.command()
async def roll(ctx):
    await ctx.send(random.randint(1,6))

bot.run(token)