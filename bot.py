# obtain proper libraries for hypixel stats and discord.py
import discord
from discord.ext import commands
import aiohttp
import asyncpraw
import random

#initialize stuff
client = commands.Bot(command_prefix = ".")

reddit = asyncpraw.Reddit(client_id="CIwP1eILd2pKNA",
                     client_secret="eEMVLkXCyLD4mXC9QHjDMIWedEI",
                     user_agent="script: Python (by /u/thesumonster)")

client.session = aiohttp.ClientSession()


@client.command()
async def hystats(ctx,mcuser):
        async with client.session.get(f'https://api.slothpixel.me/api/players/{mcuser}') as r:
            res = await r.json()  # returns dict
            await ctx.send(res['total_coins'])

@client.group()
async def gd(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send("Please add a subcommand! (profile, level)")
@gd.command()
async def profile(ctx,username):
        async with client.session.get(url = f'https://gdbrowser.com/api/profile/{username}') as r:
            res = await r.json()
              
            if res == "-1":
                await ctx.send("error! you either entered the name wrong/gdbrowser api is down. try again later")
            else:
                embed = discord.Embed(title = f"GD Stats for {res['username']}")
                embed.set_thumbnail(url = f'https://gdbrowser.com/icon/{username}')
                embed.add_field(name = 'Stars', value = res['stars'], inline=False)
                embed.add_field(name = 'Coins', value = res['coins'],inline=False)
                embed.add_field(name = 'Demons', value = res['demons'],inline=False)
                embed.set_footer(text="All info is obtained from https://gdbrowser.com")
                await ctx.send(embed=embed)

    
@client.command()
async def dadjoke(ctx):
    
    async with client.session.get(url='https://icanhazdadjoke.com/slack') as r:
        res = await r.json()
        await ctx.send(res['attachments']['text'])



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
  pollembed = discord.Embed(title= question, colour = discord.Colour(0x7289da))
  pollembed.set_author(name=f"{ctx.author.name} asks: ")
  pogmessage = await ctx.send(embed=pollembed)
  await pogmessage.add_reaction("\U0001f44d")
  await pogmessage.add_reaction("\U0001f44e")
                              


#links the skyleamoe page for a given user
@client.command()
async def sbprof(ctx,mcname):
    await ctx.send(f"https://sky.lea.moe/stats/{mcname}")

@client.command()
async def meme(ctx):
   postnum = random.randint(1,100)
   subnum = 1 
   sub = await reddit.subreddit("memes").hot(limit=100)
   for submission in sub:
    if subnum == postnum:
      print(submission.url)
    else:
      subnum += 1








#uses my api key to run the code and start sending it over to discord
client.run("NzQyODY1MjAyMzAyODEyMzIy.XzMVIQ.eS05opx4x5kVUkT02ownR74iBuQ")
