# -*- coding: utf-8 -*-

import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

import message_notify_python.catchexception
import message_notify_python.messagenotify

message_notify_python.messagenotify.MessageNotify(1, 'xxxxx')

def main():
    print(1 / 0)

if __name__ == '__main__':
    main()
    # message_notify_python.catchexception.test()