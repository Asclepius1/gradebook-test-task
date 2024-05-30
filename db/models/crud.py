from sqlalchemy.orm import Session
from db.models.models import Student, Score
from schemas.schemas import StudentCreate, ScoreCreate

def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

def create_student(db: Session, student: StudentCreate):
    db_student = Student(name=student.name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def update_student(db: Session, student_id: int, name: str):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student:
        db_student.name = name
        db.commit()
        db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: int):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student:
        db.delete(db_student)
        db.commit()
    return db_student

def get_score(db: Session, score_id: int):
    return db.query(Score).filter(Score.id == score_id).first()

def create_score(db: Session, score: ScoreCreate, student_id: int):
    db_score = Score(score=score.score, student_id=student_id)
    db.add(db_score)
    db.commit()
    db.refresh(db_score)
    return db_score

def update_score(db: Session, score_id: int, new_score: int):
    db_score = db.query(Score).filter(Score.id == score_id).first()
    if db_score:
        db_score.score = new_score
        db.commit()
        db.refresh(db_score)
    return db_score

def delete_score(db: Session, score_id: int):
    db_score = db.query(Score).filter(Score.id == score_id).first()
    if db_score:
        db.delete(db_score)
        db.commit()
    return db_score
