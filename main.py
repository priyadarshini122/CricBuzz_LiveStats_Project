import streamlit as st
import pandas as pd
from utils.api_client import get_live_matches
from crud import get_players, add_player
from sql_queries import QUERIES
from utils.db_connection import run_sql

st.set_page_config(page_title="Cricbuzz Dashboard", layout="wide")

st.sidebar.title("Cricbuzz Dashboard")
menu = st.sidebar.radio("Go to", ["Home", "Live Matches", "SQL Queries", "CRUD"])

if menu == "Home":
    st.title("🏏 Cricbuzz LiveStats Dashboard")
    st.write("Welcome! View live matches, run SQL queries, and manage cricket data.")

elif menu == "Live Matches":
    st.title("Live Matches")
    data = get_live_matches()
    for match_type in data.get("typeMatches", []):
        for series in match_type.get("seriesMatches", []):
            matches = series.get("seriesAdWrapper", {}).get("matches", [])
            for m in matches:
                info = m["matchInfo"]
                st.subheader(f"{info['team1']['teamName']} vs {info['team2']['teamName']}")
                st.write(f"Status: {info['status']}")

elif menu == "SQL Queries":
    st.title("SQL Queries")
    query_name = st.selectbox("Choose Query", list(QUERIES.keys()))
    sql = QUERIES[query_name]
    st.code(sql)
    result = run_sql(sql)
    if result:
        st.dataframe(pd.DataFrame(result))

elif menu == "CRUD":
    st.title("Manage Players")
    name = st.text_input("Player Name")
    country = st.text_input("Country")
    role = st.text_input("Role")
    if st.button("Add Player"):
        add_player(name, country, role)
        st.success(f"Player {name} added successfully!")
    st.subheader("All Players")
    players = get_players()
    st.dataframe(pd.DataFrame(players))
