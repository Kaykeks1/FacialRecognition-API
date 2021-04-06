import pymongo
from pymongo import MongoClient

import cv2
import os
import numpy as np

# import MySQLdb as mdb
import json
# import faceRecognition as fr

class get:
    def __init__(self):
        # self.connection = mdb.connect('localhost', 'root', '', 'student_verification')
        # self.cursor = self.connection.cursor(mdb.cursors.DictCursor)
        self.client = MongoClient()
        self.db = self.client.Student_ID
        self.Students = self.db.students
        

    def get_student(self, data):
        # print("44444444444444444",data)

        # self.cursor.execute("SELECT * FROM students WHERE firstName=%s"%data)#  =1
        # students = self.cursor.fetchall()
        # print(students)
        # value=None
        # for student in students:
        #     print(student)
        #     value=student
        # if value:
        #     return json.dumps(value)
        # else:
        #     return False
        # print("id is", id)

        student = self.Students.find_one({'name': data})
        print(student)
        if student:
            return student
        else:
            return False
        print("id is", id)