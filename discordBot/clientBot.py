import discord
Token = ' '

intents = discord.Intents.default()
intents.members = True
intents.presences = True
client = discord.Client(intents=intents)

"""채널 id
267314298764787712
텍스트=267314298764787712

봇 서버
976503953049157672
텍스트=976503953049157675

오디김
343687245041106944
텍스트=343687245041106944
"""

toGuild = client.get_guild(976503953049157672)
toChannel = client.get_channel(976503953049157675)

@client.event
async def on_ready():
    for member in toGuild.members:
        if member.bot==False and member.status.value=='online':
                print(f'안녕하세요 {member.name}님!')
                #await toGuild.text_channels[0].send(f'안녕하세요 {member.name}님!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content=='ㅎㅇ':
        await message.channel.send(f'안녕하세요 {message.author.name}님!')

client.run(Token)
