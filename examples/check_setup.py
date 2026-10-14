"""Environment smoke check using only invented inputs; no real analysis."""
import os
from pathlib import Path
import sys
import tempfile

# Some cloud hosts have a read-only home; matplotlib needs a writable cache.
os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "henry-starter-mpl"))
import duckdb
import matplotlib
import pandas as pd
import pytest


def main():
    root = Path(__file__).resolve().parents[1]
    players = pd.read_csv(root / "data" / "practice" / "players.csv", dtype={"player_id": "string"})
    with duckdb.connect(":memory:") as connection:
        connection.register("practice_players", players)
        count = connection.execute("SELECT COUNT(*) FROM practice_players").fetchone()[0]
    if count != len(players) or not count:
        raise RuntimeError("Practice table registration/read failed")
    print(f"Python {sys.version.split()[0]}; pandas {pd.__version__}; DuckDB {duckdb.__version__}")
    print(f"matplotlib {matplotlib.__version__}; pytest {pytest.__version__}")
    print("Setup works with invented practice data. No real input or project result was validated.")


if __name__ == "__main__":
    main()
