import os
import sys

# Добавляем текущий каталог в sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
from app.database import SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.project import Project

def load_projects_from_json(file_path):
    # Получаем директорию, в которой находится текущий скрипт
    script_dir = os.path.dirname(__file__)
    # Объединяем директорию со значением переданным в аргументе file_path
    abs_file_path = os.path.join(script_dir, file_path)

    with open(abs_file_path, 'r') as file:
        projects_data = json.load(file)
    return projects_data


def populate_projects_to_database(db: Session, projects_data):
    for project_data in projects_data:
        project = Project(**project_data)
        try:
            db.add(project)
            db.commit()
            print(f"Проект '{project.name}' успешно добавлен в базу данных.")
        except IntegrityError as e:
            db.rollback()
            print(f"Ошибка: Проект '{project.name}' уже существует в базе данных.")

if __name__ == "__main__":
    json_file_path = "projects_data.json"
    projects_data = load_projects_from_json(json_file_path)

    db = SessionLocal()
    populate_projects_to_database(db, projects_data)
    db.close()