from parser import load_inventory, load_events
from processor import process_event

from reports import (
    write_anomalies,
    write_final_state
)


# Load inventory
items = load_inventory("data/inventory.csv")


# Load events
events = load_events("data/events.csv")


# Sort events by timestamp
events.sort(
    key=lambda e: e["timestamp"]
)


# Store anomalies
anomalies = []


# Track duplicates
seen = set()


# Process events
for event in events:

    # Duplicate detection
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


# Create output files
write_anomalies(anomalies)

write_final_state(items)


print("\nProcessing complete")
