
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from .. import models
from ..schemas.student import StudentCreate, StudentUpdate, StudentOut
from ..models.student import Student
from sqlalchemy.exc import IntegrityError

router = APIRouter()

@router.get("/students", response_model=List[StudentOut])
def list_students(db: Session = Depends(get_db)):
    items = db.query(Student).order_by(Student.id).all()
    return items

@router.get("/students/{student_id}", response_model=StudentOut)
def get_student(student_id: int, db: Session = Depends(get_db)):
    item = db.query(Student).filter(Student.id == student_id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return item

@router.post("/students", response_model=StudentOut, status_code=status.HTTP_201_CREATED)
def create_student(payload: StudentCreate, db: Session = Depends(get_db)):
    data = payload.model_dump()
    if data.get("avatar_url"):
        data["avatar_url"] = str(data["avatar_url"])
    obj = Student(**data)

    db.add(obj)
    try:
        db.commit()
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email must be unique")
    db.refresh(obj)
    return obj

@router.put("/students/{student_id}", response_model=StudentOut)
def update_student(student_id: int, payload: StudentUpdate, db: Session = Depends(get_db)):
    obj = db.query(Student).filter(Student.id == student_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    data = payload.model_dump(exclude_unset=True)
    if data.get("avatar_url") is not None:
        data["avatar_url"] = str(data["avatar_url"])
    if data.get("email") is not None:
        data["email"] = str(data["email"])
    for k, v in data.items():
        setattr(obj, k, v)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email must be unique")
    db.refresh(obj)
    return obj

@router.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    obj = db.query(Student).filter(Student.id == student_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    db.delete(obj)
    db.commit()
    return {"message": "Student deleted"}
