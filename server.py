import socket
import threading


def connection_handler(conn, addr):
    global isServerAlive
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                if  'close' in data.decode():
                    isServerAlive = False
                break
            conn.sendall(data)


HOST = '0.0.0.0'
PORT = 2222
isServerAlive = True
with socket.socket() as s:
    s.bind((HOST, PORT))
    s.listen(10)
    while isServerAlive:
        connection, address = s.accept()
        thread = threading.Thread(target=connection_handler, args=(connection, address))
        thread.start()
