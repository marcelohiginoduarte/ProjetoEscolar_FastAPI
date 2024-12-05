from sqlalchemy import Column, Integer, String, Boolean
from .database import Base 


class Aluno(Base):
    __tablename__ = "Alunos"

    id = Column(Integer, primary_key=True)
    nome = Column(String, index=True)
    nome_mae = Column(String, index=True)
    serie = Column(Integer, index=True)
    Ano_letivo = Column(Integer, index=True)
    idade = Column(Integer)

class Usuario(Base):
    __tablename__ = "Usuarios"

    id = Column(Integer, primary_key=True)
    username = Column(Integer, index=True)
    email = Column(Integer, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
