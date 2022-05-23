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
sql1 = "select * from GGOMG_BOT;"

sql2 = "INSERT INTO GGOMG_BOT (word, exp) VALUES ('꼼장오','봇');"

sql3 = "select * from sqlite_master;"

cursor.execute(sql1)
rep = cursor.fetchall()

print(rep)

con.close()