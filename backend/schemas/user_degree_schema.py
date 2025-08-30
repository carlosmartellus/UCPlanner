from pydantic import BaseModel
from typing import List, Optional

class DegreeBase(BaseModel):
    name: str
    school: Optional[str] = None
    total_credits: int

class DegreeCreate(DegreeBase):
    pass

class DegreeRead(DegreeBase):
    id: int

    class Config:
        from_attributes = True
        orm_mode = True

class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int
    degrees: List[DegreeRead] = []

    class Config:
        from_attributes = True
        orm_mode = True