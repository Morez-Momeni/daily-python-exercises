# Problem 56: TCP Socket Chat (Server & Client)

## Problem
Build a simple **TCP chat application** using Python's `socket` module. The system consists of two programs:
- **Server** – waits for a client to connect, then exchanges messages.
- **Client** – connects to the server, sends messages, and receives replies.

The chat continues until the client sends `"close"` or the connection is terminated.

## My Solution

I used `socket.AF_INET` (IPv4) and `socket.SOCK_STREAM` (TCP) for reliable, connection‑oriented communication.