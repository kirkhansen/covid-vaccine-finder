import json
import requests


LOCATIONS = {
    "Clive": (41.5774667, -93.67753619999999),
    "Cedar Falls": (42.5348993, -92.4453161),
}


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


def get_and_check(quiet=True):
    output = []
    for search_location, coordinates in LOCATIONS.items():
        if not quiet:
            output.append("\n")
            output.append(f"Checking {search_location}...")
            output.append("---")

        response = get_pharmacies_with_vaccine(*coordinates)
        for pharmacy in response:
            if pharmacy["location"]["isCovidVaccineAvailable"]:
                output.append("\n")
                output.append("!!! AVAILABLE !!!")
                output.append(pharmacy["location"]["name"])
                output.append(pharmacy["location"]["address"]["line1"])
                output.append(
                    f"{pharmacy['location']['address']['city']}, {pharmacy['location']['address']['state']}"
                )
                output.append(
                    "Vaccine types: "
                    + ", ".join(get_vaccine_types(pharmacy["location"]["locationId"]))
                )
                output.append(
                    "Go to https://www.hy-vee.com/my-pharmacy/covid-vaccine-consent"
                )
            elif not quiet:
                output.append(f"(no) {pharmacy['location']['name']}")

    return output


if __name__ == "__main__":
    print("\n".join(get_and_check(quiet=False)))
