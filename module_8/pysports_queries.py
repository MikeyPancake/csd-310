#Samuel Trevino
# April 22, 2022
#MOD 8.3 Assignment

import mysql.connector

mydb = mysql.connector.connect(
    user ="pysports_user",
    password = "MySQL8IsGreat!",
    host = "127.0.0.1",
    database = "pysports",
)

#Displays Team Information
mycursor = mydb.cursor()

mycursor.execute("SELECT team_id, team_name, mascot FROM team")

teams = mycursor.fetchall()

print("--DISPLAYING TEAM RECORDS--")

for team in teams:
	#print("Team Name: {}".format(team[1]))
    print(player)


print()

#Displays Player information
mycursor = mydb.cursor()

mycursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

player = mycursor.fetchall()

print("--DISPLAYING PLAYER RECORDS--")

for player in player:
    print(player)