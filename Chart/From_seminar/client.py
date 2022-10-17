import socket
import sys
import threading


def receive():
    global is_run
    while is_run:
        try:
            message = client.recv(1024).decode('UTF-8')
            if message == 'NICK':
                client.send(nickname.encode('UTF-8'))
            else:
                print(message)
        except:
            # Close Connection When Error
            sys.stderr.write('An error occurred!')
            client.close()
            break


def write():
    global is_run
    while is_run:
        userinput = input('')
        if userinput == 'Disconnect':
            message = f'{nickname}: {userinput}'
            client.send(message.encode('ASCII'))
            is_run = False
            client.close()
            continue
        message = f'{nickname}: {userinput}'
        client.send(message.encode('ASCII'))


nickname = input('Choose your nickname: ')
server_add = ('192.168.100.23', 9669)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect(server_add)
except:
    sys.stderr.write(
        f'Подключение не установлено, т.к. конечный компьютер {server_add[0]} отверг запрос на подключение')
    exit(-1)
is_run = True
receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()
