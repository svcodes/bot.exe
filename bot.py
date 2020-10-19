# obtain proper libraries for hypixel stats and discord.py
import discord
from discord.ext import commands
import aiohttp
import asyncpraw
import random
import ksoftapi

#initialize stuff
client = commands.Bot(command_prefix = ".")

reddit = asyncpraw.Reddit(client_id="CIwP1eILd2pKNA",
                     client_secret="eEMVLkXCyLD4mXC9QHjDMIWedEI",
                     user_agent="script: Python (by /u/thesumonster)")
client.load_extension("jishaku")

client.session = aiohttp.ClientSession()
kclient = ksoftapi.Client("695cb5adaf19999c1e66774ea03d241fe4f6a3ee")


@client.event
async def on_message(message):
   if message.guild.id == 733508936216477706 and "bye" in message.content.lower():
      await message.add_reaction("\U0001f44b")
   if message.author.id == 743162094710423572:
      await message.add_reaction("\U0001f60b")
   if message.author.id == 348149669899272196 and "." in message.content.lower():
      await message.add_reaction("\U0001f633")
   
   await client.process_commands(message)

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
@gd.command()
async def level(ctx, id: int):
    async with client.session.get(f'https://gdbrowser.com/api/level/{id}') as r:
        res = await r.json()
        embed = discord.Embed(title = f"GD Level: {res['name']}")
        embed.add_field(name="Author", value = res['author'],inline=False)
        embed.add_field(name="Difficulty", value = res['difficulty'],inline=False)
        embed.add_field(name="Downloads", value = res['downloads'],inline=False)
        embed.add_field(name="Stars", value = res['stars'],inline=False)
        embed.add_field(name="Song Name", value = res['songName'],inline=False)
        await ctx.send(embed=embed)

@client.command()
async def mcserver(ctx,ipaddr):
    async with client.session.get(f'https://api.mcsrvstat.us/2/{ipaddr}') as r:
        res = await r.json()
        embed = discord.Embed(title = f"Server Stats for {ipaddr}")
        motdpath = res['motd']['clean']
        if len(motdpath) == 2:
            embed.description = (f"""**MOTD:** 
            {res['motd']['clean'][0]}
            {res['motd']['clean'][1]}
            **Players:** {res['players']['online']}/{res['players']['max']}
            **Version:** {res['version']}""")
        else: 
            embed.description = (f"""**MOTD:** 
            {res['motd']['clean'][0]}
            **Players:** {res['players']['online']}/{res['players']['max']}

            **Version:** {res['version']}""")

      
        await ctx.send(embed=embed)
        
@client.command()
async def coinflip(ctx):
    await ctx.send(f"It's {random.choice(["Heads","Tails"])}!")
    
@client.command()
async def dadjoke(ctx):
    
    async with client.session.get(url='https://icanhazdadjoke.com/slack') as r:
        res = await r.json()
        await ctx.send(res['attachments'][0]['text'])

@client.command()
async def testmeme(ctx):
    meme = await kclient.images.random_meme()
    await ctx.send(meme.image_url)


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
  await pogmessage.add_reaction("\U0001f90f")
                              


#links the skyleamoe page for a given user
@client.command()
async def sbprof(ctx,mcname,profile = None):
    if profile == None:
        await ctx.send(f"https://sky.shiiyu.moe/stats/{mcname}")
    else:
        await ctx.send(f'https://sky.shiiyu.moe/stats/{mcname}/{profile}')

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
