from pydantic import BaseModel

class ScoreBase(BaseModel):
    score: int

class ScoreCreate(ScoreBase):
    pass

class Score(ScoreBase):
    id: int
    student_id: int

    class Config:
        from_attributes = True

class StudentBase(BaseModel):
    name: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    scores: list[Score] = []

    class Config:
        from_attributes = True
