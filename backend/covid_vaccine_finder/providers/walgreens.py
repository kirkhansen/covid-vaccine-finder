import pandas as pd
import requests

from covid_vaccine_finder.utils import VaccineRecord

# Scrape the vaxmaxx website
# This Walgreens auth is not built for programatic access, so use this
# since they clearly have something setup with walgreens.
URL = "https://www.vaxxmax.com/set_state_walgreens/IA"


def get_and_check():
    html = requests.get("https://www.vaxxmax.com/set_state_walgreens/IA").text
    raw_records = pd.read_html(html, flavor="html5lib")[0].to_dict(orient="records")
    records = [
        VaccineRecord(
            available="yes",
            store_name=None,
            store_city=record["Town / City"],
            store_address=record["Zip"].split()[0],
            link="https://www.walgreens.com/findcare/vaccination/covid-19/location-screening",
            vaccine_types=None,
            provider="Walgreens",
        )
        for record in raw_records
    ]
    return records


if __name__ == "__main__":
    res = get_and_check()
    for r in res:
        print(f"({r[0]}) {r[1]}")
