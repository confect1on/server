import socket
import threading
import time

def connection_handler(conn, addr):
    with conn:
        print('Connection to', addr, "is open")
        while True:
            data = conn.recv(1024)
            if not data or 'close' in data.decode():
                break
            conn.sendall(data)
        print("Connection to", addr, "is closed")


HOST = '0.0.0.0'
PORT = 2222
isServerAlive = True
with socket.socket() as s:
    s.bind((HOST, PORT))
    s.listen(10)
    while True:
        connection, address = s.accept()
        thread = threading.Thread(target=connection_handler, args=(connection, address))
        thread.start()
