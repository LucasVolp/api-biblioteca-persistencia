from pydantic import BaseModel, ConfigDict, Field


class LivroIn(BaseModel):
    titulo: str = Field(min_length=1, max_length=200)
    autor: str = Field(min_length=1, max_length=120)
    ano: int = Field(ge=0, le=2100)
    disponivel: bool = True


class LivroOut(LivroIn):
    model_config = ConfigDict(from_attributes=True)

    id: int
