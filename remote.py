import socket
import keyboard
import time

port = 12224
host = '192.168.4.1'

x = 0

def send_udp(st):
    uc_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    st=bytes(st,'tis-620')
    uc_sock.sendto(st,(host,port))
    

def main():
    while True:   
        global x
        time.sleep(0.04)
        if keyboard.is_pressed('w+a'):
            if x == 1 :
                pass
            else :
                send_udp('wa')
                print('movement :            \u2196\u2196\u2196\u2196\u2196         ' ,end='\r')
                x=1
        elif keyboard.is_pressed('w+d'):
            if x == 2 :
                pass
            else :
                send_udp('wd')
                print('movement :            \u2197\u2197\u2197\u2197\u2197         ',end='\r')
                x=2
        elif keyboard.is_pressed('s+a'):
            if x == 3 :
                pass
            else :
                send_udp('sa')
                print('movement :            \u2199\u2199\u2199\u2199\u2199         ',end='\r')
                x=3
        elif keyboard.is_pressed('s+d'):
            if x == 4 :
                pass
            else :
                send_udp('sd')
                print('movement :            \u2198\u2198\u2198\u2198\u2198          ',end='\r')
                x=4
        elif keyboard.is_pressed('w'):
            if x == 5 :
                pass
            else :
                send_udp('w')
                print('movement :            \u21d1 \u21d1 \u21d1         ',end='\r')
                x=5
        elif keyboard.is_pressed('s'):
            if x == 6 :
                pass
            else :
                send_udp('s')
                print('movement :            \u21d3 \u21d3 \u21d3         ',end='\r')
                x=6
        elif keyboard.is_pressed('a'):
            if x == 7 :
                pass
            else :
                send_udp('a')
                print('movement :            \u21C7 \u21C7 \u21C7         ',end='\r')
                x=7
        elif keyboard.is_pressed('d'):
            if x == 8 :
                pass
            else :
                send_udp('d')
                print('movement :            \u21C9 \u21C9 \u21C9        ',end='\r')
                x=8

        elif x != 0 :
            send_udp('b')
            x=0
            time.sleep(0.1)            
            print('movement :            STOP!            ',end='\r')
        elif keyboard.is_pressed('i+o+p'):
            print(" ")
            print('                       BYE')
            time.sleep(0.75)
            send_udp('q')
            exit()
            
print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣰⠤⠤⠤⠤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠞⠛⠉⠉⠛⠓⠦⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣛⣛⣿⡿⠂⠀⠀⠀⠈⠙⠶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠈⢳⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣞⣓⣒⣒⣒⣒⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠿⠶⠶⠶⢶⣒⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇
⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⣐⣒⣒⣛⠷⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳
⠀⠀⠀⠀⠀⠀⠀⢠⡯⣤⣥⣰⣶⣖⣞⣓⣛⣛⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⠀⠀⠀⠀⠀⠀⠀⢸⠿⠿⠿⠿⠿⠿⠿⠟⠳⠤⠿⠒⠶⠶⠀⠀⠠⢤⡤⠤⠄⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⢀⣤⣤⡄⡄⢀⣤⠀⠀⠀⠀⢸
⠀⠀⠀⠀⠀⠀⠀⢸⡯⣭⠭⠭⠭⠉⠁⢠⡒⠛⠉⡍⢳⡆⠀⣠⡖⠻⡏⠙⣦⢼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⡟⠁⢀⣿⣧⣞⡁⠀⠀⠀⠀⢸
⠀⠀⠀⠀⠀⠀⢠⣟⣻⣻⣿⣫⣭⣭⠽⠌⠛⠢⠤⠔⠋⠀⠀⡇⠓⠦⠥⠞⠁⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⠳⠶⠛⠁⠇⠀⠙⠂⠀⠀⠀⢸
⠀⠀⠀⠀⠀⠀⣸⠛⠛⣷⠛⠲⠦⠤⠭⠿⠦⠄⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸
⠀⠀⠀⠀⠀⠀⢿⡭⢽⢿⡄⠀⠀⢉⣉⡉⠉⠉⠀⠀⠀⠀⢠⣼⡆⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇
⠀⠀⠀⠀⠀⠀⠈⢿⣙⣾⣓⣀⣐⣒⣒⣒⣀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠙⠶⡶⡏⠉⣉⣑⣒⣒⣒⡂⠀⠀⠐⢶⠶⠆⠀⠀⠀⠀⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡏⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠠⠴⠖⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣏⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⢤⣀⠀⠀⠀⢀⣠⠔⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⡿⣭⡉⠉⠵⠆⠀⠀⠀⠀⢀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀  ╱|、
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠼⠿⠿⣿⣯⡥⠤⠴⠖⣿⣅⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ (˚ˎ。7
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⢿⠛⠛⠛⠉⠉⠀⠀⠀⢿⡈⠙⣍⠹⡦⣄⣀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ |、˜ 〵
⠀⠀⠀⠀⠀⠀⠀⢀⣤⣴⣾⣭⣿⣯⣿⣭⠥⠄⠀⠀⠀⠀⠀⠀⠾⢷⡀⠘⣦⣽⣬⣧⠀⡻⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ じしˍ,)ノ
      ===================================================================================
      """  )                         
print('      W to foward ,S to backward ,A to turnleft ,D to turnright , Drift by your skill',end='\n\n')
print('      ===================================================================================')
print('\n                  CAR IS READY!\n')
main()
