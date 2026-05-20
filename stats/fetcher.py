from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats

# goal: find out player regular season vs post season
def get_player_stats(player_name : str):
    # find player
    matches = players.find_players_by_full_name(player_name)
    if not matches:
        raise ValueError(f"Player '{player_name}' not found")
    
    player = matches[0]
    career = playercareerstats.PlayerCareerStats(player_id=player['id'])

    reg_df = career.season_totals_regular_season.get_data_frame()
    post_df = career.season_totals_post_season.get_data_frame()

    latest_reg = reg_df #.iloc[-1]
    latest_post = post_df #.iloc[-1]

    # games played, min/game, ppg, rpg, apg, fg % (efficency), fta, 
    def season_avgs(df):
        totals = df[['GP', 'MIN', 'PTS', 'REB', 'AST', 'FGA', 'FGM', 'FTA']].sum()
        gp = totals['GP']

        return {
            "games_played": int(gp),
            "min_per_game": float(round(totals['MIN'] / gp, 1)),
            "points_per_game": float(round(totals['PTS'] / gp, 1)),
            "rebounds_per_game": float(round(totals['REB'] / gp, 1)),
            "assists_per_game": float(round(totals['AST'] / gp, 1)),
            "fg_pct": float(round(totals['FGM'] / totals['FGA'] * 100, 1)),
            "free_throws_attempted_per_game": float(round(totals['FTA'] / gp, 1))
        }

    return {
        "name": player['full_name'],
        "regular_season": season_avgs(latest_reg),
        "post_season": season_avgs(latest_post) if not post_df.empty else None
    }
