from stats.fetcher import get_player_stats
from pipeline.chain import analyze_splits

splits = get_player_stats("James Harden")
report = analyze_splits(splits)
print(report)