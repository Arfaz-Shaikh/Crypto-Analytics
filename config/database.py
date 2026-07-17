import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)

engine = create_engine(DATABASE_URL)

from sqlalchemy import text
try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        print(result.fetchone())
        print("✅ PostgreSQL Connected Successfully!")
except Exception as e:
    print(e)