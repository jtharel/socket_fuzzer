#!/usr/bin/env python3

import socket

print("Script to fuzz a network socket")
address = "192.168.1.194"
port = 9999
command = b"XXXX " #b is binary

sock = socket.socket(); 
conn = sock.connect((address, port))

for x in range(4, 100000, 4):
	message = command + b"A" * x
	print("Sending command", command, "with arg length", x)
	sock.sendall(message)
	resp = sock.recv(4096)
	print("Response Received:", resp)

