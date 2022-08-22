import socket
HOST = '0.0.0.0'
PORT = 2222
isServerAlive = True
with socket.socket() as s:
    s.bind((HOST, PORT))
    s.listen(10)
    while isServerAlive:
        connection, address = s.accept()
        with connection:
            print('Connected by', address)
            while True:
                data = connection.recv(1024)
                if not data or 'close' in data.decode():
                    isServerAlive = False
                    break
                connection.sendall(data)