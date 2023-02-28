import socket
from _thread import *

HOST = "10.29.64.72"
PORT = 8282
FORMAT = "utf-8"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind((HOST, PORT))
except socket.error as e:
    print(e)

print("CONNECTING TO SERVER")
server.listen(2)


users = ['', '']
usernames = ['', '']
def thread_client(conn, user):
    usernames[user] = conn.recv(2048 * 10).decode(FORMAT)
    message = ""
    while True:
        try:
            data = conn.recv(2048 * 10).decode(FORMAT)
            if not data:
                print("DISCONNECTED")
                break
            else:
                users[user] = data[1]
                message = usernames[user] + ":" + users[user]
                print("Received ", data)
                print("Sending ", message)

            conn.sendall(str.encode(message))
        except:
            break

        print("Lost connection")
        conn.close()

currentUser = 0
while True:
    conn, addr = server.accept()
    print("Connection to ", addr)
    start_new_thread(thread_client, (conn, currentUser))
    currentUser += 1