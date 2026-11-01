# API Biblioteca — Persistência com SQLAlchemy e Alembic

API REST para controle de livros de uma biblioteca. Os dados são salvos em um banco SQLite via SQLAlchemy, e a estrutura do banco é versionada com migrações do Alembic.

**Aluno:** Lucas Bezerra

## Estrutura

```
database.py      engine, sessão e dependência get_db
models.py        model Livro (tabela livros)
schemas.py       schemas Pydantic de entrada e saída
main.py          rotas CRUD
alembic/         configuração e migrações (versions/)
```

## Como rodar

Requer Python 3.10 ou superior.

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
alembic upgrade head           # cria o arquivo biblioteca.db com as tabelas
fastapi dev main.py
```

Documentação (Swagger): http://127.0.0.1:8000/docs

O arquivo `biblioteca.db` é gerado localmente e não vai para o repositório.

## Migrações

Depois de alterar algum model:

```bash
alembic revision --autogenerate -m "descricao da mudanca"
alembic upgrade head
```

## Rotas

| Método | Rota | Descrição |
|---|---|---|
| GET | `/livros` | Lista livros (filtros opcionais: `autor`, `disponivel`) |
| GET | `/livros/{id}` | Busca um livro |
| POST | `/livros` | Cadastra um livro |
| PUT | `/livros/{id}` | Atualiza um livro |
| DELETE | `/livros/{id}` | Remove um livro |

Exemplo de corpo para POST/PUT:

```json
{
  "titulo": "Dom Casmurro",
  "autor": "Machado de Assis",
  "ano": 1899,
  "disponivel": true
}
```
