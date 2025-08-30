from pydantic import BaseModel

class CharacteristicBase(BaseModel):
    name: str
    color: str

class CharacteristicCreate(CharacteristicBase):
    pass

class Characteristic(CharacteristicBase):
    id: int

    class Config:
        from_attributes = True
        orm_mode = True