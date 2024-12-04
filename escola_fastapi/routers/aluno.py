from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from escola_fastapi import schemas, crud
from escola_fastapi.database import SessionLocal


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/Criar_aluno/", response_model=schemas.AlunoCriado)
def criar_aluno(Aluno: schemas.CriarAluno, db: Session = Depends(get_db)):
    aluno_criado = crud.criar_aluno(db=db, Aluno=Aluno)
    if aluno_criado:
        return{"nome": aluno_criado.nome, "serie": aluno_criado.serie}
    else:
        raise HTTPException(status_code=400, detail="Erro ao criar aluno")


@router.get("/Alunos/", response_model=list[schemas.Aluno])
def ver_alunos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.ver_alunos(db=db, skip=skip, limit=limit)


@router.get("/Aluno/{aluno_id}", response_model=schemas.Aluno)
def ver_aluno(aluno_id: int, db: Session = Depends(get_db)):
    db_student = crud.filtrar_aluno(db=db, aluno_id=aluno_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Aluno não foi encontrado")
    return db_student


@router.put("/Aluno/{aluno_id}", response_model=schemas.AtualizarAluno)
def atualizar_aluno(aluno_id: int, aluno_atualizado: schemas.AtualizarAluno, db: Session = Depends(get_db)):
    return crud.atualizar_aluno_db(db, aluno_id, aluno_atualizado)