"""
Problem #56: TCP Socket Chat - Client Side
Date: 2026-09-20

A simple TCP client that:
- Connects to the server running on the local hostname and port 5005.
- Sends messages typed by the user.
- Receives replies from the server.
- Exits when the user types "close".
"""

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_name = socket.gethostname()
port = 5005

sock.connect((host_name, port))

msg = input(">")

while msg.lower().strip() != "close":

    sock.sendall(msg.encode())

    recive_data = sock.recv(1024)

    print("Recived from server" + recive_data.decode())

    msg = input(">")

sock.close()