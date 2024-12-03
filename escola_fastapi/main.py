from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import crud, models
from .database import engine
from escola_fastapi.routers import aluno
from escola_fastapi.routers.aluno import get_db

models.Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(aluno.router, prefix="/alunos", tags=["Alunos"])


@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API da Escola!"}


@app.post("/atualizar_nome_mae/")
def atualizar_nome_mae(db: Session = Depends(get_db)):
    crud.atualizar_nome_mae(db)  
    return {"message": "Alunos atualizados com sucesso!"}