import discord
from discord.ext import commands
import random
import pyfiglet
import asyncio
import time

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!cp ", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user.name}')

@bot.command()
async def hello(ctx):
    await ctx.send('I am running from cadens computer and I need help')

snipes = { 
    
}

@bot.command()
async def snipe(ctx):
    channel_id = str(ctx.channel.id)

    if channel_id in snipes:
        message_content = snipes[channel_id]['message']
        snipee = await bot.fetch_user(snipes[channel_id]['snipee_id'])
    
        embed = discord.Embed(
           description=f"{message_content}"
        )
        embed.set_author(name=f"{snipee}")
        embed.set_footer(text=f"Sniped by {ctx.author}")
        
        await ctx.send(f"you got sniped! {snipee.mention}", embed=embed)
    else:
        await ctx.send("No message found to snipe in this channel.")

@bot.event
async def on_messege_delete(message):
    if message.author.bot:
        return

    # Store the sniped messages in the dictionary
    channel_id = str(message.channel.id)
    snipes[channel_id] = {
        'author': message.author.display_name,
        'message': message.content,
        'snipee_id': message.author.id
    }

@bot.command()
async def magic8ball(ctx, *, question: str = None):
    if not question:
        await ctx.send("Please provide a question <prefix> <command> <question>")
        return

    responses = [
         "yes",
         "no",
         "maybe",
         "undeniable",
         "doubtfull",
    ]

responses = random.choice(responses)
await ctx.send(f'Question: {question}/n Answer: {responses}')



bot.run('MTA4MDA3MDU1MDM2NzUwNjQ0Mg.GMEJwt.pAwng6lPMgZi-VQMpxmOOLKKA0FFsNLk4wnFQA')