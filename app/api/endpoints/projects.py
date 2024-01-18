from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud

router = APIRouter()

@router.get("/projects/")
async def read_projects(db: Session = Depends(get_db)):
    projects = crud.get_projects(db)
    return projects