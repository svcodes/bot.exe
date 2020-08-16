# obtain proper libraries for hypixel stats and discord.py
import discord
from discord.ext import commands
import hypixel

#initialize discord.py and hypixel api
client = commands.Bot(command_prefix = ".")
API_KEYS = ['HYPIXEL API KEY GOES HERE']
hypixel.setKeys(API_KEYS)

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

#tells you if you have nitro idk why i made this
@client.command()
async def nitro(ctx):
    user = ctx.author
    
    if user.premium_since == None:
        await ctx.send("you do not have nitro")
    else:
        await ctx.send("you have nitro")

#links the skyleamoe page for a given user
@client.command()
async def sbprof(ctx,mcname):
    await ctx.send(f"https://sky.lea.moe/stats/{mcname}")

#uses hypixel.py to show the rank and network level of a user
@client.command()
async def hystats(ctx,mcuser):
    Player = hypixel.Player(mcuser)
    HYPlayerName = Player.getName()
    HYPlayerRank = Player.getRank()
    HYPlayerLevel = Player.getLevel()
    infotosend = f"""
    {HYPlayerName} has the rank of {HYPlayerRank['rank']}
    The level of {HYPlayerName} is {round(HYPlayerLevel,0)}
    """ 
    await ctx.send(infotosend)   

#uses my bot token to run the code and start sending it over to discord
client.run("DISCORD BOT TOKEN GOES HERE")
