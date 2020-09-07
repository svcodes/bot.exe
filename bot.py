# obtain proper libraries for hypixel stats and discord.py
import discord
from discord.ext import commands


#initialize discord.py and hypixel api
client = commands.Bot(command_prefix = ".")


#sends a message to the console when the bot is connected
@client.event
async def on_ready():
    print(f"{client.user} is ready!")

@client.command
async def hystats(ctx,mcuser):
    async with aiohttp.ClientSession() as cs:
    async with cs.get('https://api.slothpixel.me/api/players/{mcuser}') as r:
        res = await r.json()  # returns dict
        await ctx.send(res['total_coins'])
    
#basic ping command
@client.command(brief = "Tells you the ping in ms", description = "Tells you the time to connect from idiot.exes pc to the discord server (in ms)")
async def ping(ctx):
    await ctx.send(f"pong! {round(client.latency * 1000, 4)} ms")

#orchestra website command that mentions the sender
@client.command(brief = "links the orchestra website", description = "links the orchestra website")
async def website(ctx):
    await ctx.send(f"{ctx.author.mention} https://sites.google.com/a/roundrockisd.org/round-rock-high-dragon-orchestra/")

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

#links the rrdragonorchestra instagram
@client.command()
async def instagram(ctx):
    await ctx.send(f"{ctx.author.mention} https://instagram.com/rrdragonorchestra")
    

#links the skyleamoe page for a given user
@client.command()
async def sbprof(ctx,mcname):
    await ctx.send(f"https://sky.lea.moe/stats/{mcname}")

#uses hypixel.py to show the rank and network level of a user


@client.event
async def on_message(message):
    if message.content.startswith('$greet'):
        channel = message.channel
        await channel.send('Say hello!')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send('Hello {.author}!'.format(msg))



@client.command()
async def basement(ctx):
    myguild = client.get_guild(733508936216477706)

    basement_role = myguild.get_role(744013188911071362)

    await ctx.author.add_roles(basement_role)

@client.event
async def on_message(message):
    if message.content.startswith('$echo'):
        channel = message.channel
        await channel.send('say something')

        def check (m):
            return m.author != client.user and m.author == message.author

        msg = await client.wait_for('message')
        await channel.send(msg.content)





#uses my api key to run the code and start sending it over to discord
client.run("NzQyODY1MjAyMzAyODEyMzIy.XzMVIQ.eS05opx4x5kVUkT02ownR74iBuQ")
