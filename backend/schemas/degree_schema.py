from pydantic import BaseModel

class DegreeBase(BaseModel):
    name: str
    school: str | None = None
    total_credits: int

class DegreeCreate(DegreeBase):
    pass

class DegreeRead(DegreeBase):
    id: int

    class Config:
        from_attributes = True
        orm_mode = True