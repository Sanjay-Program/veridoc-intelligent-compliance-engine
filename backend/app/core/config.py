import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME: str = "Veridoc Global"

    # DB
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", "postgresql://admin:admin@localhost:5432/veridoc"
    )


settings = Settings()
