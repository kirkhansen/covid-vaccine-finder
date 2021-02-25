import requests
import http.cookies


AUTH_COOKIES = "QuantumMetricSessionLink=https://cvs.quantummetric.com/#/users/search?autoreplay=true&qmsessioncookie=6c2984a337fe6370468bd7e94759e51d&ts=1613638149-1613724549; pe=p1; acctdel_v1=on; adh_new_ps=on; adh_ps_pickup=on; adh_ps_refill=on; buynow=off; sab_displayads=on; db-show-allrx=on; disable-app-dynamics=on; disable-sac=on; dpp_cdc=off; dpp_drug_dir=off; dpp_sft=off; getcust_elastic=on; echome_lean6=off-p0; enable_imz=on; enable_imz_cvd=on; enable_imz_reschedule_instore=off; enable_imz_reschedule_clinic=off; …9159FE5FE26~YAAQN9vJF7aPaLV3AQAAAE8v2woOOexo9mm9r1390AGTP/13GcOeO8z3P+X2trZ9PdrOj4++wFMEqMI2s0XDLlRQ5qxEcxn+wHMJCSy+YyEudUVBsQ5hI3Ouv4cw0O+lQ+MBJ4liTvIg2e/8+oEjoCvrI3I2/pEx5VugUO0q7LbpwfUC3gxe3cHwMjZl; gbi_sessionId=ckllem4yl00001w7wogkyay2j; bm_sv=43E776430AEE369E7374E37326F5E6E4~/h5EenCp/L2cxzXwy4XrnM2r3QRjSK0bm+QOQ20YfcLOL3TkmG/FB/tUccP/LPXFm2qzqM+Ciug+EQreog7XvlWPnFEaJxGtHxbvaAsFXHyAyjGVTgRn6v4oERDOww/W3uzkaafcNwDwpdbemz8xaA==; qmexp=1614291892555; QuantumMetricSessionID=919c2bd015639e9fca2b3cf466de70b1"
COOKIE_JAR = requests.cookies.RequestsCookieJar()
COOKIE_JAR.update(http.cookies.SimpleCookie(http.cookies.SimpleCookie(AUTH_COOKIES)))


def get_availability():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.cvs.com/immunizations/covid-19-vaccine',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Sec-GPC': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }
    params = {"vaccineinfo": ""}
    res = requests.get(
        "https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.IA.json",
        headers=headers,
        params=params,
        cookies=COOKIE_JAR.get_dict()
    )
    return res.json()["responsePayloadData"]["data"]["IA"]

def check_availability():
    results = []
    availability = get_availability()
    for city in availability:
        if city["status"] == "Fully Booked":
            results.append(("no", city["city"]))
        else:
            results.append(("yes", city["city"]))
    return results


if __name__ == "__main__":
    res = check_availability()
    for r in res:
        print(f"({r[0]}) {r[1]}")
