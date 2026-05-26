import csv



def write_anomalies(anomalies):

    with open(
        "output/anomalies.csv",
        "w",
        newline=""
    ) as file:

        fieldnames = [
            "event_id",
            "reason"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for anomaly in anomalies:

            writer.writerow(anomaly)



def write_final_state(items):

    with open(
        "output/final_state.csv",
        "w",
        newline=""
    ) as file:

        fieldnames = [
            "item_id",
            "start_status",
            "start_holder"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for item in items.values():

            writer.writerow({
                "item_id": item["item_id"],
                "start_status": item["start_status"],
                "start_holder": item["start_holder"]
            })