from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class StudentSchemaNestedOne(BaseModel):
    name: str = Field(...)
    last_name: str = Field(...)
    phone_num: str = Field(...)


class StudentSchema(BaseModel):
    students: List[StudentSchemaNestedOne]


class CourseSchemaNestedOne(BaseModel):
    course: str = Field(...)
    teacher: str = Field(...)
    price: int = Field(...)
    capacity: int = Field(...)


class CourseSchema(BaseModel):
    courses: List[CourseSchemaNestedOne]


class ClassSchema(BaseModel):
    user: StudentSchemaNestedOne = Field(...)
    course: CourseSchemaNestedOne = Field(...)
    is_paid: bool = Field(...)
    start_date: Optional[datetime] = datetime.now()

