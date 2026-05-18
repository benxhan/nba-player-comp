from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats

def get_player_stats(player_name : str) -> dict:
    # find player
    matches = players.find_players_by_full_name(player_name)
    if not matches:
        raise ValueError(f"Player '{player_name}' not found")
    
    player = matches[0]
    career = playercareerstats.PlayerCareerStats(player_id=player['id'])
    df = career.get_data_frames()[0]
    latest = df.iloc[-1]

    return {
        "name": player['full_name'],
        "season": latest['SEASON_ID'],
        "points_per_game": round(latest['PTS'] / latest['GP'], 1),
        "rebounds_per_game": round(latest['REB'] / latest['GP'], 1),
        "assists_per_game": round(latest['AST'] / latest['GP'], 1),
        "games_played": int(latest['GP']),
    }
