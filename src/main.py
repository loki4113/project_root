from parser import load_inventory, load_events
from processor import process_event

from reports import (
    write_anomalies,
    write_final_state
)



items = load_inventory("data/inventory.csv")



events = load_events("data/events.csv")



events.sort(
    key=lambda e: e["timestamp"]
)

anomalies = []

seen = set()

for event in events:

    
    if event["event_id"] in seen:

        anomalies.append({
            "event_id": event["event_id"],
            "reason": "DUPLICATE_EVENT"
        })

        print(
            f"Rejected {event['event_id']} - duplicate"
        )

        continue

    seen.add(event["event_id"])

    process_event(
        event,
        items,
        anomalies
    )

write_anomalies(anomalies)

write_final_state(items)

print("\nProcessing complete")
