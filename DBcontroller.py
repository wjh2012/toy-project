import sqlite3

con = sqlite3.connect("C:/Users/wjh20/workdpace/discordBot/bot.db")
cursor = con.cursor()

sql = "CREATE TABLE knowledge(word text, exp text)"