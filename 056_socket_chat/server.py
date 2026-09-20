"""
Problem #56: TCP Socket Chat - Server Side
Date: 2026-09-20

A simple TCP server that:
- Binds to the local hostname on port 5005.
- Listens for one incoming connection.
- Exchanges messages with the connected client in a loop.
- Closes the connection when the client disconnects.
"""

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
port = 5005

sock.bind((host_name, port))
sock.listen(2)

print(f"Server is listening on {host_name} {port}")

conn, address = sock.accept()
print(f"Connection from: {address}")

while True:
    recive_data = conn.recv(1024).decode()

    if not recive_data:
        break
    print(f"from connected user: {recive_data}")

    send_data = input(">")
    conn.send(send_data.encode())

conn.close()