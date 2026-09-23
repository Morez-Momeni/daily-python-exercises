import os
import socket
import threading
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

def keep_data_connection(id,enter, exit = None, status = "Disconnected"):
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
    return data


def connection_counter():
    for current_connection in range(1,100):
        yield current_connection

def history():
    clear()
    for value in connections.values():
        print('-' *26)
        print(f"Connection#{value['id']:^}")
        print('-' *26)
        print(f"ID:{value['id']} \nIP: {value["client_ip"]}\
               \nDate:{value["date"]}  \nConnection_time:{value["connect_time"]} \
               \nStatus:{value["status"]} \
               \nExit_time:{value["exit_time"]}\
               \nDuration:{value["duration"]}") 
        print('-' *26)

def search(id):

    result = connections.get(id)

    if result is not None:
        print("\n" + "=" * 45)
        print(f"              CONNECTION #{id}")
        print("=" * 45)
        print(f"IP Address   : {result['client_ip']}")
        print(f"Client Port  : {result['client_port']}")
        print(f"Date         : {result['date']}")
        print(f"Connected At : {result['connect_time']}")
        print(f"Exit Time    : {result['exit_time']}")
        print(f"Status       : {result['status']}")
        print(f"Duration     : {result['duration']}")
        print("=" * 45)

    else:
        print("\n" + "-" * 45)
        print(f"Connection #{id} not found")
        print("-" * 45)


def write_in_log_file(log):
    with open("log.txt",'a',encoding="utf-8") as file :
        file.write(f"{log}\n ")




def statics():
    
    def status():
        active = 0
        disconnected = 0
        for val in connections.values():
            if val["status"] == "Disconnected":
                disconnected += 1 
            else:
                active += 1
        return active , disconnected
    
    def uniqe_ip():
        
        ip_list = []
        for val in connections.values():
            if val["client_ip"] not in ip_list:
                ip_list.append(val["client_ip"])
        return len(ip_list)

    def avrage_duration():
        avr = None
        total_durations = 0
        number_of_connections = len(connections)
        for val in connections.values():
            total_durations += val["duration"]
        avr = total_durations / number_of_connections
        return avr

    all_connections = len(connections)
    active_connections , disconnect_connections = status()
    uniqe_ip_connections = uniqe_ip()
    connections_avrage_duration = avrage_duration()

    print("\n" + "=" * 55)
    print("                 CONNECTION STATISTICS")
    print("=" * 55)

    print(f"Total Connections   : {all_connections}")
    print(f"Active Connections  : {active_connections}")
    print(f"Disconnected        : {disconnect_connections}")
    print(f"Unique IP Addresses : {uniqe_ip_connections}")
    print(f"Average Duration    : {connections_avrage_duration:.2f} seconds")

    print("=" * 55)


def ip_connection_count():
    all_ip = []
    counted = []
    result = []
    for val in connections.values():
        all_ip.append(val["client_ip"])

    for ip in all_ip:
        if ip not in counted:
            counted_ip_number = all_ip.count(ip)
            counted.append(ip)
            result.append((ip,counted_ip_number))
    return result   



def sus_ip():

    def detection():
        sus_ips = []  
        all_ip = ip_connection_count()
        for item in all_ip:
            if item[1] > 5:
                sus_ips.append(item)
        return sus_ips
    sus_ip_detection = detection()
    if not sus_ip_detection:
        return False
    return sus_ip_detection
    
def handle_client(conn, address, conn_id):

    start_connection_time = time.time()
    start_action = datetime.datetime.now().strftime("%H:%M:%S")

    log = keep_data_connection(conn_id, start_action, status="Active")
    write_in_log_file(str(log))
    show_client_information()

    while True:

        recive_data = conn.recv(1024).decode()

        if recive_data.strip().lower() == "close" or not recive_data:
            print(f"Connection#{conn_id} disconnected")
            conn.close()
            break

        print(f"from connected user: {recive_data}")

        send_data = f"Server received: {recive_data}"
        conn.send(send_data.encode())

    finish_action = datetime.datetime.now().strftime("%H:%M:%S")
    duration = time.time() - start_connection_time

    connections[conn_id].update({
        "exit_time": finish_action,
        "status": "Disconnected",
        "duration": duration
    })

    write_in_log_file(str(connections[conn_id]))


counter = connection_counter()



while True:
    try:
        conn, address = sock.accept()

        conn_id = next(counter)

        suspicition_ip = sus_ip()

        if suspicition_ip:
            for ip, count in suspicition_ip:
                print("\n" + "=" * 55)
                print("                 SECURITY ALERT")
                print("=" * 55)
                print(f"IP Address : {ip}")
                print(f"Connections: {count}")
                print(f"Threshold  : 5")
                print("-" * 55)
                print("Warning: This IP has made too many connections.")
                print("=" * 55)

        thread = threading.Thread(
            target=handle_client,
            args=(conn, address, conn_id)
        )

        thread.start()

    except KeyboardInterrupt:
        print("Server Histoty:")
        history()
        print("\nServer Goodbye...")
        break
