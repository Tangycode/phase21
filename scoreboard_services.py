from utils.calculations import calculate_run_rate

# This function is now integration-ready and expects real match data input
def get_match_scoreboard(match_id):
    
    # In integration mode, this should be replaced with DB/API call
    match_data = fetch_match_data(match_id)

    if not match_data:
        return {
            "status": "error",
            "message": "Match not found"
        }

    innings = match_data.get("innings")

    if not innings:
        return {
            "status": "success",
            "message": "Match exists but no innings started",
            "data": {
                "match_id": match_id,
                "status": "no_innings"
            }
        }

    runs = innings["runs"]
    wickets = innings["wickets"]
    balls = innings["balls"]

    overs = balls // 6 + (balls % 6) / 10
    run_rate = calculate_run_rate(runs, balls)

    return {
        "status": "success",
        "data": {
            "match_id": match_id,
            "batting_team": innings["batting_team"],
            "bowling_team": innings["bowling_team"],
            "score": f"{runs}/{wickets}",
            "overs": overs,
            "run_rate": run_rate,
            "key_performers": {
                "batsman": innings.get("top_batsman"),
                "bowler": innings.get("top_bowler")
            }
        }
    }


# This simulates dynamic fetching (replace with real DB/API integration)
def fetch_match_data(match_id):
    # Placeholder — to be replaced in Django integration
    return {
        "match_id": match_id,
        "innings": {
            "runs": 120,
            "wickets": 3,
            "balls": 90,
            "batting_team": "Team A",
            "bowling_team": "Team B",
            "top_batsman": "Player 1",
            "top_bowler": "Player 2"
        }
    }
