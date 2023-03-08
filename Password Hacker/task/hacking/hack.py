import socket
import sys
import random


abc = 'abcdefghijklmnopqrstuvwxyz0123456789'
args = sys.argv

with open(r'c:\Users\Lovis\PycharmProjects\Password Hacker\Password Hacker\task\passwords.txt', 'r') as file:
    passwords = [line for line in file.read().splitlines()]


def generate_password():
    '''function - generator of all passwords from dictionary'''
    for password in passwords:
        yield password.rstrip().lower()


def random_password():
    '''function - generating random password from dictionary'''
    pas = random.choice(list(generate_password()))
    uppers = []
    for i in range(len(pas)):
        uppers.append(random.randint(0, 1))

    return ''.join(
        pas[j].upper() if uppers[j] == 1
        else pas[j]
        for j in range(len(pas)))


with socket.socket() as client_socket:
    hostname = args[1]
    port = int(args[2])
    address = (hostname, port)
    client_socket.connect(address)
    while True:
        for i in range(1000000):
            password = random_password()
            client_socket.send(password.encode())

            response = client_socket.recv(1024)

            if response.decode() == 'Connection success!':
                print(password)
                exit()
            else:
                i += 1
                continue
