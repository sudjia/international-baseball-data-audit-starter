"""Small unrelated teaching query; do not count it as a portfolio deliverable."""
from pathlib import Path
import duckdb
import pandas as pd


def main():
    root = Path(__file__).resolve().parents[1]
    players = pd.read_csv(root / "data" / "practice" / "players.csv", dtype={"player_id": "string"})
    with duckdb.connect(":memory:") as connection:
        connection.register("practice_players", players)
        rows = connection.execute("""
            SELECT practice_role, COUNT(*) AS people
            FROM practice_players
            WHERE practice_age >= 22
            GROUP BY practice_role
            ORDER BY people DESC, practice_role
        """).fetchall()
    print("Invented teaching data only:", rows)


if __name__ == "__main__":
    main()
