from models import User, Book
from database import engine, SessionLocal
from sqlalchemy.orm import Session

with SessionLocal as session:
    usuario_inicial = User(nome="Maria", email="maria@gmail")
    livro_inicial = Book(titulo="Dom Casmurro", id_usuario=1)

    session.add(usuario_inicial)
    session.add(livro_inicial)

    session.commit()