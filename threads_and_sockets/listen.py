#!/usr/bin/python3
import socket
import sh
from threading import Thread
from threading import Lock
from time import sleep

WORK_ARR = []
# Locks are a synchronization primitive used to protect the global WORK_ARR data structure
# NOTE: LOCKS ARE NOT NEEDED IN P4!!!!! (they are, however, needed for this example)
WORK_ARR_lock = Lock()

def listen():
    # Construct a socket object
    serversocket = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)

    host = 'localhost'
    port = 8181

    # Bind the socket to a port number
    # Similar to linking a phone to a phone number
    serversocket.bind((host, port))

    # Starts the socket listening for connection requests
    # This does not block, it simply allows connections to be made
    serversocket.listen()
    print('Server socket is listening')

    while True:
        # Establish a connection upon receiving a request
        # Similar to answering a phone when it rings
        # The following blocks until a connection is requested in the request queue
        # https://github.com/python/cpython/blob/master/Lib/socket.py#L205-L219
        clientsocket, addr = serversocket.accept()
        print('Connection request accepted from: {}'.format(addr))

        # Receive the message from the sender
        # The following blocks until recv buffer is non-empty
        data = clientsocket.recv(1024).decode()
        print('Message: {}'.format(data))

        # Lock the global data structure
        WORK_ARR_lock.acquire()
        WORK_ARR.append({
            'in': './input.txt',
            'out': './output.txt',
            'exe': data
        })
        # Release the lock after modifying
        WORK_ARR_lock.release()

        msg = 'Gonna do that work\r\n'
        # Send an acknowledgement message back to send.py
        clientsocket.send(msg.encode('ascii'))
        clientsocket.close()

def look_for_work():
    while True:
        if WORK_ARR:
            WORK_ARR_lock.acquire()
            work = WORK_ARR[-1]
            del WORK_ARR[-1]
            WORK_ARR_lock.release()

            print('Doing work now for: {}'.format(work['exe']))
            do_work(work['exe'], work['in'], work['out'])
        else:
            print('No work to do')

        # Avoid busy-waiting
        sleep(5)

def do_work(exe, in_f_name, out_f_name):
    in_file = open(in_f_name, 'r')
    out_file = open(out_f_name, 'w')

    # Run executable file from shell
    executable = sh.Command(exe)
    executable(_in=in_file, _out=out_file)

    in_file.close()
    out_file.close()
    print('Finished doing work for: {}'.format(exe))

if __name__ == '__main__':
    t = Thread(target=listen)
    t.start()

    t2 = Thread(target=look_for_work)
    t2.start()

