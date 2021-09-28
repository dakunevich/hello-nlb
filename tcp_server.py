#!/usr/bin/env python3
from datetime import datetime
import signal, socket, sys, time

def handler(signum, frame):
    """ Catch <ctll+c> signal for clean stop"""
    print('\nGracefully shutdown...')
    server.close()
    sys.exit(0)

signal.signal(signal.SIGINT, handler)

# bind the socket to the port 6789
address = ('', 6789)
max_size = 4096 # 4 KiB

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(1)

print(datetime.now(), '--- Starting the server. ---')

while True:
    print(datetime.now(), 'Waiting for a client to call.')
    connection, addr = server.accept()

    try:
        # show who connected to us
        print(datetime.now(), 'Connection from ', addr)
        
        while True:
            data = b''
            part = connection.recv(max_size)
            data += part
            if data:
                # output received data
                print(datetime.now(), "Data: %s" % data)
            else:
                # no more data -- quit the loop
                print(datetime.now(), "--- no data. Bye! ---")
                break
    except KeyboardInterrupt:
        print("^C received")
        sys.exit(1)
    finally:
        # Clean up the connection
        connection.close()
