from .db_connection import run_sql

def insert_sample_data():
    run_sql("INSERT INTO players (name, country, role) VALUES (:name, :country, :role)",
            {"name": "Virat Kohli", "country": "India", "role": "Batsman"})
    run_sql("INSERT INTO players (name, country, role) VALUES (:name, :country, :role)",
            {"name": "Steve Smith", "country": "Australia", "role": "Batsman"})
    run_sql("INSERT INTO teams (name, country) VALUES (:name, :country)",
            {"name": "India", "country": "India"})
    run_sql("INSERT INTO teams (name, country) VALUES (:name, :country)",
            {"name": "Australia", "country": "Australia"})
