# Problem 59: Multithreaded Socket Server with Logging, Statistics & Security Alerts

## Problem
Extend the socket chat server to support **multiple simultaneous clients** using threads, while preserving all the reporting features from the previous version:
- Session logging to disk (`log.txt`).
- Connection history.
- Lookup by connection ID.
- Aggregate statistics.
- Suspicious IP detection (threshold: 5 connections).

The client remains the same as before.

## My Solution

The key architectural change is the introduction of **`threading.Thread`** to handle each client in a separate thread. This allows the server to accept a new connection while an existing client is still chatting.

### Main Changes

1. **`handle_client(conn, address, conn_id)`** – encapsulates the entire client session logic. Each accepted connection spawns a new thread that runs this function.
2. **Automatic reply** – the server no longer prompts for input; instead, it automatically replies with `"Server received: <message>"`. This makes the server fully concurrent (no `input()` blocking the loop).
3. **Security check before thread spawn** – `sus_ip()` is called right after `accept()`, and an alert is printed if any IP exceeds the threshold.
4. **`thread.start()`** – launches the new thread; the main loop immediately returns to `accept()` and waits for the next client.