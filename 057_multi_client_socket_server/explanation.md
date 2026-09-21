# Problem 57: Multi‑Client Socket Server with Connection Logging

## Problem
Extend the basic TCP chat from Problem 56 to:
- Accept up to **3 sequential client connections**.
- For each connection, **display and store** client information (IP, port, connection date/time).
- Record the **exit time** when the client disconnects.
- Allow clients to terminate the session by sending `"close"`.

## My Solution

I used `socket`, `datetime`, and `os` to build the server, and kept the client from the previous exercise with a small modification (`close` handling).

### Server (`server.py`)

Key components:
- **`connections` dictionary** – stores metadata for each connection (id, IP, port, date, connect time, exit time).
- **`show_client_information()`** – prints the connection details on screen.
- **`keep_data_connection(id, enter, exit)`** – records connection data into the dictionary.
- **`connection_counter()` generator** – provides unique connection IDs (1 to 99).
- **Main loop** – accepts up to 3 clients sequentially, chats with each, and records the exit time.