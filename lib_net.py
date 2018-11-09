# -*- coding:utf-8 -*-

import socket
import threading

class LIB_TCP:
    def __init__(self, port, funcRecv):
        self.__port = port
        self.__funcRecv = funcRecv

        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__threadRecv = threading.Thread(target=self.__recv)

    def start(self):
        self.__socket.bind(("0.0.0.0", self.__port))
        self.__socket.listen()
        self.__threadRecv.start()

    def stop(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("localhost", self.__port))
        s.send(bytes("exit".encode("utf8")))

    def __recv(self):
        while True:
            client, addr = self.__socket.accept()
            data = str(client.recv(1024), encoding="utf8")
            client.close()
            if data == "exit":
                print("收到结束命令")
                break
            self.__funcRecv(addr, data)
