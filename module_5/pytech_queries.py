
import pymongo

from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://admin:admin@cluster0.4gjlh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = cluster["cluster0"]
students = db["students"]

#Finds All
docs = db.students.find()
for doc in docs:
    print(doc)

print()

# Finds One
doc = db.students.find_one({"_id": 1007})
print(doc)

