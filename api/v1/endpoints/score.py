from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.base import get_db
from db.models import crud
from schemas import schemas

router = APIRouter(prefix="/score", tags=["Score"])

@router.post("/", response_model=schemas.Score)
async def create_score(score: schemas.ScoreCreate, student_id: int, db: Session = Depends(get_db)):
    '''Добавление оценки ученику, принимает id ученика и оценку'''
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return crud.create_score(db=db, score=score, student_id=student_id)

@router.get("/{score_id}", response_model=schemas.Score)
async def read_score(score_id: int, db: Session = Depends(get_db)):
    '''Получение информации об оценке по id'''
    db_score = crud.get_score(db, score_id=score_id)
    if db_score is None:
        raise HTTPException(status_code=404, detail="Score not found")
    return db_score

@router.patch("/{score_id}", response_model=schemas.Score)
async def update_score(score_id: int, new_score: int, db: Session = Depends(get_db)):
    '''Обновить информацию об оценке, принимает id оценки и новую оценку'''
    db_score = crud.get_score(db, score_id=score_id)
    if db_score is None:
        raise HTTPException(status_code=404, detail="Score not found")
    return crud.update_score(db=db, score_id=score_id, new_score=new_score)

@router.delete("/{score_id}", response_model=schemas.Score)
async def delete_score(score_id: int, db: Session = Depends(get_db)):
    '''Удаление оценки по id'''
    db_score = crud.get_score(db, score_id=score_id)
    if db_score is None:
        raise HTTPException(status_code=404, detail="Score not found")
    return crud.delete_score(db=db, score_id=score_id)