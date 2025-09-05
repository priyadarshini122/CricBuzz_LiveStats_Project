import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RAPIDAPI_KEY")
API_HOST = os.getenv("RAPIDAPI_HOST")
BASE_URL = "https://cricbuzz-cricket.p.rapidapi.com"

HEADERS = {
    "x-rapidapi-key": API_KEY if API_KEY else "",
    "x-rapidapi-host": API_HOST if API_HOST else "cricbuzz-cricket.p.rapidapi.com"
}

# ✅ Fallback sample data
SAMPLE_MATCHES = {
    "typeMatches": [
        {
            "matchType": "International",
            "seriesMatches": [
                {
                    "seriesAdWrapper": {
                        "seriesName": "Sample Series",
                        "matches": [
                            {
                                "matchInfo": {
                                    "matchId": 12345,
                                    "team1": {"teamName": "India"},
                                    "team2": {"teamName": "Australia"},
                                    "status": "India 120/3 in 15 overs"
                                }
                            }
                        ]
                    }
                }
            ]
        }
    ]
}

def get_live_matches():
    if not API_KEY:
        print("⚠️ No API key found. Using sample data.")
        return SAMPLE_MATCHES
    try:
        url = f"{BASE_URL}/matches/v1/live"
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"⚠️ API Error: {e}. Using sample data instead.")
        return SAMPLE_MATCHES
