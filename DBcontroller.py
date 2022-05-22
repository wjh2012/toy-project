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
sql = " "

cursor.execute(sql)
con.close()