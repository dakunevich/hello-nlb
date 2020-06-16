#!/usr/bin/env python3
from datetime import datetime
import socket


# bind the socket to the port 6789
address = ('', 6789)
max_size = 1000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(1)

print(datetime.now(), ' Starting the server.')

while True:
    print('Waiting for a client to call.')
    connection, addr = server.accept()

    try:
        # show who connected to us
        print(datetime.now(), ' Connection from ', addr)

        while True:
            data = connection.recv(max_size)
            if data:
                # output received data
                print("Data: %s" % data)
            else:
                # no more data -- quit the loop
                print("no data.")
                break
    finally:
        # Clean up the connection
        connection.close()
