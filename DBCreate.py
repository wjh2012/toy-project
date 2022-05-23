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
sql = "CREATE TABLE GGOMG_BOT(word text PRIMARY KEY, exp text,userID text,userName text,guild text,Date text)"
cursor.execute(sql)
con.commit()


con.close()