from pydantic import BaseModel
from .characteristics_schema import Characteristic

class DegreeCourseBase(BaseModel):
    degree_id: int
    course_id: int
    characteristic_id: int | None = None

class DegreeCourseCreate(DegreeCourseBase):
    pass

class DegreeCourse(DegreeCourseBase):
    characteristic: Characteristic | None

    class Config:
        from_attributes = True
        orm_mode = True