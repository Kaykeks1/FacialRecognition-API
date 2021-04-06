import pymongo
from pymongo import MongoClient

class create:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.Student_ID
        self.Students = self.db.students
    def insert_student(self, data):
        print("2222222222222222",data)
        id = self.Students.insert({'name': data.name, 'department': data.department, 'matric_no': data.matric_no})
        print("id is", id)