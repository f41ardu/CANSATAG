#!/usr/bin/pyhton
# readArduino.py
# thr / 2017-05-18

import serial

def readlineCR(port):
    rv = ""
    while True:
        ch = port.read()
        rv += ch
        if ch=='\r' or ch=='\n':
            return rv

PORT = '/dev/ttyUSB0' # or ACMx = 0,...,4 check tail -f /var/log/messages
BAUD = 38400
port = serial.Serial(PORT,BAUD)


while True:
#    port.write("\r\nSay something:")
    rcv = readlineCR(port)
    print(repr(rcv))
