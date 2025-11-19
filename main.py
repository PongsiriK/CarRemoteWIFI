import network
import socket
from machine import PWM,Pin
import time
# LB = Left back
# F = Forward, B = Backward

BLF16=PWM(Pin(16),freq=500,duty=0)
BLB17=PWM(Pin(17),freq=500,duty=0)
BRF33=PWM(Pin(33),freq=500,duty=0)
BRB32=PWM(Pin(32),freq=500,duty=0)
FLF18=PWM(Pin(18),freq=500,duty=0)
FLB19=PWM(Pin(19),freq=500,duty=0)
FRF26=PWM(Pin(26),freq=500,duty=0)
FRB25=PWM(Pin(25),freq=500,duty=0)

BL =[BLF16,BLB17]
BR =[BRF33,BRB32]
FL =[FLF18,FLB19]
FR =[FRF26,FRB25]

x=0

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#ฟังก์ชั่นกำหนดความเร็วแต่ละล้อ

def wheel(fb,pw) :
    if pw >= 0 :
        fb[0].duty(pw)
        fb[1].duty(0)
    else :
        fb[0].duty(0)
        fb[1].duty(abs(pw))

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#ฟังก์ชั่นพุ่งทะยานไปเลย แม็กนั่ม!!!

def g(speed) :
    print("Speed? = ",speed)
    if abs(speed) <= 1023 :
        global x
        x = speed
        wheel(BR,speed)
        wheel(BL,speed)
        wheel(FR,speed)
        wheel(FL,speed)
        if speed > 0 :
            print("^^^")
        else :
            print("vvv")
    else :
        print("Can't do that. (MAX : 1023)")
        
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#ฟังก์ชั่นหุ้นยนเต้นลีลาด
def r(cw) :
    wheel(BR,-cw)
    wheel(FR,-cw)
    wheel(BL,cw)
    wheel(FL,cw)
    
def l(cw) :
    wheel(BR,cw)
    wheel(FR,cw)
    wheel(BL,-cw)
    wheel(FL,-cw)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#เป็นการเลี้ยวแบบไม่หยุดเพื่อหมุน
def rr(cww) :
    int(cww)
    wheel(BR,0)
    wheel(FR,-cww)
    wheel(BL,1000)
    wheel(FL,1000)
    
def ll(cww) :
    int(cww)
    wheel(BR,1000)
    wheel(FR,1000)
    wheel(BL,0)
    wheel(FL,-cww)

def brr(cww) :
    int(cww)
    wheel(BR,0)
    wheel(FR,-cww)
    wheel(BL,-1000)
    wheel(FL,-1000)

def bll(cww) :
    int(cww)
    wheel(BR,-1000)
    wheel(FR,-1000)
    wheel(BL,0)
    wheel(FL,-cww)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#การเร่งความเร็วด้วยการกำหนดเวลาและจำนวนครั้งที่เปลี่ยนความเร็ว
def gg(stc,at,r) :
    SPT=abs(x-stc)/r
    SPT=int(SPT)
    y=x
    if stc < x :
        SPT=-SPT
    for n in range(r) :
        y=y+SPT
        time.sleep(at/r)
        g(y)
    g(stc)

#==========================================================================================
acp = network.WLAN(network.AP_IF)
acp.config(essid='Doraemon',password='12345678910fb',authmode=network.AUTH_WPA2_PSK)
acp.active(True)

port=12224
host='192.168.4.1'

srv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
srv_sock.bind((host,port))

while True:
    data,add = srv_sock.recvfrom(2)
    data.decode('tis-620')    
    if(data==b'wd'):
        if x != 1000 :
            gg(1000,0.1,10)
        rr(500)
    elif(data==b'wa'):
        if x != 1000 :
            gg(1000,0.1,10)
        ll(500)
    elif(data==b'sa'):
        bll(-500)
    elif(data==b'sd'):
        brr(-500)
    elif(data==b'w'):
        gg(1000,0.1,10)
        print(x)
    elif(data==b's'):
        gg(-1000,0.1,10)
    elif(data==b'd'):
        r(1000)
    elif(data==b'a'):
        l(1000)
    elif(data==b'b'):
        gg(0,0.1,10)
    elif(data==b'q'):
        socket.close()
        break
