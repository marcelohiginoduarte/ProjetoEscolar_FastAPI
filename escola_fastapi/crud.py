from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas

def ver_alunos(db: Session, skip: int=0, limit = 10):
    return db.query(models.Aluno).offset(skip).limit(limit).all()

def filtrar_aluno(db: Session, aluno_id: int):
    return db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()


def verificar_aluno_existente(db: Session, nome: str, nome_mae: str):
    return db.query(models.Aluno).filter(models.Aluno.nome == nome, models.Aluno.nome_mae == nome_mae).first()

def criar_aluno(db: Session, Aluno: schemas.CriarAluno):
    aluno_existente = verificar_aluno_existente(db, Aluno.nome, Aluno.nome_mae)
    if aluno_existente:
        raise HTTPException(status_code=400, detail="Aluno ja esta cadastrado!")
    

    db_aluno = models.Aluno(**Aluno.dict())
    db.add(db_aluno)
    db.commit()
    db.refresh(db_aluno)
    return db_aluno


def atualizar_aluno_db(db: Session, aluno_id: int, aluno_atualizado: schemas.AtualizarAluno):
    db_aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()

    if not db_aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")

    for key, value in aluno_atualizado.dict(exclude_unset=True).items():
        setattr(db_aluno, key, value)

    db.commit()
    db.refresh(db_aluno)
    return db_aluno