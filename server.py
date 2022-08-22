import socket
def data_receive(socket, stream_len):
    buffer = ""
    while len(buffer) < stream_len:
        chunk = socket.recv(stream_len - len(buffer))
        if chunk == '':
            raise RuntimeError("Broken chunk")
        buffer += chunk
    return buffer
if __name__ == "__main__":
    HOST = ''
    PORT = 2020
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