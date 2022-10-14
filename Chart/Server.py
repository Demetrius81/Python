import socket

soc = ('localhost', 9669)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(soc)
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f'Connected to {addr}')
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
