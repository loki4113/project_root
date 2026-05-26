# Process events
def process_event(
    event,
    items,
    anomalies
):

    action = event["action"]

    item_id = event["item_id"]


    # Reject unknown item
    if item_id not in items:

        anomalies.append({
            "event_id": event["event_id"],
            "reason": "UNKNOWN_ITEM"
        })

        return


    item = items[item_id]


    # CHECKOUT
    if action == "CHECKOUT":

        if item["start_status"] != "available":

            anomalies.append({
                "event_id": event["event_id"],
                "reason": "ITEM_NOT_AVAILABLE"
            })

            return


        item["start_status"] = "checked_out"

        item["start_holder"] = event["actor_id"]

        print(f"{item_id} checked out")


    # RETURN
    elif action == "RETURN":

        if item["start_status"] != "checked_out":

            anomalies.append({
                "event_id": event["event_id"],
                "reason": "INVALID_RETURN"
            })

            return


        item["start_status"] = "available"

        item["start_holder"] = ""

        print(f"{item_id} returned")