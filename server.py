import socket
import threading
import webbrowser

HEADER = 8
PORT = 5050
SERVER = "your-ip"
CLIENTIP = "clients-ip"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MSG = "!Disconnect"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_connection(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while(connected):
        msg_lenght = conn.recv(HEADER).decode(FORMAT)
        if msg_lenght:
            msg_lenght = int(msg_lenght)
            msg = conn.recv(msg_lenght).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False
            if msg == "Youtube":
                webbrowser.open("https://www.youtube.com/")
            if msg == "Reddit":
                webbrowser.open("https://www.reddit.com/")
            confirm(conn, msg)
            print(f"[{addr}] {msg}")


    conn.close()


def start():
    server.listen() 
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_connection, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


def confirm(conn, msg):
    def send_msg(callback):
        callback_len = len(callback)
        send_lenght = str(callback_len).encode(FORMAT)
        #send_lenght += b" " * (HEADER - len(send_lenght))
        send_lenght += send_lenght.ljust(HEADER - len(send_lenght))
        conn.send(send_lenght)
        conn.send(callback)
    if(msg == DISCONNECT_MSG):
        callback = "[SERVER] Disconnection confirmed!".encode(FORMAT)
        send_msg(callback)
    else:
        callback = "[SERVER] Message received!".encode(FORMAT)
        send_msg(callback)





print("[STARTING] server is starting...")

start()
