from fastapi import FastAPI, Depends, status
from fastapi import HTTPException
from sqlalchemy.orm import Session
from escola_fastapi import crud, models, schemas
from .database import engine
from escola_fastapi.routers import aluno, usuarios
from escola_fastapi.routers.aluno import get_db
from escola_fastapi.securyt import create_access_token, verify_token, authenticate_user
from escola_fastapi.models import Usuario


models.Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(aluno.router, prefix="/alunos", tags=["Alunos"])
app.include_router(usuarios.router, prefix="/usuarios", tags=["Usuarios"])


@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API da Escola!"}


@app.post("/token")
def login_for_access_token(form_data: schemas.UserLogin, db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.Usuario})
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/atualizar_nome_mae/")
def atualizar_nome_mae(db: Session = Depends(get_db)):
    crud.atualizar_nome_mae(db)  
    return {"message": "Alunos atualizados com sucesso!"}