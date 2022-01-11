from datetime import datetime

from bson.objectid import ObjectId
from fastapi import FastAPI, HTTPException

from .models import StudentSchema, CourseSchema, ClassSchema
from .database import students_collection, course_collection, class_collection

app = FastAPI()


@app.post('/create_student')
def create_student_table(student: StudentSchema):
    try:
        students_collection.insert_many(map(dict, student.students))
    except:
        HTTPException(status_code=404, detail='cant create student table')


@app.post('/create_courses')
def create_courses(course: CourseSchema):
    try:
        course_collection.insert_many(map(dict, course.courses))
    except:
        HTTPException(status_code=404, detail='cant create course table')


@app.post('/create_class')
def create_class(cls: ClassSchema):
    class_collection.insert_one(cls.dict())


@app.put('/set_end_date')
def set_end_time(obj_id: str):
    query = {"_id": ObjectId(obj_id)}
    update = {"$set": {"end_date": datetime.now()}}
    class_collection.update_one(query, update)


@app.get('/show_class')
def show_class():
    for cls in class_collection.find():
        duration = cls['end_date'] - cls['start_date']
        return f'{cls["user"]["name"]}, {cls["course"]["course"]}, {duration.seconds}'


@app.delete('/delete_student')
def delete_obj(obj_id: str):
    students_collection.delete_one({'_id': ObjectId(obj_id)})
