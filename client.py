
import socket

HEADER = 8
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MSG = "!Disconnect"
SERVER = "your-ip"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_lenght = len(message)

    send_lenght = str(msg_lenght).encode(FORMAT)
    send_lenght += send_lenght.ljust(HEADER - len(send_lenght))

    client.send(send_lenght)
    client.send(message)
    receive_confirmation()


def receive_confirmation():
    msg_lenght = client.recv(HEADER).decode(FORMAT)
    msg_lenght = int(msg_lenght)
    msg = client.recv(msg_lenght).decode(FORMAT)
    print(msg)


x = input("What do you want to send?")
send(x)
send(DISCONNECT_MSG)
