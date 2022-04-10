import pymongo

from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://admin:admin@cluster0.4gjlh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = cluster["cluster0"]
students = db["students"]

# Finds All
docs = db.students.find()
for doc in docs:
    print(doc)

# Add new document
megan = {
    "_id": 1010, 
    "first_name":"megan", 
    "last_name": "rusher"
    }
megan_student_id = db.students.insert_one(megan).inserted_id

print()

# Finds new addition
doc = db.students.find_one({"_id": 1010})
print(doc)

# Delete new addition
megan_studen_id = db.students.delete_one({"_id": 1010})

print()

#Finds All
docs = db.students.find()
for doc in docs:
    print(doc)