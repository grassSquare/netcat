from tkinter import *
import socket
class Application_ui(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('设置连接')
        self.master.geometry('304x202')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.Label1 = self.Label(self.Frame, text="Password: ")
        self.Text1 = Entry(self.Frame)

class Application(Application_ui):
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Command1_Cmd(self, event=None):
        #TODO, Please finish the function here!
        print("exed")
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        global port
        port = int(self.Text2.get())
        print(port)
        try:
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
