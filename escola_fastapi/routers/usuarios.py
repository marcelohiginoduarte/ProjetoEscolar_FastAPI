from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from escola_fastapi import schemas, crud, models
from escola_fastapi.database import SessionLocal
from escola_fastapi.securyt import get_current_user, hash_passsword


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/Criar_usuario/", response_model=schemas.Usuario)
def criar_usuario(
    usuario: schemas.UsuarioCreate,
    db: Session = Depends(get_db)
):
    db_usuario = models.Usuario(
        username=usuario.username,
        email=usuario.email,
        hashed_password=hash_passsword(usuario.password)
    )

    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

@router.get("/ver_usuario", response_model=list[schemas.Usuario])
def ver_usuraios(skip: int=0, limit: int=10, db:Session = Depends(get_db)):
    return crud.ver_usuarios(db=db, skip=skip, limit=limit)