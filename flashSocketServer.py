from tkinter import *
import socket
import easygui as g

def startLink():
    g.msgbox("succsee")

if __name__ == "__main__":
    tk = Tk()

    Label1 = Label(tk,text="用哪个端口收发？：")
    Text1 = Entry(tk)
    Button1 = Button(tk,text="Start Link",command=startLink())

    Label1.pack()
    Text1.pack()
    Button1.pack()

    tk.mainloop()