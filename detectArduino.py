#!/usr/bin/pyhton
# detectArduino.py
# thr / 2017-05-18

import serial
for com in range(0,4):
  try:
#PORT = '/dev/ttyACM' # check /var/log/messages whil connecting your Arduino to Raspberry PI
    PORT = '/dev/ttyACM'+str(com)
    BAUD =  38400
    board = serial.Serial(PORT,BAUD)
    print 'Arduino erkannt an /dev/ttyACM'+str(com)
    print 'Hardware: %s' % board.__str__()
    board.close()
    break
  except:
    print 'Kein Arduino an /dev/ttyACM'+str(com)
