import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///cricbuzz.db")
engine = create_engine(DATABASE_URL, echo=False)

def run_sql(sql, params=None):
    with engine.begin() as conn:
        result = conn.execute(text(sql), params or {})
        try:
            return result.fetchall()
        except:
            return None
