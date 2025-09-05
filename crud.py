from utils.db_connection import run_sql

def get_players(limit=50):
    return run_sql("SELECT * FROM players LIMIT :limit", {"limit": limit})

def add_player(name, country, role):
    run_sql("INSERT INTO players (name, country, role) VALUES (:name, :country, :role)",
            {"name": name, "country": country, "role": role})
