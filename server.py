import socket
import threading
import sys
import webbrowser


class colors:
    RED   = "\033[1;31m"  
    BLUE  = "\033[1;34m"
    CYAN  = "\033[1;36m"
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"
    BOLD    = "\033[;1m"
    REVERSE = "\033[;7m"

sys.stdout.write(colors.RED)

HEADER = 8
PORT = 5050
SERVER = ""
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MSG = "!Disconnect"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(ADDR)

    def handle_connection(conn, addr):
        print(f"[NEW CONNECTION] {addr} connected.")

        connected = True
        while(connected):
            msg_lenght = conn.recv(HEADER).decode(FORMAT)
            match msg_lenght:
                case _:
                    msg_lenght = int(msg_lenght)
                    msg = conn.recv(msg_lenght).decode(FORMAT)
                    match msg:
                        case "Youtube":
                            webbrowser.open("https://www.youtube.com/")
                        case "Reddit":
                            webbrowser.open("https://www.reddit.com/")
                        case "!Disconnect":
                            connected = False
                    confirm(conn, msg)
                    print(f"Message received[{addr}] Message: {msg} ")
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
        match msg:
            case "!Disconnect":
                callback = "[SERVER] Disconnection confirmed!".encode(FORMAT)
            case _:
                callback = "[SERVER] Message received!".encode(FORMAT)
        
        callback_len = len(callback)
        send_lenght = str(callback_len).encode(FORMAT)
        send_lenght += send_lenght.ljust(HEADER - len(send_lenght))
        conn.send(send_lenght)
        conn.send(callback)

    if __name__ == '__main__':
        print("[STARTING] Server is starting...")
        start()
