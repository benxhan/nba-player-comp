from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(model="claude-haiku-4-5-20251001")

prompt = ChatPromptTemplate.from_template("""
    You are an NBA analyst. A player's career regular season and playoff stats are below.
    Write a scouting report analyzing how their game changes in the postseason. Do not overuse flowerly language, keep it concise and use basketball terminology.

    Player: {name}

    Regular Season (career averages over {reg_gp} games):
    - Minutes per game: {reg_mpg}
    - Points per game: {reg_ppg}
    - Rebounds per game: {reg_rpg}
    - Assists per game: {reg_apg}
    - FG%: {reg_fg}%
    - Free throws attempted per game: {reg_fta}

    Playoffs (career averages over {post_gp} games):
    - Minutes per game: {post_mpg}
    - Points per game: {post_ppg}
    - Rebounds per game: {post_rpg}
    - Assists per game: {post_apg}
    - FG%: {post_fg}%
    - Free throws attempted per game: {post_fta}

    Analyze the following specifically:
    1. Scoring — does this player step up or shrink in the playoffs?
    2. Role and usage — do their minutes increase, suggesting the team leans on them more?
    3. Aggression — does their FTA go up, showing they attack the basket more under pressure?
    4. Efficiency — does their FG% hold up or drop?

    End with:
    - listing all of the above stats as displayed above
    - a clear verdict on whether this is a true playoff performer.
""")

chain = prompt | llm

def analyze_splits(splits: dict) -> str:
    reg = splits["regular_season"]
    post = splits["post_season"]

    response = chain.invoke({
        "name": splits["name"],
        "reg_gp": reg["games_played"],
        "reg_mpg": reg["min_per_game"],
        "reg_ppg": reg["points_per_game"],
        "reg_rpg": reg["rebounds_per_game"],
        "reg_apg": reg["assists_per_game"],
        "reg_fg": reg["fg_pct"],
        "reg_fta": reg["free_throws_attempted_per_game"],
        "post_gp": post["games_played"],
        "post_mpg": post["min_per_game"],
        "post_ppg": post["points_per_game"],
        "post_rpg": post["rebounds_per_game"],
        "post_apg": post["assists_per_game"],
        "post_fg": post["fg_pct"],
        "post_fta": post["free_throws_attempted_per_game"],
    })
    return response.content