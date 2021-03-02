from collections import namedtuple

VaccineRecord = namedtuple(
    "VaccineRecord",
    ("available", "store_name", "store_address", "store_city", "link", "vaccine_types", "provider"),
)
