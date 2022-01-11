from pymongo import MongoClient

client = MongoClient()
db = client.academy_denormalized

students_collection = db.student
course_collection = db.courses
class_collection = db.classes

