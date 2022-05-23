import sqlite3

con = sqlite3.connect("C:/Users/wjh20/workdpace/discordBot/bot.db")
cursor = con.cursor()
"""
word
exp
userID
userName
guild
date
"""
sql1 = "select exp from GGOMG_BOT where word='ㄱㅁㄹ'"

sql2 = '''INSERT INTO GGOMG_BOT VALUES('꼼장오','봇','123','123','123','1234')'''

sql3 = '''select * from sqlite_master'''

sql4 = sql = "SELECT word, exp from GGOMG_BOT"
try:
    cursor.execute(sql4)
except:
    print('에러')

rep = cursor.fetchall()
print(rep)

con.close()