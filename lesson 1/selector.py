import socket
from select import select
import selectors

HOST = '127.0.0.1'
PORT = 65432

selector = selectors.DefaultSelector()

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data = accept_connection)


def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()
    print(f'Подключение {addr}')
    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data = send_message)

def send_message(client_socket):
    request = client_socket.recv(1024)
    if request:
        print('Ответ клиента:', request.decode())
        client_socket.sendall('Hi'.encode())
    else:
        print('Клиент отключён')
        selector.unregister(client_socket)
        client_socket.close()
    
def event_loop():
    while True:
        events = selector.select()
        for key, _ in events:
            callback = key.data
            callback(key.fileobj)

if __name__ == '__main__':
    server()
    event_loop()