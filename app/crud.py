from sqlalchemy.orm import Session
from .models.project import Project

def get_projects(db: Session):
    return db.query(Project).all()