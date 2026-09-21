import os
import socket
import time
import datetime


connections = {}

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host_name = socket.gethostname()
port = 5000
sock.bind((host_name,port))
sock.listen(2)

def clear():
    os.system("cls" if os.name == "nt" else "clear")
clear()

print(f"Server is listening on {host_name} {port}")


def show_client_information():
    client_ip , client_port = address[0] , address[1]
    connected_time = datetime.datetime.now()
    print('='* 20)
    print(f"Connection#{conn_id}")
    print('='* 20)
    print(f"IP:{client_ip}\nPort:{client_port} \
          \nServerPort:{port}\nDate:{connected_time.strftime("%d-%m-%Y")} \
          \nTime:{connected_time.strftime("%H:%M:%S")}")
    print('='* 20)

def keep_data_connection(id,enter, exit = None, status = False):
    client_ip , client_port = address[0] , address[1]
    connected_date = datetime.datetime.now()

    data =  {"id": id , 
             "client_ip":client_ip,"client_port":client_port,
             "date":connected_date.strftime("%d-%m-%Y"),
             "connect_time":enter,
             "exit_time":exit,
             "status" : status,
             "duration" : None
             }
    connections[id] = data

def connection_counter():
    for current_connection in range(1,100):
        yield current_connection

def history():
    for value in connections.values():
        print('-' *26)
        print(f"Connection#{value['id']:^}")
        print('-' *26)
        print(f"ID:{value['id']:<21d} | \nIP: {value["client_ip"]:<20s} | \
               \nDate:{value["date"]:<19s} | \nConnection_time:{value["connect_time"]} | \
               \nExit_time:{value["exit_time"]:<15s} | \
               \nDuration:{value["duration"]:<15.2f}") 
        print('-' *26)
counter = connection_counter()


while True:
    try:
        conn , address = sock.accept()
        conn_id = next(counter)
        start_connection_time = time.time()
        start_action = datetime.datetime.now().strftime("%H:%M:%S")
        keep_data_connection(conn_id,start_action,status=True)
        show_client_information()

        while True:
        
            recive_data = conn.recv(1024).decode()

            if recive_data.strip().lower() == "close" or not recive_data:
                print(f"Connection#{conn_id} disconnected")
                conn.close()
                break

            print(f"from connected user: {recive_data}")

            send_data = input(">")
            conn.send(send_data.encode())
        finish_action = datetime.datetime.now().strftime("%H:%M:%S")
        duration = time.time() - start_connection_time
        connections[conn_id].update({
            "exit_time": finish_action,
            "status": False,
            "duration": duration
            })
    except KeyboardInterrupt:
        print("Server Histoty:")
        history()
        print("\nServer Goodbye...")
        break


print()