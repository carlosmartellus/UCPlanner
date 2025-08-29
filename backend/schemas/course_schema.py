from pydantic import BaseModel

class CourseBase(BaseModel):
    code: str
    name: str
    nrc: int
    credits: int
    area: str | None = None

class CourseCreate(CourseBase):
    pass

class CourseRead(CourseBase):
    id: int

    class Config:
        from_attributes = True
