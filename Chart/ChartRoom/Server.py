import socket  # Import socket module
from concurrent.futures import thread
import threading


def on_new_client(clientsocket, addr):
    while True:
        msg = clientsocket.recv(1024)
        # do some checks and if msg == someWeirdSignal: break:
        print(addr, ' >> ', msg)
        # Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.
        clientsocket.send(msg)
    clientsocket.close()


host = '192.168.100.23'  # Get local machine name
port = 9669  # Reserve a port for your service.

print('Server started!')
print('Waiting for clients...')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
s.bind((host, port))  # Bind to the port
s.listen()  # Now wait for client connection.


while True:
    c, addr = s.accept()  # Establish connection with client.
    new_client_thread = threading.Thread(target=on_new_client)
    new_client_thread.start()
    print(f'Got connection from {addr}')
    # Note it's (addr,) not (addr) because second parameter is a tuple
    # Edit: (c,addr)
    # that's how you pass arguments to functions when creating new threads using thread module.
s.close()
