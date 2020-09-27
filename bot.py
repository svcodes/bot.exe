# obtain proper libraries for hypixel stats and discord.py
import discord
from discord.ext import commands
import aiohttp
import asyncpraw
import random

#initialize discord.py and hypixel api
client = commands.Bot(command_prefix = ".")

reddit = asyncpraw.Reddit(client_id="CIwP1eILd2pKNA",
                     client_secret="eEMVLkXCyLD4mXC9QHjDMIWedEI",
                     user_agent="script: Python (by /u/thesumonster)")


@client.command()
async def hystats(ctx,mcuser):
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f'https://api.slothpixel.me/api/players/{mcuser}') as r:
            res = await r.json()  # returns dict
            await ctx.send(res['total_coins'])



#sends a message to the console when the bot is connected
@client.event
async def on_ready():
    print(f"{client.user} is ready!")

    
#basic ping command
@client.command(brief = "Tells you the ping in ms", description = "Tells you the time to connect from idiot.exes pc to the discord server (in ms)")
async def ping(ctx):
    await ctx.send(f"pong! {round(client.latency * 1000, 4)} ms")


#funny meme command
@client.command(brief = "haha brrr go brrrr", description = "brrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
async def brr(ctx):
    await ctx.send("https://i.clouds.tf/hys8/7nvo.png")

@client.command()
async def poll(ctx, *, question):
  pogmessage = await ctx.send(f"{ctx.author.name} asks: {question}")
  await pogmessage.add_reaction("\U0001f44d")
  await pogmessage.add_reaction("\U0001f44e")
                              


#links the skyleamoe page for a given user
@client.command()
async def sbprof(ctx,mcname):
    await ctx.send(f"https://sky.lea.moe/stats/{mcname}")

@client.command()
async def meme(ctx):
    memesubs = ["memes","dankmemes"]
    subreddit = await reddit.subreddit(random.choice(memesubs))
    submission = await subreddit.random()
    await ctx.send(submission.url)








#uses my api key to run the code and start sending it over to discord
client.run("NzQyODY1MjAyMzAyODEyMzIy.XzMVIQ.eS05opx4x5kVUkT02ownR74iBuQ")
