from tkinter import *
import socket

def msgbox(msg:str)->Tk:
    msgbox = Tk()
    Label1 = Label(msgbox, text=msg)
    Label1.gird()
    msgbox.mainloop()

def startLink():
    port = int(Text1.get())
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(("localhost",port))
    server.listen(5)
    while True:
        pass
if __name__ == "__main__":
    tk = Tk()

    Label1 = Label(tk,text="用哪个端口收发？：")
    Text1 = Entry(tk)
    Button1 = Button(tk,text="Start Link",command=startLink)

    Label1.grid()
    Text1.grid()
    Button1.grid()

    tk.mainloop()