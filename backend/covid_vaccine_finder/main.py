import json

from pathlib import Path
from itertools import chain

from covid_vaccine_finder.providers import cvs, hyvee, medicap

DATA_FILE = Path(Path(__file__).absolute().parent.parent.parent, "frontend/public/data.json")


def build_dataset_for_frontend():
    results = chain(hyvee.get_and_check(), medicap.get_and_check(), cvs.get_and_check())
    dict_records = [record._asdict() for record in results]
    with DATA_FILE.open("w") as f:
        json.dump(dict_records, f)


if __name__ == "__main__":
    build_dataset_for_frontend()
