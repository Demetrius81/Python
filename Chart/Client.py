import socket

soc = ('localhost', 9669)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(soc)
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data!r}")
