from sqlalchemy.orm import Session
from . import models, schemas

def ver_aluno(db: Session, skip: int=0, limit = 10):
    return db.query(models.Aluno).offset(skip).limit(limit).all()

def filtrar_aluno(db: Session, aluno_id=int):
    return db.query(models.Aluno).filter(models.Aluno,id == aluno_id).frist()

def criar_aluno(db: Session, Aluno: schemas.CriarAluno):
    db_aluno = models.Aluno(**Aluno.dict())
    db.add(db_aluno)
    db.commit()
    db.refresh(db_aluno)
    return db_aluno