# echo-server.py
# testing
import socket

HOST = ""  # Standard loopback interface address (localhost)
PORT = 23232  # Port to listen on (non-privileged ports are > 1023)
def listenforcommands():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ears:
        ears.bind((HOST, PORT))
        print('Listening...')
        ears.listen()
        conn, addr = ears.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = str(conn.recv(1024))
                
                if not data:
                    break
                return(data)
                # conn.sendall(data)
