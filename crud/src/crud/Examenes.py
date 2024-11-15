from sqlalchemy.orm import Session
from src.schemas.Examenes import ExamenCreate
from src.models.Examenes import Examen

def get_examen(db: Session, examen_id: int):
    return db.query(Examen).filter(Examen.id == examen_id).first()

def get_examenes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Examen).offset(skip).limit(limit).all()

def create_examen(db: Session, examen: ExamenCreate):
    db_examen = Examen(**examen.dict())
    db.add(db_examen)
    db.commit()
    db.refresh(db_examen)
    return db_examen

def update_examen(db: Session, examen_id: int, examen: ExamenCreate):
    db_examen = db.query(Examen).filter(Examen.id == examen_id).first()
    if db_examen:
        for key, value in examen.dict().items():
            setattr(db_examen, key, value)
        db.commit()
        db.refresh(db_examen)
    return db_examen

def delete_examen(db: Session, examen_id: int):
    db_examen = db.query(Examen).filter(Examen.id == examen_id).first()
    if db_examen:
        db.delete(db_examen)
        db.commit()
    return db_examen