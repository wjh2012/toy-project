import discord
from discord.ext import commands
import asyncio
import sqlite3
import datetime

con = sqlite3.connect("C:/Users/wjh20/workdpace/discordBot/bot.db")
cursor = con.cursor()

Token = 'OTc2NDg1MTEyMTEzOTQyNTU4.G-x05V.wAkJnB_ycrFSbJZhE__1rKxPKLcQo5miMgF25o'

intents = discord.Intents.default()
intents.members = True
intents.presences = True
bot = commands.Bot(command_prefix='>', intents=intents)

Dongma=267314298764787712
DongmaText=267314298764787712
Botserver=976503953049157672
odikim=343687245041106944

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
    if guild.id == Botserver:
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



#----------------------------------------------------------------------------------------------------

@bot.event
async def on_message(message):
    if checkGuild(message.guild):
        if message.author == bot.user:
            return
        await bot.process_commands(message)

@bot.event
async def on_command_error(ctx,error):
    await ctx.send('무슨 뜻인지 모르겠어요!')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

#-----------------------------------------------------------------------------------------
@bot.listen()
async def on_message(message):
    if checkGuild(message.guild):
        if message.author == bot.user:
            return
        msg = message.content.split()
        if msg[0].startswith('!!'):
            if word=='배운말':
                sql = "SELECT word, exp from GGOMG_BOT"
                cursor.execute(sql)
            else:
                if len(msg)==1:
                    word = msg[0].removeprefix('!!')
                    try:
                        sql = f"SELECT exp from GGOMG_BOT where word='{word}'"
                        cursor.execute(sql)
                        exp = cursor.fetchall()
                        await message.channel.send(f'{exp[0][0]}')
                    except:
                        await message.channel.send('모르겠어요')
                else:
                    word = msg[0].removeprefix('!!')
                    exp = ' '.join(msg[1:])
                    try:
                        sql = f"INSERT INTO GGOMG_BOT VALUES('{word}','{exp}','{message.author.id}','{message.author.name}','{message.guild.name}','{str(datetime.datetime.now())}')"
                        cursor.execute(sql)
                        con.commit()
                        await message.channel.send(f'새로 배웠어요!\n{word}는(은) {exp}')
                    except:
                        sql = f"UPDATE GGOMG_BOT SET exp='{exp}', userID='{message.author.id}', userName='{message.author.name}', guild='{message.guild.name}', date='{str(datetime.datetime.now())}'"
                        cursor.execute(sql)
                        con.commit()
                        await message.channel.send(f'다시 배웠어요!\n{word}은(는) {exp}')
        else:
            pass


            


@bot.listen()
async def on_message(message):
    if checkGuild(message.guild):
        if message.author == bot.user:
            return
        if message.content=='ㅎㅇ':
            await message.channel.send(f'안녕하세요 {message.author.name}님!')

@bot.listen()
async def on_message(message):
    if checkGuild(message.guild):
        if message.author == bot.user:
            return
        if message.content=='슉슈슉':
            await message.channel.send('슉. 슈슉 시. 시발럼아 슈슉. 슉 슉시. 시벌람아. 슉. 시발. 슈슉 슉. 시. 시발. 슉 럼아 슈슉. 시발. 럼아 슉. 슈슉 슉. 슉 시. 시발럼. 아슉 슈슉 슉. 시벌람아. 슉슉. 슈슉 시. 시발럼아 슈슉. 슉 슉시. 시발럼아. 슉. 시발. 슈슉 슉. 시. 시발. 슉 럼아 슈슉. 시발.')

@bot.listen()
async def on_message(message):
    if checkGuild(message.guild):
        if message.author == bot.user:
            return
        if message.content=='따흐흑':
            await message.channel.send('악!!!')

@bot.listen()
async def on_message(message):
    if checkGuild(message.guild):
        if message.author == bot.user:
            return
        if message.content=='새끼..':
            await message.channel.send('기열!')         

@bot.listen()
async def on_message(message):
    if checkGuild(message.guild):
        if message.author == bot.user:
            return
        if message.content in ('칼', '칼?'):
            onList = checkOnline(message.guild)
            voList = checkVoice(message.guild)
            a_sub_b = [x for x in onList if x not in voList]
            final = [x for x in a_sub_b if x.id in kal.values and x.id!=message.author]
            menList = [x.mention for x in final]
            await message.channel.send("".join(map(str, menList)))           

bot.run(Token)