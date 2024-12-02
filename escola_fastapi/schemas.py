from pydantic import BaseModel

class AlunoBase(BaseModel):
    nome: str
    serie: int
    Ano_letivo: int
    idade: int

class CriarAluno(AlunoBase):
    pass

class Aluno(AlunoBase):
    id: int

    class Config:
        orm_mode = True

