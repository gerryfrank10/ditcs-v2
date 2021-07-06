import serial
import time
import string

ser = serial.Serial('/dev/ttyUSB2', 9600)

while True:
    serialdata = ser.readline()
    print(serialdata)