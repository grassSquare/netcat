#-*- coding:utf-8 -*-
import socket
import os, sys
import easygui as g
try:
    from tkinter import *
except ImportError:  #Python 2.x
    PythonVersion = 2
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    PythonVersion = 3
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()

listen: bool = False
target: str = ""
port: int = 0


class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('设置连接')
        self.master.geometry('304x202')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('Label1.TLabel',anchor='w', font=('宋体',9))
        self.Label1 = Label(self.top, text='目标ip：', style='Label1.TLabel')
        self.Label1.place(relx=0.026, rely=0.04, relwidth=0.266, relheight=0.124)

        self.Text1Var = StringVar(value='')
        self.Text1 = Entry(self.top,textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.place(relx=0.526, rely=0.04, relwidth=0.451, relheight=0.124)

        self.style.configure('Label2.TLabel',anchor='w', font=('宋体',9))
        self.Label2 = Label(self.top, text='目标port：', style='Label2.TLabel')
        self.Label2.place(relx=0.026, rely=0.198, relwidth=0.24, relheight=0.084)

        self.Text2Var = StringVar(value='')
        self.Text2 = Entry(self.top,textvariable=self.Text2Var, font=('宋体',9))
        self.Text2.place(relx=0.526, rely=0.198, relwidth=0.451, relheight=0.124)

        self.style.configure('Command1.TButton',font=('宋体',9))
        self.Command1 = Button(self.top, text='测试连接', command=self.Command1_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.026, rely=0.356, relwidth=0.345, relheight=0.163)

        self.style.configure('Label3.TLabel',anchor='w', font=('宋体',9))
        self.Label3 = Label(self.top, style='Label3.TLabel')
        self.Label3.place(relx=0.395, rely=0.356, relwidth=0.398, relheight=0.163)

        self.style.configure('Command2.TButton',font=('宋体',9))
        self.Command2 = Button(self.top, text='连接', command=self.Command2_Cmd, style='Command2.TButton')
        self.Command2.place(relx=0.026, rely=0.554, relwidth=0.345, relheight=0.163)

        self.Text3Var = StringVar(value='')
        self.Text3 = Entry(self.top, textvariable=self.Text3Var, font=('宋体',9))
        self.Text3.place(relx=0.395, rely=0.554, relwidth=0.556, relheight=0.401)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Command1_Cmd(self, event=None):
        #TODO, Please finish the function here!
        print("exed")
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        global target
        global port
        try:
            target = str(self.Text1.get())
            port = int(self.Text2.get())
        except:
            g.msgbox("请输入ip及port")
        print(target,port)
        try:
            client.connect((target, port))
            client.send("sss")
        except:
            print("fail")
            self.Label3.config(text="连接失败" )#label3.text = "fail"

    def Command2_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
    try: top.destroy()
    except: pass
