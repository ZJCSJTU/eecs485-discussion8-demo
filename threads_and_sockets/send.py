#!/usr/bin/python3

import socket

def send_message():
    # Construct a client socket object
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = "localhost"
    port = 8181
    # Connect to the server (listen.py)
    clientsocket.connect((host, port))

    # Send the executable file to the server
    clientsocket.send("./double.py".encode())
    
    # Wait for an acknowledgement message from the server
    msg = clientsocket.recv(1024)

    # Close the socket connection
    clientsocket.close()

    # Print the message received from the server
    print("listener said:")
    print (msg.decode('ascii'))

if __name__ == "__main__":
    send_message()