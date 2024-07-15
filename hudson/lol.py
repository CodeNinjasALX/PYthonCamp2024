import discord 
from discord.ext import commands
import random
import asyncio
import time

intents = discord.Intents.all() 

bot = commands.Bot(command_prefix= "!hb ", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as{bot.user.name}')

@bot.command()
async def hello(ctx):
    await ctx.send('I am Running from my computer ')


snips = {
}

@bot.command()
async def snipe(ctx):
    channel_id =str(ctx.channel.id)

    if channel_id in snips:
        message_content = snipes[chnnel_id]['message']
        snipee = await bot.fetch_user(snips[chnnel_id]['snipee_id'])

        embed =discord.Embed(
        description=f"{message_content}"
   )
    embed.set_author(name=f"{snipee}")
    embed.set_footer(text=f"snipet by{ctx.author}")
else:

@bot.event()
async def on_message_delete(message):
    if message.author.bot:
        return

        channel_id = str(massage.channel.id)
        snips[channel_id] ={
        
        }

@bot.command(name= '8ball')
async def magic8ball(ctx, *, question: str = None):
    if not question:
        await ctx.sand("please provid a queston <prefics> <comand> <ques>")

bot.run('MTA4MDA3MDU1MDM2NzUwNjQ0Mg.GMEJwt.pAwng6lPMgZi-VQMpxmOOLKKA0FFsNLk4wnFQA')
    
