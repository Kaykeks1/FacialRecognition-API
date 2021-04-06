import web
#from models import login
import models.CreateStudent
import models.GetStudent

import cv2
import os
import numpy as np
import faceRecognition as fr
from PIL import Image
from PIL.ExifTags import TAGS

urls = (
    '/student/create', 'Create',
    '/student/get', 'Get'
)
app = web.application(urls, globals())


class Create:
    def POST(self):
        data = web.input()
        print(data)
        student_model = models.CreateStudent.create()
        student_model.insert_student(data)
        return data

class Get:
    def POST(self):
        data = web.input()
        fp=data.image
        print(data.image)
        print(type(data.image))
        f=open("input.jpg","wb")
        f.write(data.image)
        f.close()

        test_img=cv2.imread("input.jpg")
        print(test_img)

        faces_detected,gray_img=fr.recognizer.faceDetection(test_img)
        print("faces_detected:",faces_detected)
        print("faces_detected:",type(faces_detected) is tuple)
        if (type(faces_detected) is tuple):
            return {'error': 'Face not detected'}
        face_recognizer=cv2.face.LBPHFaceRecognizer_create()
        face_recognizer.read('trainingData2.yml')
        # name = {0 : "'Priyanka'",1 : "'Kangana'",2:"'Akan'",3:"'Kayode'"}
        # name = {0 : "'Jackie'",1 : "'Priyanka'",2:"'Kayode'"}
        name = {0 : "Jackie",1 : "Priyanka",2:"Kayode"}

        for face in faces_detected:
            (x,y,w,h)=face
            roi_gray=gray_img[y:y+h,x:x+w]
            print('w is: ',w,'h is: ',h)
            cv2.imwrite('face.jpg', roi_gray)
            cv2.imwrite('roi_gray.jpg', roi_gray)
            label,confidence=face_recognizer.predict(roi_gray)
            print("confidence:",confidence)
            print("label:",label)
            predicted_name=name[label]
            if(confidence>38):
                return {'error': 'Student is not verified'}
            fr.recognizer.resultImage(test_img,face,predicted_name)

        student_model = models.GetStudent.get()
        student = student_model.get_student(predicted_name)
        if student:
            return student
        print("error!")
        return "error"


if __name__ == "__main__":
    app.run()