import calendar
import datetime
import requests
import time

from covid_vaccine_finder.utils import VaccineRecord


LOCATIONS = {
    "203496798588177": "Grimes Medicap",
    "203496319988170": "Easton Blvd Medicap",
    "203496387790166": "Ankeny Medicap",
    "203496311988162": "Altoona Medicap",
    "203496930188161": "Beaverdale Medicap",
    "203497206788164": "East 14th Medicap",
    "203496965888176": "Indianola Medicap",
    "203497248190157": "Waukee Medicap",
    "203497111390148": "Norwalk Medicap",
    "203496657588171": "Carlisle Medicap",
}


def check_availability(location_id):
    today = datetime.date.today()
    this_month = {
        "startDate": today.strftime("%Y-%m-01"),
        "endDate": today.strftime(
            "%Y-%m-{}".format(calendar.monthrange(today.year, today.month)[1])
        ),
    }
    # This will never happen, right?
    if today.month == 12:
        today_next_month = today.replace(month=1, year=today.year + 1)
    else:
        today_next_month = today.replace(month=(today.month + 1))
    next_month = {
        "startDate": today_next_month.strftime("%Y-%m-01"),
        "endDate": today_next_month.strftime(
            "%Y-%m-{}".format(
                calendar.monthrange(today_next_month.year, today_next_month.month)[1]
            )
        ),
    }

    dates_with_openings = []
    for date_range in (this_month, next_month):
        params = {
            "action": "getAppointments",
            "formID": location_id,
            "qid": "54",
            "timezone": "America/Chicago (GMT-06:00)",
            "ncTz": round(time.time() * 1000),
            "startDate": date_range["startDate"],
            "endDate": date_range["endDate"],
        }
        response = requests.get("https://hipaa.jotform.com/server.php", params=params)
        if not response.json()["content"]:
            return []
        for d, openings in response.json()["content"].items():
            if not openings:
                continue

            timeslots = [
                timeslot for timeslot, available in openings.items() if available
            ]
            if timeslots:
                dates_with_openings.append({d: timeslots})

    return dates_with_openings


def get_and_check():
    records = []
    for location_id, name in LOCATIONS.items():
        availability = check_availability(location_id)
        if availability:
            records.append(
                VaccineRecord(
                    available="yes",
                    store_name=name,
                    store_city=None,
                    store_address=None,
                    link=f"https://hipaa.jotform.com/{location_id}",
                    vaccine_types=None,
                    provider="Medicap",
                )
            )
        else:
            records.append(
                VaccineRecord(
                    available="no",
                    store_name=name,
                    store_city=None,
                    store_address=None,
                    link=f"https://hipaa.jotform.com/{location_id}",
                    vaccine_types=None,
                    provider="Medicap",
                )
            )

    return records


if __name__ == "__main__":
    res = get_and_check()
    for r in res:
        print(f"({r[0]}) {r[1]}")
