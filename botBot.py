import discord
from discord.ext import commands
import sqlite3

con = sqlite3.connect("C:/Users/wjh20/workdpace/discordBot/bot.db")
cursor = con.cursor()

Token = 'OTc2NDg1MTEyMTEzOTQyNTU4.G-x05V.wAkJnB_ycrFSbJZhE__1rKxPKLcQo5miMgF25o'

intents = discord.Intents.default()
intents.members = True
intents.presences = True
bot = commands.Bot(command_prefix='!', intents=intents)

Dongma=267314298764787712
DongmaText=267314298764787712
Botserver=976503953049157672

kal={
    "인텔사냥꾼":261012687302033409,
    "김재홍":271271763793412096,
    "폐인중":276383229198467074,
    "원장호":343619341826260992,
    "정관호":351782836552073216,
    "김서겸":831187209239134229,
    "최희성":328795854326726657,
}

def checkGuild(guild):
    if guild.id == Dongma:
        return True
    else:
        return False

def checkOnline(guild):
    who = []
    for member in guild.members:
        if member.bot==False and member.status.value == 'online':
            who.append(member)
    return who

def checkVoice(guild):
    who = []
    for channel in guild.voice_channels:
        who+=channel.members
    return who
        
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
"""
@bot.event
async def on_ready():
    for member in bot.get_guild(267314298764787712).members:
        print(member.name, member.id)
"""
"""
@bot.event
async def on_member_update(before, after):
    if checkGuild(before.guild):
        if before.status.value in ('offline','dnd') and after.desktop_status.value=='online':
            await after.guild.text_channels[0].send(f"안녕하세요. {after.name}님!")
"""
@bot.event
async def on_message(message):
    if checkGuild(message.guild):
        if message.author == bot.user:
            return
        if message.content=='ㅎㅇ':
            await message.channel.send(f'안녕하세요 {message.author.name}님!')
        if message.content=='슉슈슉':
            await message.channel.send('슉. 슈슉 시. 시발럼아 슈슉. 슉 슉시. 시벌람아. 슉. 시발. 슈슉 슉. 시. 시발. 슉 럼아 슈슉. 시발. 럼아 슉. 슈슉 슉. 슉 시. 시발럼. 아슉 슈슉 슉. 시벌람아. 슉슉. 슈슉 시. 시발럼아 슈슉. 슉 슉시. 시발럼아. 슉. 시발. 슈슉 슉. 시. 시발. 슉 럼아 슈슉. 시발.')
        if message.content=='칼':
            onList = checkOnline(message.guild)
            voList = checkVoice(message.guild)
            a_sub_b = [x for x in onList if x not in voList]
            final = [x for x in a_sub_b if x.id in kal.values and x.id!=message.author]
            menList = [x.mention for x in final]
            await message.channel.send("".join(map(str, menList)))

bot.run(Token)