import json

from datetime import datetime, timezone
from pathlib import Path
from itertools import chain

from covid_vaccine_finder.providers import cvs, hyvee, medicap, walgreens
from covid_vaccine_finder.rss_feed import generate_rss_feed

DATA_FILE = Path(
    Path(__file__).absolute().parent.parent.parent, "frontend/public/data.json"
)
LAST_UPDATED_FILE = Path(
    Path(__file__).absolute().parent.parent.parent, "frontend/public/last-updated.json"
)
RSS_FEED_FILE = Path(
    Path(__file__).absolute().parent.parent.parent, "frontend/public/feed.xml"
)


def build_dataset_for_frontend():
    results = list(chain(
        hyvee.get_and_check(),
        medicap.get_and_check(),
        cvs.get_and_check(),
        walgreens.get_and_check(),
    ))
    dict_records = [record._asdict() for record in results]
    with DATA_FILE.open("w") as f:
        json.dump(dict_records, f)
    save_rss_feed(results)


def save_rss_feed(records):
    feed_xml = generate_rss_feed(records).rss()
    with RSS_FEED_FILE.open("w") as f:
        f.write(feed_xml)


def save_last_updated_time():
    with LAST_UPDATED_FILE.open("w") as f:
        json.dump({"last_updated": datetime.now(timezone.utc).timestamp()}, f)


if __name__ == "__main__":
    build_dataset_for_frontend()
    save_last_updated_time()
