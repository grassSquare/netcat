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
    print("BHP Net Tool")
    print()
    print("Usge:bhpnet.py -t target_host -p port")
    print("-l --listen              -listen on [host]:[port] for incoming connections")
    print("-c --command             -initialize a command shell")
    print("-e --execute             -execute the given file upon receiving a connection")
    print("-u --upload=destination  -upon receiving connection upload a file and write to [destination]")
    print()
    print("Examples:")
    print("bhpnet.py -t 192.168.0.1 -p 5555 -l -c")
    print("bhpnet.py -t 192.168.0.1 -p 5555 -l -u=C:\\target.exe")
    print("bhpnet.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\"")
    print("echo 'ABCDEFGHI' | ./bhpnet.py -t 192.168.11.12 -p 135")
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

            buffer



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

if __name__ == '__main__':
    main()