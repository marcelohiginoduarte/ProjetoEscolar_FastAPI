from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/Criar_aluno/", response_model=schemas.Aluno)
def criar_aluno(Aluno: schemas.CriarAluno, db: Session = Depends(get_db)):
    return crud.criar_aluno(db=db, Aluno=Aluno)


@app.get("/Alunos/", response_model=list[schemas.Aluno])
def ver_alunos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.ver_alunos(db=db, skip=skip, limit=limit)


@app.get("/Aluno/{aluno_id}", response_model=schemas.Aluno)
def ver_aluno(aluno_id: int, db: Session = Depends(get_db)):
    db_student = crud.filtrar_aluno(db=db, aluno_id=aluno_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Aluno não foi encontrado")
    return db_student

@app.post("/atualizar_nome_mae/")
def atualizar_nome_mae(db: Session = Depends(get_db)):
    crud.atualizar_nome_mae(db)  
    return {"message": "Alunos atualizados com sucesso!"}