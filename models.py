from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Livro(Base):
    __tablename__ = "livros"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(200))
    autor: Mapped[str] = mapped_column(String(120), index=True)
    ano: Mapped[int]
    disponivel: Mapped[bool] = mapped_column(default=True)
