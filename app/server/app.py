from fastapi import FastAPI, HTTPException

from .models import StudentSchema, CourseSchema, ClassSchema
from .database import MongoStorage

app = FastAPI()

mongo = MongoStorage()


@app.post('/create_student')
def create_student_table(student: StudentSchema):
    try:
        mongo.store_many(map(dict, student.students), 'students')
    except:
        raise HTTPException(status_code=404, detail="cant create student table")


@app.post('/create_courses')
def create_courses(course: CourseSchema):
    mongo.store_many(map(dict, course.courses), 'courses')


@app.post('/create_class')
def create_class(cls: ClassSchema):
    mongo.store_one(cls.dict(), 'classes')


@app.put('/set_end_date')
def set_end_time(obj_id: str):
    mongo.update(obj_id)


@app.get('/show_class')
def show_class():
    class_collection = mongo.load('classes')
    for cls in class_collection:
        duration = cls['end_date'] - cls['start_date']
        return f'{cls["user"]["name"]}, {cls["course"]["course"]}, {duration.seconds}'


@app.delete('/delete_student')
def delete_student(obj_id: str):
    mongo.delete(obj_id)
