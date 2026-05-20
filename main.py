import sys
import os
from stats.fetcher import get_player_stats
from pipeline.chain import analyze_splits

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"Player Name\"")
        sys.exit(1)

    player_name = sys.argv[1]
    print(f"Fetching stats for {player_name}...")

    splits = get_player_stats(player_name)

    if splits["post_season"] is None:
        print(f"{player_name} has no playoff data.")
        sys.exit(1)

    print("Generating report...\n")
    report = analyze_splits(splits)

    # save to file
    os.makedirs("reports", exist_ok=True)
    filename = player_name.lower().replace(" ", "_") + ".md"
    filepath = os.path.join("reports", filename)

    with open(filepath, "w") as f:
        f.write(f"# {player_name} — Playoff vs Regular Season Report\n\n")
        f.write(report)

    print(report)
    print(f"\nReport saved to {filepath}")

if __name__ == "__main__":
    main()