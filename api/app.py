from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from stats.fetcher import get_player_stats
from pipeline.chain import analyze_splits

app = FastAPI(title="NBA Comparer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PlayerQuery(BaseModel):
    name: str


@app.post("/api/player")
async def analyze_player(query: PlayerQuery):
    try:
        splits = get_player_stats(query.name)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    report = None
    if splits.get("post_season") is None:
        report = "No playoff data available for this player."
    else:
        report = analyze_splits(splits)

    return {
        "name": splits["name"],
        "regular_season": splits["regular_season"],
        "post_season": splits["post_season"],
        "report": report,
    }


@app.get("/api/player/{name}")
async def get_player(name: str):
    try:
        splits = get_player_stats(name)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    report = None
    if splits.get("post_season") is None:
        report = "No playoff data available for this player."
    else:
        report = analyze_splits(splits)

    return {
        "name": splits["name"],
        "regular_season": splits["regular_season"],
        "post_season": splits["post_season"],
        "report": report,
    }
