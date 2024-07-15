import discord
from discord.ext import commands
import random
import pyfiglet
import asyncio
import time

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!oyoy ", intents=intents)

@bot.event
async def on_ready():
    print(f'we have logged in as) {bot.user.name}')


@bot.command()
async def hello(ctx):
        await ctx.send('i am running from bobs computer')

snipes = {
      
}

@bot.command()
async def snipe(ctx):
    channel_id = str(ctx.channel.id)

    if channel_id in snipes:
        message_content = snipes[channel_id]['message']
        snipee = await bot.fetch_user(snipes[channel_id]['snipee_id'])


        embed = discord.embed(
            discription=f"{message_content}"
        )
        embed.set_author(name=f"{snipee}")
        embed.set_author(text=f"snped by {ctx.author}")

        await ctx.send(f"you got sniped! {snipee.mention}")
    else:
        await ctx.send("no message found to snipe this channel.")


@bot.event()
async def on_message_delete(message):
    if message.author.bot:
        return

    channel_id = str(message.channel.id)
    snipes[channel_id] = {
        'authour': message.author.display_name,
        'message': message.content,
        'snipe_id': message.authot.id,
    }

    channel_id = str(message.channel.id)

@bot.command(name+'8ball')
async def magic8ball(ctx, *, question: str None):
    if not question:
        await ctx.send("plz provide a question <prefix> <command> <question>")
        return
    
    responses = [
        "no"
        "no"
        "yes"
        "mabye"

    ]
    
response = random.random(respsonses)
await ctx.send(f'Question: {question}/n Answer: {response}')

bot.run('MTA4MDA3MDU1MDM2NzUwNjQ0Mg.GMEJwt.pAwng6lPMgZi-VQMpxmOOLKKA0FFsNLk4wnFQA')

