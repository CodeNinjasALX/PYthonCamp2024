import discord
from discord.ext import commands
import random
import pyfiglet
import asyncio
import time


intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!zw ", intents=intents)

@bot.event
async def on_ready():
    print(f'we have logged in as {bot.user.name}')
@bot.command()
async def hello(ctx):
    await ctx.send('my compooter is bouta blow')

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
        embed.set_footer(text=f"sniped by {ctx.author}")
        await ctx.send(f"sniped ez {snipee.mention}", embed=embed)
    else:
        await ctx.send("nothing here")


@bot.event
async def on_message_delete(message):
    if message.author.bot: 
        return

    channel_id = str(message.channel.id)
    snipes[channel_id] = {
        'author': message.author.display_name,
        'message': message.content,
        'snipee_id': message.author.id
    }

@bot.command(name='8ball')
async def magic8ball(ctx, *, question: str = None):
    if not question:
        await ctx.send("ask away <prefix> <command> <question>")
        return


    responses = [
        "sigma",
        "sigma",
        "rizz",
        "skibidi",
        "skibidi",
    ]
    response = random.choice(responses)
    await ctx.send(f'question: {question}/n🎱 Answer: {response}')
bot.run('MTA4MDA3MDU1MDM2NzUwNjQ0Mg.GMEJwt.pAwng6lPMgZi-VQMpxmOOLKKA0FFsNLk4wnFQA')


