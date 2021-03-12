import json
import requests

from covid_vaccine_finder.utils import VaccineRecord


LOCATIONS = {
    "Clive": (41.5774667, -93.67753619999999),
    "Cedar Falls": (42.5348993, -92.4453161),
}


def get_vaccine_events():
    data = json.dumps(
        {
            "operationName": "GetActivePublicCovidVaccineEvents",
            "variables": {},
            "query": (
                "query GetActivePublicCovidVaccineEvents {\n"
                "    getActiveCovidVaccineEvents(where: {isPrivate: false}) {\n"
                "    covidVaccineEligibilityTerms\n"
                "    covidVaccineEventId\n"
                "    locationId\n"
                "    name\n"
                "    reservationStartDate\n"
                "    reservationEndDate\n"
                "    allowSecondTimeSlotReservation\n"
                "    availability {\n"
                "        covidVaccineManufacturerId\n"
                "        manufacturerName\n"
                "        hasAvailability\n"
                "        isSingleDose\n"
                "        __typename\n"
                "    }\n"
                "    details\n"
                "    phoneNumber\n"
                "    address {\n"
                "        addressLine1\n"
                "        addressLine2\n"
                "        city\n"
                "        state\n"
                "        zip\n"
                "        __typename\n"
                "        }\n"
                "        __typename\n"
                "    }\n"
                "}\n"
            ),
        }
    )
    response = requests.post(
        "https://www.hy-vee.com/my-pharmacy/api/graphql",
        data=data,
    )
    res = response.json()["data"]["getActiveCovidVaccineEvents"]
    return res


def get_pharmacies_with_vaccine(lat, lon):
    response = requests.post(
        "https://www.hy-vee.com/my-pharmacy/api/graphql",
        data=json.dumps(
            {
                "operationName": "SearchPharmaciesNearPointWithCovidVaccineAvailability",
                "variables": {"radius": 50, "latitude": lat, "longitude": lon},
                "query": (
                    "query SearchPharmaciesNearPointWithCovidVaccineAvailability("
                    "$latitude: Float!, $longitude: Float!, $radius: Int! = 40) {\n"
                    "  searchPharmaciesNearPoint(latitude: $latitude, "
                    "longitude: $longitude, "
                    "radius: $radius) {\n"
                    "    distance\n"
                    "    location {\n"
                    "      locationId\n"
                    "      name\n"
                    "      nickname\n"
                    "      phoneNumber\n"
                    "      businessCode\n"
                    "      isCovidVaccineAvailable\n"
                    "      address {\n"
                    "        line1\n"
                    "        line2\n"
                    "        city\n"
                    "        state\n"
                    "        zip\n"
                    "        latitude\n"
                    "        longitude\n"
                    "        __typename\n"
                    "      }\n"
                    "      __typename\n"
                    "    }\n"
                    "    __typename\n"
                    "  }\n"
                    "}\n"
                ),
            }
        ),
    )

    return response.json()["data"]["searchPharmaciesNearPoint"]


def get_vaccine_types(location_id):
    response = requests.post(
        "https://www.hy-vee.com/my-pharmacy/api/graphql",
        data=json.dumps(
            {
                "operationName": "GetCovidVaccineLocationAvailability",
                "variables": {"locationId": location_id},
                "query": (
                    "query GetCovidVaccineLocationAvailability($locationId: ID!) {\n"
                    "  getCovidVaccineLocationAvailability(locationId: $locationId) {\n"
                    "    covidVaccineManufacturerId\n"
                    "    manufacturerName\n"
                    "    hasAvailability\n"
                    "    isSingleDose\n"
                    "    __typename\n"
                    "  }\n"
                    "}\n"
                ),
            }
        ),
    )

    return [
        m["manufacturerName"]
        for m in response.json()["data"]["getCovidVaccineLocationAvailability"]
        if m["hasAvailability"]
    ]


def get_and_check():
    # TODO: this is getting a little gross. might be better to move this record building logic, or
    # have each response generator function here return the same types of objects
    results = []
    for search_location, coordinates in LOCATIONS.items():
        response = get_pharmacies_with_vaccine(*coordinates)
        for pharmacy in response:
            if pharmacy["location"]["isCovidVaccineAvailable"]:
                ", ".join(get_vaccine_types(pharmacy["location"]["locationId"]))
                results.append(
                    VaccineRecord(
                        available="yes",
                        store_name=pharmacy["location"]["name"],
                        store_address=pharmacy["location"]["address"]["line1"],
                        store_city=pharmacy["location"]["address"]["city"],
                        vaccine_types=", ".join(
                            get_vaccine_types(pharmacy["location"]["locationId"])
                        ),
                        link="https://www.hy-vee.com/my-pharmacy/covid-vaccine-consent",
                        provider="Hy-Vee",
                        doses_available=None,
                    )
                )
            else:
                results.append(
                    VaccineRecord(
                        available="no",
                        store_name=pharmacy["location"]["name"],
                        store_address=pharmacy["location"]["address"]["line1"],
                        store_city=pharmacy["location"]["address"]["city"],
                        vaccine_types=None,
                        link="https://www.hy-vee.com/my-pharmacy/covid-vaccine-consent",
                        provider="Hy-Vee",
                        doses_available=None,
                    )
                )
    # Add in events
    # TODO: May need to add in some filters for this to avoid out of state events
    for event in get_vaccine_events():
        if any(a["hasAvailability"] for a in event["availability"]):
            vaccine_types = (
                m["manufacturerName"]
                for m in event["availability"]
                if m["hasAvailability"]
            )
            results.append(
                VaccineRecord(
                    available="yes",
                    store_name=f"Event: {event['name']}",
                    store_address=event["address"]["addressLine1"],
                    store_city=event["address"]["city"],
                    vaccine_types=", ".join(vaccine_types),
                    link="https://www.hy-vee.com/my-pharmacy/covid-vaccine-consent",
                    provider="Hy-Vee",
                    doses_available=None,
                )
            )

    return results


if __name__ == "__main__":
    res = get_and_check()
    for r in res:
        print(f"({r[0]}) {r[1]}")
