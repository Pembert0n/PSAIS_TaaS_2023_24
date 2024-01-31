import discord
from discord.ext import commands

bot_prefix = '/'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=bot_prefix, intents=intents)

@bot.event
async def on_ready():
    print(f'Bot gestartet: {bot.user.name} ({bot.user.id})')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command(name='team')
async def ping(ctx):
    await ctx.send('Bei diesem Project haben Authanh Duong, Suphi Pembe und Nils Thieringer mitgearbeitet.')

@bot.command(name='ask')
async def ping(ctx):
    await ctx.send('Aktuell besteht keine Verbingung zu den Podcastdaten. Bitte versuche es später erneut, oder wende dich an einen Entwickler.')

@bot.command(name='summarize')
async def ping(ctx):
    await ctx.send('Aktuell besteht keine Verbingung zu den Podcastdaten. Bitte versuche es später erneut, oder wende dich an einen Entwickler.')

@bot.command(name='search')
async def ping(ctx):
    await ctx.send('Aktuell besteht keine Verbingung zu den Podcastdaten. Bitte versuche es später erneut, oder wende dich an einen Entwickler.')




@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the TaaS Testserver!'
    )

bot.run("MTE5NDY2NjM4OTgxOTEwMTIwNA.GuWZHz.9Hh8g5WDsxGchYBZ2oQ_1EcnjgQM4EqYAx1XfE")
