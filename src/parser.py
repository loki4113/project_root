import csv

from datetime import datetime

def load_inventory(path):

    items = {}

    with open(path) as file:

        reader = csv.DictReader(file)

        for row in reader:

            items[row["item_id"]] = row

    return items


def load_events(path):

    events = []

    with open(path) as file:

        reader = csv.DictReader(file)

        for row in reader:

            try:

                row["timestamp"] = datetime.fromisoformat(
                    row["timestamp"]
                )

                events.append(row)

            except:

                print(
                    f"Invalid timestamp "
                    f"{row['event_id']}"
                )

    return events