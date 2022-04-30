#Samuel Trevino
# April 29, 2022
#MOD 9.3 Assignment

import mysql.connector

mydb = mysql.connector.connect(
    user ="pysports_user",
    password = "MySQL8IsGreat!",
    host = "127.0.0.1",
    database = "pysports",
)

# Executes Insert

mycursor = mydb.cursor()

insert = "INSERT INTO player (first_name, last_name, team_id) VALUES ('Smeagol', 'Shire Folk', 1)";

mycursor.execute(insert)

mydb.commit()

query = "SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id"

mycursor.execute(query)

players = mycursor.fetchall()

print()
print("--DISPLAYING PLAYERS AFTER INSERT--")

for player in players:
    print(player)


# Executes update

update = "UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'"

mycursor.execute(update)

mydb.commit()

# Executes new query 

query = "SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id"

mycursor.execute(query)

players = mycursor.fetchall()

print()
print("--DISPLAYING PLAYERS AFTER UPDATE--")

for player in players:
    print(player)

# Executes Delete

delete = "DELETE FROM player WHERE first_name = 'Gollum'"    

mycursor.execute(delete)

mydb.commit()

# Executes new query 

query = "SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id"

mycursor.execute(query)

players = mycursor.fetchall()

print()
print("--DISPLAYING PLAYERS AFTER DELETE--")

for player in players:
    print(player)