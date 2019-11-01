#!/usr/bin/env python3
import socket
import ssl


class TCPClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client = ssl.wrap_socket(self.client, ssl_version=ssl.PROTOCOL_TLSv1)
        self.client.connect((host, port))

    @staticmethod
    def receive(conn):
        response = ''
        while True:
            chunk = conn.recv(4096)
            response = response + chunk.decode('UTF-8')
            if len(chunk) < 4096:
                break
        return response

    def execute(self):
        while True:
            self.client.send(input().encode('UTF-8'))
            print(self.receive(self.client), end="")


x = TCPClient('127.0.0.1', 9999)
x.execute()