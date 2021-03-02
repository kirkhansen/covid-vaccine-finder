import requests
import http.cookies

from covid_vaccine_finder.utils import VaccineRecord


def get_availability():
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://www.cvs.com/immunizations/covid-19-vaccine",
        "DNT": "1",
        "Connection": "keep-alive",
        "Sec-GPC": "1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
    }
    params = {"vaccineinfo": ""}
    res = requests.get(
        "https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.IA.json",
        headers=headers,
        params=params,
    )
    return res.json()["responsePayloadData"]["data"]["IA"]


def get_and_check():
    results = []
    availability = get_availability()
    for city in availability:
        if city["status"] == "Fully Booked":
            results.append(
                VaccineRecord(
                    available="no",
                    store_name=None,
                    store_address=None,
                    store_city=city["city"],
                    link="https://www.cvs.com/immunizations/covid-19-vaccine",
                    vaccine_types=None,
                    provider="CVS",
                )
            )
        else:
            results.append(
                VaccineRecord(
                    available="yes",
                    store_name=None,
                    store_address=None,
                    store_city=city["city"],
                    link="https://www.cvs.com/immunizations/covid-19-vaccine",
                    vaccine_types=None,
                    provider="CVS",
                )
            )
    return results


if __name__ == "__main__":
    res = get_and_check()
    for r in res:
        print(f"({r[0]}) {r.store_city}")
