from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_db
from models import Livro
from schemas import LivroIn, LivroOut

app = FastAPI(title="API Biblioteca")


def buscar_livro(db: Session, livro_id: int) -> Livro:
    livro = db.get(Livro, livro_id)
    if livro is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Livro não encontrado")
    return livro


@app.get("/livros", response_model=list[LivroOut])
def listar_livros(
    autor: str | None = None,
    disponivel: bool | None = None,
    db: Session = Depends(get_db),
):
    consulta = select(Livro)
    if autor:
        consulta = consulta.where(Livro.autor.ilike(f"%{autor}%"))
    if disponivel is not None:
        consulta = consulta.where(Livro.disponivel == disponivel)
    return db.scalars(consulta).all()


@app.get("/livros/{livro_id}", response_model=LivroOut)
def obter_livro(livro_id: int, db: Session = Depends(get_db)):
    return buscar_livro(db, livro_id)


@app.post("/livros", response_model=LivroOut, status_code=status.HTTP_201_CREATED)
def criar_livro(dados: LivroIn, db: Session = Depends(get_db)):
    livro = Livro(**dados.model_dump())
    db.add(livro)
    db.commit()
    db.refresh(livro)
    return livro


@app.put("/livros/{livro_id}", response_model=LivroOut)
def atualizar_livro(livro_id: int, dados: LivroIn, db: Session = Depends(get_db)):
    livro = buscar_livro(db, livro_id)
    for campo, valor in dados.model_dump().items():
        setattr(livro, campo, valor)
    db.commit()
    db.refresh(livro)
    return livro


@app.delete("/livros/{livro_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_livro(livro_id: int, db: Session = Depends(get_db)):
    livro = buscar_livro(db, livro_id)
    db.delete(livro)
    db.commit()
