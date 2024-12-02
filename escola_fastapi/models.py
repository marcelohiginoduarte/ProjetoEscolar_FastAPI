from sqlalchemy import Column, Integer, String
from .database import Base 


class Aluno(Base):
    __tablename__ = "Alunos"

    id = Column(Integer, primary_key=True)
    nome = Column(String, index=True)
    serie = Column(Integer, index=True)
    Ano_letivo = Column(Integer, index=True)
    idade = Column(Integer)
