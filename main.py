from pymongo import MongoClient
from datetime import datetime
from data import students, courses
from bson.objectid import ObjectId

client = MongoClient()
db = client.academy_denormalized

students_collection = db.students
course_collection = db.courses
class_collection = db.classes


def store_once():
    students_collection.insert_many(students)
    course_collection.insert_many(courses)


def add_to_class():
    zahra = students_collection.find_one({'name': "zahra"})
    python = course_collection.find_one({'course': "python"})

    classroom = class_collection.insert_one({
        'user': zahra,
        'course': python,
        'is_paid': True,
        'start_date': datetime.now()
    }
    )
    return classroom.inserted_id


def set_end_date(object_id):
    query = {'_id': ObjectId(object_id)}
    update = {"$set": {'end_date': datetime.now()}}
    class_collection.update_one(query, update)


def show_class():
    for cls in class_collection.find():
        duration = cls['end_date'] - cls['start_date']
        print(f'{cls["user"]["name"]}\t{cls["course"]["course"]}\t {duration.seconds}')


def delete_obj():
    students_collection.delete_one({'_id': ObjectId("61dabe2499b493b3911b5fa6")})



if __name__ == "__main__":
    # store_once()
    # add_to_class()
    # set_end_date("61daca2d305c69ff2a98a699")
    # show_class()
    delete_obj()
