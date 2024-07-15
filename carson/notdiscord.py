import discord
from discord.ext import commands
import random
import pyfiglet
import asyncio
import time

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!cm ", intents=intents)

@bot.event
async def on_ready():
    print(f'we have logged in as {bot.user.name}')

@bot.command()
async def hello(ctx):
    await ctx.send('I am running from carsons computer')

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

        await ctx.sent(f"You got sniped! {snipee.mention}", embed=embed)
    else:
        await ctx.send("No message found to snipe in this channel.")
        
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
async def magig8ball(ctx, *, queston: str = None):
    if not queston:
        await ctx.send("Please provide a queston <prefix> <command> <queston>")
        return
    
    responses = [
        "no",
        "yes",
        "maybe",
        "definently",
        "no way"
    ]

    response = random.choice(responses)
    await ctx.send(f'queston: {queston}\n🎱 Answer: {response}')


bot.run('MTA4MDA3MDU1MDM2NzUwNjQ0Mg.GMEJwt.pAwng6lPMgZi-VQMpxmOOLKKA0FFsNLk4wnFQA')