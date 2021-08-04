import RPi.GPIO as IO 
import time 
import requests
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)

IO.setwarnings(False)
IO.setmode(IO.BCM)

lst = [1,2,3,4]

IO.setup(14,IO.OUT)
IO.setup(15,IO.OUT)
IO.setup(18,IO.OUT)

IO.setup(23,IO.OUT)
IO.setup(24,IO.OUT)
IO.setup(16,IO.OUT)

IO.setup(8,IO.OUT)
IO.setup(7,IO.OUT)
IO.setup(1,IO.OUT)

IO.setup(17,IO.IN)
IO.setup(27,IO.IN)
IO.setup(22,IO.IN)
IO.setup(5,IO.IN)
IO.setup(6,IO.IN)
IO.setup(26,IO.IN)

countA = 0
countB = 0
countC = 0

lst_sen1 = [17,22,6]
lst_sen2 = [27,5,26]

lst_green = [14,23,8]
lst_yellow = [15,24,7]
lst_red = [18,16,1]



def roadE():
    
    IO.output(lst_red[0], True)
    IO.output(lst_red[1], True)
    IO.output(lst_red[2], True)
    time.sleep(2)
    IO.output(lst_yellow[0], True)
    IO.output(lst_yellow[1], False)
    IO.output(lst_yellow[2], False)
    time.sleep(1)
    IO.output(lst_red[0], False)
    IO.output(lst_red[1], True)
    IO.output(lst_red[2], True)
    IO.output(lst_yellow[0], False)
    IO.output(lst_yellow[1], False)
    IO.output(lst_yellow[2], False)
    IO.output(lst_green[0], True)
    IO.output(lst_green[1], False)
    IO.output(lst_green[2], False)
    time.sleep(5)
    IO.output(lst_yellow[0], True)
    IO.output(lst_yellow[1], False)
    IO.output(lst_yellow[2], False)
    IO.output(lst_green[0], False)
    IO.output(lst_green[1], False)
    IO.output(lst_green[2], False)
    time.sleep(0.5)

def roadF():
    IO.output(lst_red[0], True)
    IO.output(lst_red[1], True)
    IO.output(lst_red[2], True)
    time.sleep(2)
    IO.output(lst_yellow[0], False)
    IO.output(lst_yellow[1], True)
    IO.output(lst_yellow[2], False)
    time.sleep(1)
    IO.output(lst_red[0], True)
    IO.output(lst_red[1], False)
    IO.output(lst_red[2], True)
    IO.output(lst_yellow[0], False)
    IO.output(lst_yellow[1], False)
    IO.output(lst_yellow[2], False)
    IO.output(lst_green[0], False)
    IO.output(lst_green[1], True)
    IO.output(lst_green[2], False)
    time.sleep(5)
    IO.output(lst_yellow[0], False)
    IO.output(lst_yellow[1], True)
    IO.output(lst_yellow[2], False)
    IO.output(lst_green[0], False)
    IO.output(lst_green[1], False)
    IO.output(lst_green[2], False)
    time.sleep(0.5)  

def roadG(): 
    IO.output(lst_red[0], True)
    IO.output(lst_red[1], True)
    IO.output(lst_red[2], True)
    time.sleep(2)
    IO.output(lst_yellow[0], False)
    IO.output(lst_yellow[1], False)
    IO.output(lst_yellow[2], True)
    time.sleep(1)
    IO.output(lst_red[0], True)
    IO.output(lst_red[1], True)
    IO.output(lst_red[2], False)
    IO.output(lst_yellow[0], False)
    IO.output(lst_yellow[1], False)
    IO.output(lst_yellow[2], False)
    IO.output(lst_green[0], False)
    IO.output(lst_green[1], False)
    IO.output(lst_green[2], True)
    time.sleep(5)
    IO.output(lst_red[0], True)
    IO.output(lst_red[1], True)
    IO.output(lst_red[2], False)
    IO.output(lst_yellow[0], False)
    IO.output(lst_yellow[1], False)
    IO.output(lst_yellow[2], True)
    IO.output(lst_green[0], False)
    IO.output(lst_green[1], False)
    IO.output(lst_green[2], False)
    time.sleep(0.5)

while True: 
    if(IO.input(lst_sen1[0])==0 and IO.input(lst_sen2[0]) == 0):
        roadE()
        countA +=1
        countB = 0
        countC = 0
        road =5
        data={'count':countA, 'status':'mp','road':road}
        res = requests.post("http://192.168.43.138:8000/api/traffic/", data=data)
        print(countA)
        time.sleep(2)

    if(IO.input(lst_sen1[0])==0 and IO.input(lst_sen2[0]) == 1):
        roadE()
        countA +=1
        countB = 0
        countC = 0
        road = 5
        data={'count':countA, 'status':'mp','road':road}
        res = requests.post("http://192.168.43.138:8000/api/traffic/", data=data)
        print(countA)
        time.sleep(2)

    elif (IO.input(lst_sen1[1])==0 and IO.input(lst_sen2[1]) == 0):
        roadF()
        countA =0
        countB +=1
        countC = 0
        road =6
        data={'count':countB, 'status':'mp','road':road}
        res = requests.post("http://192.168.43.138:8000/api/traffic/", data=data)
        print(countB)
        time.sleep(2)

    elif (IO.input(lst_sen1[1])==0 and IO.input(lst_sen2[1]) == 1):
        roadF()
        countA =0
        countB +=1
        countC =0
        print(countB)
        road =6
        data={'count':countB, 'status':'mp','road':road}
        res = requests.post("http://192.168.43.138:8000/api/traffic/", data=data)
    elif (IO.input(lst_sen1[2])==0 and IO.input(lst_sen2[2]) == 0):
        roadG()
        countA =0
        countB =0
        countC +=1
        road =7
        data={'count':countC, 'status':'mp','road':road}
        res = requests.post("http://192.168.43.138:8000/api/traffic/", data=data)
        print(countC)
        time.sleep(2)

    elif (IO.input(lst_sen1[2])==0 and IO.input(lst_sen2[2]) == 1):
        roadG()
        countA =0
        countB = 0
        countC +=1
        print(countC)
        road =7
        data={'count':countC, 'status':'mp','road':road}
        res = requests.post("http://192.168.43.138:8000/api/traffic/", data=data)
    else:
        roadE()
        countA +=1
        countB = 0
        countC =0
        print(countC)
        road =5
        data={'count':countA, 'status':'mp','road':road}
        res = requests.post("http://192.168.43.138:8000/api/traffic/", data=data)
# ##########################################################
        roadF()
        countA =0
        countB  +=1
        countC =0
        print(countB)
        road =6
        data={'count':countB, 'status':'mp','road':road}
        res = requests.post("http://192.168.43.138:8000/api/traffic/", data=data)
# ##########################################################
        roadG()
        countC =0
        countB =0
        countC +=1
        print(countC)
        road =6
        data={'count':countC, 'status':'mp','road':road}
        res = requests.post("http://192.168.43.138:8000/api/traffic/", data=data)
