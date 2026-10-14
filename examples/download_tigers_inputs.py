"""Obtain/cache three raw inputs. Setup helper only: no project analysis or answers."""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://statsapi.mlb.com/api/v1/"


def acquire(directory, name, url):
    path = directory / f"{name}.json"
    metadata = directory / f"{name}.metadata.json"
    if path.exists() and metadata.exists():
        record = json.loads(metadata.read_text())
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if record.get("url") == url and record.get("sha256") == digest:
            print(f"Using saved input: {path.name}")
            return json.loads(path.read_text())
        raise ValueError(f"Existing input/metadata mismatch for {name}; preserve and review before replacing")
    if path.exists() or metadata.exists():
        raise ValueError(f"Incomplete existing input for {name}; preserve and review before downloading")
    request = Request(url, headers={"User-Agent": "henry-baseball-learning/1.0"})
    with urlopen(request, timeout=30) as response:
        body = response.read()
        payload = json.loads(body)
        if not isinstance(payload, dict):
            raise ValueError("Expected a JSON object; no usable input saved")
        record = {"url": url, "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
                  "http_status": response.status, "bytes": len(body),
                  "sha256": hashlib.sha256(body).hexdigest()}
    path.write_bytes(body)
    metadata.write_text(json.dumps(record, indent=2) + "\n")
    print(f"Saved input: {path.name}")
    return payload


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "data" / "raw")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    common = BASE + "stats?stats=season&group=hitting&season=2025&sportIds=12"
    suffix = "&playerPool=ALL&limit=1000"
    team = acquire(args.output_dir, "mlb_erie_batting_2025", common + "&teamId=106" + suffix)
    acquire(args.output_dir, "mlb_eastern_batting_2025", common + "&leagueId=113" + suffix)
    splits = team["stats"][0]["splits"]
    ids = sorted({row["player"]["id"] for row in splits})
    if not ids or len(ids) > 50:
        raise ValueError("Unexpected biography sample size; ask mentor to review")
    acquire(args.output_dir, "mlb_erie_people_2025", BASE + "people?personIds=" + ",".join(map(str, ids)))
    print("Raw inputs ready. Henry still implements loading, validation, SQL, charts and findings.")


if __name__ == "__main__":
    main()
