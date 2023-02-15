# echo-server.py
# testing
import sys
import socket
import selectors
import types
import traceback
from commslibs import Message

HOST = ""  # Standard loopback interface address (localhost)
PORT = 23232  # Port to listen on (non-privileged ports are > 1023)

chooser = selectors.DefaultSelector()

# host, port = sys.argv[1], int(sys.argv[2])
plug = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
plug.bind((HOST, PORT))
plug.listen()
print(f"Listening on {(HOST, PORT)}")
plug.setblocking(False)

chooser.register(plug, selectors.EVENT_READ, data=None)

def accept_wrapper(sock):
        conn, addr = sock.accept()  # Should be ready to read
        print(f"Accepted connection from {addr}")
        conn.setblocking(False)
        message = Message(chooser, conn, addr)
        chooser.register(conn, selectors.EVENT_READ, data=message)

######
def listenforcommands():
    try:
        while True:

            events = chooser.select(timeout=None)

            for key, mask in events:
                if key.data is None:
                    accept_wrapper(key.fileobj)
                else:
                    message = key.data
                    try:
                        message.process_events(mask)
                    except Exception:
                        print(
                            f"Main: Error: Exception for {message.addr}:\n"
                            f"{traceback.format_exc()}"
                        )
                        message.close()
    except KeyboardInterrupt:
        print("Caught keyboard interrupt, exiting")
    finally:
        chooser.close()





#  def listenforcommands():
#    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ears:
#        ears.bind((HOST, PORT))
#        print('Listening...')
#        ears.listen()
#        conn, addr = ears.accept()
#        with conn:
#            print(f"Connected by {addr}")
#            while True:
#                data = str(conn.recv(1024))
                
#                if not data:
#                    break
#                return(data)
#                # conn.sendall(data)
