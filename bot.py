import discord
from discord.ext import commands

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print(f"{client.user} is ready!")

@client.command(brief = "Tells you the ping in ms", description = "Tells you the time to connect from idiot.exes pc to the discord server (in ms)")
async def ping(ctx):
    await ctx.send(f"pong! {round(client.latency * 1000, 4)} ms")

@client.command(brief = "links the orchestra website", description = "links the orchestra website")
async def website(ctx):
    await ctx.send(f"{ctx.author.mention} https://sites.google.com/a/roundrockisd.org/round-rock-high-dragon-orchestra/")

@client.command(brief = "haha brrr go brrrr", description = "brrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
async def brr(ctx):
    await ctx.send("https://i.clouds.tf/hys8/7nvo.png")

@client.command()
async def nitro(ctx):
    user = ctx.author
    
    if user.premium_since == None:
        await ctx.send("you do not have nitro")
    else:
        await ctx.send("you have nitro")

client.run("TOKEN HERE")
