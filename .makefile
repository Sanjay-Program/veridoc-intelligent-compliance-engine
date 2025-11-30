run-api:
    uvicorn app.main:app --reload --port 8000

install:
    pip install -r requirements.txt

compose:
    docker-compose up --build

format:
    black .
    ruff check . --fix
