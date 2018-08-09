# This is a unix domain socket example for wpa_supplicant

#!/usr/bin/env python
import socket
import sys
import os

#SERVER_PATH = "/tmp/python_unix_socket_server"
SERVER_PATH = "/var/run/wpa_supplicant/wlan0"
CLIENT_PATH = "/tmp/qooq"

try:
    os.unlink(CLIENT_PATH)
except IOError:
    if os.path.exists(CLIENT_PATH):
        raise

def recvall(sock, n):
    data = b''
    while len(data) < n:
        print("Q")
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data

def run_unix_domain_socket_client():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    sock.bind(CLIENT_PATH)
    # Connect the socket to the path where the server is listening
    server_address = SERVER_PATH 
    print("connecting to {:s}".format(server_address))
    try:
        sock.connect(server_address)
    except socket.error as msg:
        print(msg)
        sys.exit(1)

    try:
        message = "ATTACH"
        print("Sending [{!r}]".format(message))
        sock.sendall(bytes(message, 'utf-8'))
        data = sock.recv(1024)
        #print("Received [{:s}]".format(data))
        print("Received [{!r}]".format(data))
        #print("Received [%s]" % data)

        while 1:
            msg = input('Enter command\n')
            sock.sendall(bytes(msg, 'utf-8'))
            #data = sock.recv(1024)
            data = recvall(sock, 4)
            print("Received [{!r}]".format(data))

    finally:
        print ("Closing client")
        sock.close()

if __name__ == '__main__':
    run_unix_domain_socket_client()
