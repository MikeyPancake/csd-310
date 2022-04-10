
import pymongo

from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://admin:admin@cluster0.4gjlh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = cluster["cluster0"]
students = db["students"]

fred = {
    "_id": 1007, 
    "first_name":"fred", 
    "last_name": "johnson"
    }

mike = {
    "_id": 1008, 
    "first_name":"mike", 
    "last_name": "davis"
    }
dave = {
    "_id": 1009, 
    "first_name":"dave", 
    "last_name": "hugs"
    }

fred_student_id = db.students.insert_one(fred).inserted_id
mike_student_id = db.students.insert_one(mike).inserted_id
dave_student_id = db.students.insert_one(dave).inserted_id 
print(fred_student_id)
print(mike_student_id)
print(dave_student_id)






