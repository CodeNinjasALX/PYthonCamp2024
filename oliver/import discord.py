import discord
from discord.ext import commands
import random
import pyfiglet
import asyncio
import time

intents = discord.Intent.all()
bot = commands.bot(command_prefix="!ml ", intents=intents)

@bot.event
async def on_ready():
    print(f'we have logged in as) {bot.user.name}')

bot.run('MTA4MDA3MDU1MDM2NzUwNjQ0Mg.GMEJwt.pAwng6lPMgZi-VQMpxmOOLKKA0FFsNLk4wnFQA')