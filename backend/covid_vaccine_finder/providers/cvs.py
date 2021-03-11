import json

import requests

from covid_vaccine_finder.utils import VaccineRecord

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.5",
    "Content-Type": "application/json",
    "Origin": "https://www.cvs.com",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": "https://www.cvs.com/vaccine/intake/store/cvd-store-select/first-dose-select",
    "Sec-GPC": "1",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
}
# Might be able to lump imzData with two records for each vaccine availability
# but the current response payload doesn't tell me which dose is available
# so i'll stick with two requests for now
REQUEST_DATA = {
    "requestMetaData": {
        "appName": "CVS_WEB",
        "lineOfBusiness": "RETAIL",
        "channelName": "WEB",
        "deviceType": "DESKTOP",
        "deviceToken": "7777",
        "apiKey": "a2ff75c6-2da7-4299-929d-d670d827ab4a",
        "source": "ICE_WEB",
        "securityType": "apiKey",
        "responseFormat": "JSON",
        "type": "cn-dep",
    },
    "requestPayloadData": {
        "selectedImmunization": ["CVD"],
        "distanceInMiles": 35,
        "imzData": [
            {
                "imzType": "CVD",
                "ndc": ["59267100002", "59267100003", "59676058015", "80777027399"],
                "allocationType": "1",
            }
        ],
        "searchCriteria": {"addressLine": "50111"},
    },
}
URL = "https://www.cvs.com/Services/ICEAGPV1/immunization/1.0.0/getIMZStores"


def get_availability():
    # Builds a dict of both first and second dose availability

    availability = {}
    allocationTypeMap = {"1": "first", "3": "second"}

    for allocationType in ("1", "3"):  # 1 is first dose, 3 is second dose
        request_data = REQUEST_DATA.copy()
        request_data["requestPayloadData"]["imzData"][0][
            "allocationType"
        ] = allocationType
        res = requests.post(
            URL,
            headers=HEADERS,
            data=json.dumps(request_data),
        )
        data = res.json()
        payload = data.get("responsePayloadData", {"locations": []})

        for loc in payload["locations"]:
            store_num = loc["StoreNumber"]
            if not store_num in availability:
                availability[store_num] = loc
            if availability[store_num].get("doses_available"):
                availability[store_num]["doses_available"].append(
                    allocationTypeMap[allocationType]
                )
            else:
                availability[store_num]["doses_available"] = [
                    allocationTypeMap[allocationType]
                ]
    return availability


def get_and_check():
    results = []
    availability = get_availability()
    for loc in availability.values():
        results.append(
            VaccineRecord(
                available="yes",
                store_name=loc["StoreNumber"],
                store_address=loc["addressLine"],
                store_city=loc["addressCityDescriptionText"],
                link="https://www.cvs.com/immunizations/covid-19-vaccine",
                vaccine_types=loc["mfrName"],
                provider="CVS",
                doses_available=",".join(loc["doses_available"]),
            )
        )
    return results


if __name__ == "__main__":
    res = get_and_check()
    for r in res:
        print(f"({r[0]}) {r.store_city}")
