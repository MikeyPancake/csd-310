#Samuel Trevino
# April 27, 2022
#MOD 9.2 Assignment

import mysql.connector

mydb = mysql.connector.connect(
    user ="pysports_user",
    password = "MySQL8IsGreat!",
    host = "127.0.0.1",
    database = "pysports",
)

#print(mydb)

mycursor = mydb.cursor()

query = "SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id"

mycursor.execute(query)

players = mycursor.fetchall()

print("--DISPLAYING TEAM RECORDS--")

for player in players:
    print(player)

