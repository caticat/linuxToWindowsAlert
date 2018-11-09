# -*- coding:utf-8 -*-

import tkinter
import tkinter.messagebox
import threading

import lib_net

listenPort = 9999

def recv(addr, data):
    threading.Thread(target=alert, args=(addr, data)).start()

def alert(addr, data):
    tkinter.messagebox.showerror(addr, data)

if __name__ == "__main__":
    server = lib_net.LIB_TCP(listenPort, recv)
    server.start()
    root = tkinter.Tk()
    root.resizable(width=False, height=False)
    root.title("监听程序")
    label = tkinter.Label(root, text="  监听端口%s中...  " % listenPort)
    label.pack()
    root.mainloop()
    server.stop()
