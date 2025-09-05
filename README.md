📊 Cricbuzz LiveStats Dashboard

A real-time cricket analytics dashboard built with Python, Streamlit, SQLAlchemy, and SQLite, integrated with Cricbuzz API (via RapidAPI).

🚀 Features

📡 Live Matches: Fetches live cricket match updates using Cricbuzz API.

🧑‍🤝‍🧑 Players Database: Store, add, and query players with country and role.

🏏 Teams & Matches: Manage teams and match records.

⚡ SQL Queries: Run 25 predefined SQL queries to analyze players, teams, and matches.

✏️ CRUD Operations: Add new players dynamically.

🛠 ETL Pipeline: Load sample data or API data into the database.

🗂 Project Structure
cricbuzz_livestats/
│── db/
│   └── schema.sql          # Database schema (Players, Teams, Matches)
│── src/
│   ├── main.py             # Streamlit app entry point
│   ├── crud.py             # CRUD operations
│   ├── sql_queries.py      # 25 SQL queries
│   ├── create_tables.py    # Script to create DB tables
│   └── utils/
│       ├── api_client.py   # Cricbuzz API client
│       ├── db_connection.py# Database connection
│       └── etl.py          # Data load utilities
│── cricbuzz.db             # SQLite database (auto-created)
│── requirements.txt        # Dependencies
│── .env                    # Environment variables (API keys)
│── README.md               # Project documentation

⚙️ Installation & Setup

Clone the repo

git clone https://github.com/your-username/cricbuzz-livestats.git
cd cricbuzz-livestats


Create virtual environment

python -m venv venv
.\venv\Scripts\activate   # Windows PowerShell


Install dependencies

pip install -r requirements.txt


Set up database

python src/create_tables.py


Configure API Key

Create a .env file in the project root:

RAPIDAPI_KEY=your_rapidapi_key_here
RAPIDAPI_HOST=cricbuzz-cricket.p.rapidapi.com


Run the app

python -m streamlit run src/main.py

🛠 Dependencies

streamlit

sqlalchemy

pandas

requests

python-dotenv

Install them with:

pip install streamlit sqlalchemy pandas requests python-dotenv

📖 Example Queries

Some of the 25 queries available in the dashboard:

All Players

Indian Players

Australian Batsmen

All Teams

Ongoing Matches

Head-to-Head: India vs Australia

Match Count by Status

🎯 Future Enhancements

Add visualizations (bar charts, pie charts, etc.)

Support for player statistics (runs, wickets, averages).

Role-based access for admins vs viewers.

Deployment on Streamlit Cloud / Heroku / AWS.
