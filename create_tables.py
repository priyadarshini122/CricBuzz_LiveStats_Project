from utils.db_connection import engine
from sqlalchemy import text

with open("db/schema.sql", "r") as f:
    sql_script = f.read()

statements = [stmt.strip() for stmt in sql_script.split(";") if stmt.strip()]

with engine.begin() as conn:
    for stmt in statements:
        conn.execute(text(stmt))

print("✅ Tables created successfully")
