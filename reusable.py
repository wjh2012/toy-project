import datetime
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

a= [('꼼장오', '멍청이'), ('관호', '멍청이'), ('아냐', '깡통')]

Q = [1.3, 2.4]
print(', '.join('{:.2f}'.format(f) for f in Q))
# 1.30, 2.40