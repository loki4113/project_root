# Makerspace Asset Ledger

## Overview

This project is a simple inventory event processing system for a makerspace environment.

The system reads inventory and event data from CSV files, processes checkout and return events, validates operations, tracks anomalies, and reconstructs the final inventory state.

The project was built using Python and focuses on:
- file processing
- event-driven logic
- state management
- validation
- report generation

---

## Features

The system supports:

- inventory loading from CSV
- event loading from CSV
- chronological event sorting
- checkout processing
- return processing
- duplicate event detection
- invalid return detection
- anomaly tracking
- final inventory reconstruction
- CSV report generation

---

## Project Structure

```text
project-root/
│
├── data/
│   ├── inventory.csv
│   ├── events.csv
│   └── policy.json
│
├── output/
│   ├── anomalies.csv
│   └── final_state.csv
│
├── src/
│   ├── main.py
│   ├── parser.py
│   ├── processor.py
│   └── reports.py
│
├── README.md
├── ASSUMPTIONS.md
├── TEST_PLANS.md
├── TRACE.md
└── AI_AND_ASSISTANCE.md
```

---

## How The System Works

1. Inventory data is loaded from `inventory.csv`
2. Event data is loaded from `events.csv`
3. Events are sorted chronologically
4. Each event is validated and processed
5. Inventory state is updated
6. Invalid operations are tracked as anomalies
7. Final reports are generated

---

## Technologies Used

- Python 3
- CSV module
- datetime module

---

## How To Run

From the project root directory:

```bash
python src/main.py
```

---

## Generated Output Files

### anomalies.csv

Contains invalid or rejected events such as:
- duplicate events
- invalid returns
- unavailable items
- unknown actions

---

### final_state.csv

Contains the reconstructed final inventory state after all valid events are processed.

---



## Error Handling

The system handles:
- invalid timestamps
- duplicate event IDs
- invalid returns
- unavailable items
- unknown actions

Invalid events are recorded as anomalies instead of crashing the system.



## Author

Victor Kipkemboi