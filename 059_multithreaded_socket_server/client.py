import socket 


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

host_name = socket.gethostname()
port = 5000

sock.connect((host_name,port))



while True:

    msg = input(">")

    if msg.lower().strip() == "close":
        msg = "close"
        sock.sendall(msg.encode())
        sock.close()
        break    
    sock.sendall(msg.encode())

    recive_data = sock.recv(1024)

    print("Recived from server: " + recive_data.decode())


sock.close()