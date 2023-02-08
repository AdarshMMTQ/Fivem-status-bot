import os
import discord
import asyncio
import time
import requests as rq
from discord.ext import commands
from discord.ext import tasks

## Setup
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = commands.Bot(command_prefix=['-'], intents=intents)
client.remove_command('help')

## Config
class config:
    serverIP = "127.0.0.1:30120" #IP:PORT | Example: 21.98.336.41:30120 | Use 127.0.0.1:PORT if you're running it on same Server as FiveM Server.
    guildID =  #Your Discord Server ID, must be int. | Example: 721939142455459902
    Token = "" #Your Discord Bot Token

## Events
@client.event
async def on_ready():
    print(f'\nLogged as: {client.user.name} - {client.user.id}\nConnected to:')
    for i in client.guilds:
        print(
        f'{i}'
        )
    print('Bot Is Ready!')
    client.my_current_task = live_status.start()

## Players Count Function // Callable Everywhere, returns number
def pc():
    try:
        resp = rq.get('http://'+config.serverIP+'/players.json').json()
        return(len(resp))
    except:
        return('N/A')

## Say Commands
@client.command(pass_content=True, aliases=['s'])
@commands.has_permissions(administrator=True) 
async def say(ctx, *, text):
    
    try:
        await ctx.message.delete()
        timenow = time.strftime("%H:%M")
        embed=discord.Embed(title=" Bot", description=" ", color=0xfff705)
        embed.set_author(name="Bot", url="", icon_url="")#enter your icon url
        embed.set_thumbnail(url=ctx.author.avatar.url)
        embed.add_field(name="Message:", value=text, inline=False)
        embed.set_footer(text=f"{ctx.message.author} |  FiveM Bot | {timenow}")
        await ctx.send(embed=embed)
    except Exception as err:
        print(err)
    
@client.command(pass_context=True, aliases=['hs'])
@commands.has_permissions(administrator=True) 
async def hsay(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(text)

## Players Lookup
@client.command(aliases=['playerid', 'loid', 'server'])
@commands.has_permissions(administrator=True) 
async def pid(ctx, pids):
    
    if not pid:
        await ctx.send('<@{}>, Please Specify A In-Game Player ID!')
        return
    resp = rq.get('http://'+config.serverIP+'/players.json')
    for _ in resp.json():
        if _['id'] == int(pids):
            pembed = discord.Embed(title='PlayerID Query Seccessful!', color=discord.Color.dark_green())
            pembed.add_field(name='Steam Name : {}\nIn-Game ID : {}'.format(_['name'], _['id']), value='Ping : {}'.format(_['ping']), inline=False)
            [pembed.add_field(name=args.split(':')[0].capitalize(), value=args.split(':')[1], inline=False) for args in _['identifiers']]

            await ctx.send(embed=pembed)
        else:
            pass

    
## Server run
@client.command()
@commands.has_permissions(administrator=True) 
async def run(ctx):
    
    await ctx.message.delete()
    timenow = time.strftime("%H:%M")
    embed=discord.Embed(title="Server Run Help", description="Follow Below instructions)", color=0xff1414)
    embed.set_thumbnail(url="")#enter url
    embed.add_field(name="✅ Paste this in f8 ✅", value=f"connect {config.serverIP}", inline=False)
    embed.set_footer(text=f"{timenow}")
    await ctx.send(embed=embed)
    
## Help Command
@client.command()
@commands.has_permissions(administrator=True) 
async def help(ctx):
    
    embed=discord.Embed(title=" FiveM Bot", description=" FiveM Bot Commands List", color=0xfff700)
    embed.set_author(name="Welcome To  FiveM Bot", url="", icon_url="")#enter icon_url
    embed.set_thumbnail(url="")#enter url
    embed.add_field(name="Prefix  =  -", value="You Have to use - before every - command :)", inline=False)
    embed.add_field(name="-players", value="Server Online Players List", inline=False)
    embed.add_field(name="-pid", value="(pid (Users Fivem id) ) LookUp PlayerID From Online Players List", inline=False)
    embed.add_field(name="-say", value="(say (Your message) ) Say Something as BOT in Embed Message with your name", inline=False)
    embed.add_field(name="-hsay", value="(hsay (Your message) ) Say Something as BOT [Hidden Mode]", inline=False)
    embed.add_field(name="-run", value="Server run shod Embed", inline=False)
    embed.add_field(name="-ip", value="(ip (Source IP) ) To check some IP Address", inline=False)
    await ctx.send(embed=embed)
    
## Players Command
@client.command()
@commands.has_permissions(administrator=True) 
async def players(ctx):
    
    timenow = time.strftime("%H:%M")
    resp = rq.get('http://'+config.serverIP+'/players.json').json()
    total_players = len(resp)
    if len(resp) > 25:
        for i in range(round(len(resp) / 25)):
            embed = discord.Embed(title=' FiveM Bot', description='Server Players', color=discord.Color.blurple())
            embed.set_footer(text=f'Total Players : {total_players} | FiveMBot | {timenow}')
            count = 0
            for player in resp:
                embed.add_field(name=player['name'], value='ID : ' + str(player['id']))
                resp.remove(player)
                count += 1
                if count == 25:
                    break
                else:
                    continue

            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title=' FiveM Bot', description='Server Players', color=discord.Color.blurple())
        embed.set_footer(text=f'Total Players : {total_players} |  FiveM Bot | {timenow}')
        for player in resp:
            embed.add_field(name=player['name'], value='ID : ' + str(player['id']))
        await ctx.send(embed=embed)
    
@client.command()
@commands.has_permissions(administrator=True)
async def ip(ctx, *, ip=None):
    if not ip:
        await ctx.send('<@{}>, Please Specify A IP Address!'.format(ctx.message.author.id))
        return
    rsp = rq.get('http://ip-api.com/json/'+ip).json()
    if rsp['status'] == 'fail':
        #await ctx.send('Error !\nAPI Respond: '+rsp['message']+'\nQuery: '+rsp['query'])
        embed=discord.Embed(color=0xFF0000)
        embed.add_field(name="❌ Query Failed", value="❓ Reason: "+rsp['message'])
        embed.set_footer(text="Query: "+ip)
        await ctx.send(embed=embed)
        return
    embed=discord.Embed(color=0x00FFFF)
    embed.add_field(name="✅Status: "+rsp['status'], value=f"\n\n🌍Country: {rsp['country']} \n\n🌏CountryCode: {rsp['countryCode']} \n\n🔷Region: {rsp['region']} \n\n🔷Region Name: {rsp['regionName']} \n\n🔷City: {rsp['city']} \n\n🕑TimeZone: {rsp['timezone']} \n\n🏢ISP: {rsp['isp']}\n\n🏢ISP OrgName: {rsp['org']}\n\n🏢ISP MoreInfo: {rsp['as']}", inline=False)
    embed.set_footer(text="Requested IP: "+ip)
    await ctx.send(embed=embed)

## Live Status
@tasks.loop()
async def live_status(seconds=75):
    pcount = pc()
    Dis = client.get_guild(config.guildID) #Int

    activity = discord.Activity(type=discord.ActivityType.watching, name=f'🎮 {pcount} players playing')
    await client.change_presence(activity=activity)
    await asyncio.sleep(15)



client.run(config.Token)