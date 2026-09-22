## Problem
Extend the socket chat server with:
- **Persistent accept loop** – keeps accepting clients until `Ctrl+C`.
- **Connection logging** – each session is written to `log.txt` (both on connect and disconnect).
- **Statistics report** – total, active, disconnected, unique IPs, average duration.
- **Search by connection ID** – look up a specific session.
- **Suspicious IP detection** – alert when an IP exceeds 5 connections.

## My Solution

The server now contains multiple helper functions, each with a focused responsibility:

| Function | Purpose |
|----------|---------|
| `show_client_information()` | Prints the current client's info |
| `keep_data_connection()` | Stores session metadata in `connections` dict |
| `connection_counter()` | Generates sequential connection IDs |
| `history()` | Prints all recorded sessions |
| `search(id)` | Looks up a session by ID |
| `write_in_log_file(log)` | Appends a string to `log.txt` |
| `statics()` | Computes and prints aggregate statistics |
| `ip_connection_count()` | Counts connections per IP |
| `sus_ip()` | Flags IPs with more than 5 connections |