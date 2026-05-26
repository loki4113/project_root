# Assumptions

The following assumptions were made during implementation:

- Events are processed chronologically after sorting by timestamp.
- Item IDs are unique.
- Event IDs should be unique.
- Items must be available before checkout.
- Items must be checked out before return.
- Invalid timestamps are skipped.
- Unknown items are rejected as anomalies.