from pydantic import BaseModel, EmailStr
from typing import Optional, List

class AlunoBase(BaseModel):
    nome: str
    nome_mae: str
    serie: int
    Ano_letivo: int
    idade: int

class AlunoCriado(BaseModel):
    nome: str
    serie: int

    class Config:
        orm_mode = True
        exclude_none = True


class CriarAluno(AlunoBase):
    pass


class Aluno(AlunoBase):
    id: int

    class Config:
        orm_mode = True

class AtualizarAluno(AlunoBase):
    nome: str
    nome_mae: str
    serie: int
    Ano_letivo: int
    idade: int

class UserLogin(BaseModel):
    username: str
    password: str

class UserInDB(UserLogin):
    hashed_password: str

class Usuario(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True

class UsuarioCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UsuarioAtivo(Usuario):
    is_active: bool

    class Config:
        from_attributes = True