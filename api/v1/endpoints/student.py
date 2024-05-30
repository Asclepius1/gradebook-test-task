from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.base import get_db
from db.models import crud
from schemas import schemas

router = APIRouter(prefix="/students", tags=["Student"])

@router.post("/", response_model=schemas.Student)
async def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    '''Создание нового ученика, принимает имя ученика'''
    return crud.create_student(db=db, student=student)

@router.get("/{student_id}", response_model=schemas.Student)
async def read_student(student_id: int, db: Session = Depends(get_db)):
    '''Получение информации об ученике по id'''
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@router.patch("/{student_id}", response_model=schemas.Student)
async def update_student(student_id: int, name: str, db: Session = Depends(get_db)):
    '''Изменение информаций ученика, принимает id ученика и новое имя'''
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return crud.update_student(db=db, student_id=student_id, name=name)

@router.delete("/{student_id}", response_model=schemas.Student)
async def delete_student(student_id: int, db: Session = Depends(get_db)):
    '''Удаление ученика по id'''
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return crud.delete_student(db=db, student_id=student_id)