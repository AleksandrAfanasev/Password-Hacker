import socket
import sys


args = sys.argv
# working with a socket as a context manager
with socket.socket() as client_socket:
    hostname = args[1]
    port = int(args[2])
    address = (hostname, port)

    client_socket.connect(address)

    data = args[3].encode()

    client_socket.send(data)

    response = client_socket.recv(1024)

    response = response.decode()
    print(response)
