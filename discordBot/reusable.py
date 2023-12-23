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
a= [('꼼', '멍청이'), ('관호', '멍청이'), ('냐', '깡통')]
q=""
for i,j in a:
    q+="{:<10}{:<10}\n".format(i,j)

print(q)