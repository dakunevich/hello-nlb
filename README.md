# Simple service with tcp port open

Docker image expecting connection on TCP Port 6789. Supposed to be tested with ECS Service and NLB

To build a Docker image from the Dockerfile, run the following command from inside this directory

```sh
$ docker build -t <docker-hub-username>/hello-nlb .
```
This will produce the following output

```sh
Sending build context to Docker daemon  11.62MB
Step 1/4 : FROM python:3.7-alpine
 ---> e854017db514
Step 2/4 : ADD tcp_server.py /
 ---> 375a6d2489f3
Step 3/4 : EXPOSE 6789
 ---> Running in 07717bca5170
Removing intermediate container 07717bca5170
 ---> 034601e370c4
Step 4/4 : CMD [ "python", "./tcp_server.py" ]
 ---> Running in 4e522be61137
Removing intermediate container 4e522be61137
 ---> 845cb8341d08
Successfully built 845cb8341d08
```

To run the image in a Docker container, use the following command
```sh
$ docker run -itd --name hello-nlb --publish 6789:6789 <docker-hub-username>/hello-nlb:1.0
Starting the server at  2020-05-28 13:20:03.655402
Waiting for a client to call.

$ telnet localhost 6789
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
hey


connection from ('172.17.0.1', 35706)
Data: b'hey\r\n'
```
