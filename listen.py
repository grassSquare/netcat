import os
import sys
import tty, termios
import time

if __name__ == '__main__':
    print("Reading form keybord")
    print()
    print('press Q to quit')
    while True:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        # old_settings[3]= old_settings[3] & ~termios.ICANON & ~termios.ECHO
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        # print 'error'
        if ch == 'i':
            print('move forward')
        elif ch == 'm':
            print('move back')
        elif ch == 'j':
            print("turn left!")
        elif ch == 'l':
            print("turn right!")
        elif ch == 'u':
            print
            "turn right!"
        elif ch == 'o':
            print
            "turn right!"
        elif ch == 'k':
            print
            "stop motor!"
        elif ch == 'q':
            print
            "shutdown!"
            break
        elif ord(ch) == 0x3:
            # 这个是ctrl c
            print
            "shutdown"
            break
        print
        "Reading form keybord"
        print
        """   i
j  k  l
   m"""
        print
        'press Q or ctrl+c to quit'
    # rate.sleep()
---------------------
作者：CSDN_Flying
来源：CSDN
原文：https: // blog.csdn.net / u010918541 / article / details / 54709222
版权声明：本文为博主原创文章，转载请附上博文链接！