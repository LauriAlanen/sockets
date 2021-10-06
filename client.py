import socket

HEADER = 8
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MSG = "!Disconnect"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_lenght = len(message)
    send_lenght = str(msg_lenght).encode(FORMAT)
    send_lenght += b" " * (HEADER - len(send_lenght))
    client.send(send_lenght)
    client.send(message)
send("Tietokone")
send(DISCONNECT_MSG)
