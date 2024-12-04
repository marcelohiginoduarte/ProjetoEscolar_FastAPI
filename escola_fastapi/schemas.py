from pydantic import BaseModel
from typing import Optional

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

