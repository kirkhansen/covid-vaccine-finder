from datetime import datetime, timezone
from rfeed import Item, Guid, Feed


def available_records_generator(records):
    for record in records:
        if record.available == "yes":
            yield record


def generate_rss_feed(records):
    now_utc = datetime.now(timezone.utc)
    items = []
    for record in available_records_generator(records):
        description = f"""
        <h1>Vaccine availble</h1>
        <table>
          <tr>
            <th>Provider</th>
            <th>Store Name</th>
            <th>Store Address</th>
            <th>Store City</th>
            <th>Appointment Link</th>
          </tr>
          <tr>
            <td>{record.provider}</td>
            <td>{record.store_name}</td>
            <td>{record.store_address}</td>
            <td>{record.store_city}</td>
            <td><a href="{record.link}">{record.link}</a></td>
          </tr>
        </table>
        """

        item = Item(
            title="Vaccine Available",
            description=description,
            guid=Guid(
                f"{record.store_name}{record.store_address}{record.store_city}",
                isPermaLink=False,
            ),
            pubDate=now_utc,
        )
        items.append(item)

    feed = Feed(
        title="Covid Vaccine Finder Updates",
        link="https://kirkhansen.github.io/covid-vaccine-finder/",
        description="Feed produces new records when available vaccine is detected.",
        language="en-US",
        lastBuildDate=now_utc,
        items=items,
    )

    return feed


if __name__ == "__main__":
    from covid_vaccine_finder.utils import VaccineRecord

    records = [
        VaccineRecord(
            available="yes",
            store_name="test",
            store_city="des moines",
            store_address="test street",
            link="test.com",
            vaccine_types=None,
        ),
        VaccineRecord(
            available="no",
            store_name="test no",
            store_city="des moines",
            store_address="test no street",
            link="test.com",
            vaccine_types=None,
        )
    ]
    print(generate_rss_feed(records).rss())
