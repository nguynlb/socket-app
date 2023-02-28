import socket
from _thread import *
HOST = "172.20.142.208"
PORT = 8282
FORMAT = "utf-8"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
username = input("Username :")
try:
    client.connect((HOST, PORT))
    client.send(str.encode(username))
except socket.error as e:
    print(e)

def receive_message(username):
    message = client.recv(2048 * 10).decode(FORMAT)
    print(message)


message = ""
while True:
    start_new_thread(receive_message, (username,))
    message = input(f"{username} :")
    client.send(str.encode(message))

