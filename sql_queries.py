QUERIES = {
    # --- Players Queries ---
    "All Players": "SELECT * FROM players LIMIT 50",
    "Indian Players": "SELECT * FROM players WHERE country='India'",
    "Australian Batsmen": "SELECT * FROM players WHERE country='Australia' AND role='Batsman'",
    "All Bowlers": "SELECT * FROM players WHERE role='Bowler'",
    "Players with 'Virat' in Name": "SELECT * FROM players WHERE name LIKE '%Virat%'",
    "Players by Country Count": "SELECT country, COUNT(*) AS player_count FROM players GROUP BY country",
    "Batsmen Count": "SELECT COUNT(*) AS total_batsmen FROM players WHERE role='Batsman'",
    "Bowlers by Country": "SELECT country, COUNT(*) AS bowler_count FROM players WHERE role='Bowler' GROUP BY country",
    "Top 10 Players Alphabetically": "SELECT * FROM players ORDER BY name ASC LIMIT 10",
    "Players Without Role": "SELECT * FROM players WHERE role IS NULL OR role=''",

    # --- Teams Queries ---
    "All Teams": "SELECT * FROM teams LIMIT 50",
    "Teams from India": "SELECT * FROM teams WHERE country='India'",
    "Teams by Country Count": "SELECT country, COUNT(*) AS team_count FROM teams GROUP BY country",
    "Team Names Alphabetical": "SELECT * FROM teams ORDER BY name ASC",
    "Unique Team Countries": "SELECT DISTINCT country FROM teams",

    # --- Matches Queries ---
    "All Matches": "SELECT * FROM matches LIMIT 50",
    "Match Status": "SELECT id, team1, team2, status FROM matches",
    "Ongoing Matches": "SELECT * FROM matches WHERE status LIKE '%Live%'",
    "Completed Matches": "SELECT * FROM matches WHERE status LIKE '%Completed%'",
    "Matches with India": "SELECT * FROM matches WHERE team1='India' OR team2='India'",
    "Matches per Team": "SELECT team1 AS team, COUNT(*) AS matches_played FROM matches GROUP BY team1 "
                        "UNION ALL SELECT team2, COUNT(*) FROM matches GROUP BY team2",
    "Head-to-Head India vs Australia": "SELECT * FROM matches WHERE (team1='India' AND team2='Australia') OR (team1='Australia' AND team2='India')",
    "Match Count by Status": "SELECT status, COUNT(*) AS total FROM matches GROUP BY status",
    "Teams Appearing in Matches": "SELECT DISTINCT team1 AS team FROM matches UNION SELECT DISTINCT team2 FROM matches",
}
