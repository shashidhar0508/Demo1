from pydantic import BaseModel


class Technology(BaseModel):
    id: int
    name: str
    created_on: str


class Question(BaseModel):
    id: int
    name: str
    created_on: str
