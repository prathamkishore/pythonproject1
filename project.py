#!/usr/bin/python3
import webbrowser,time,socket
import subprocess,ipaddress
x="""
press 1 to start you default browser:-
press 2 to to chech internet connection speed:-
press 3 to check your internet status:-
press 4 to check current date and time:-
press 5 to  check current temperature of your city:-
press 6 to check public ip :-
press 7 to create a directory in your os :-
press 8 to reboot your system:-
press 9 to play songs in youtube:-
press 10 to search something in google search engine:-
"""
print(x)
choice=input()
print("your choice is " +choice)
if choice == '4':  
    print("current date and time ",subprocess.getoutput("date" ))
elif choice == '1':
    print('starting browser',time.sleep(3),webbrowser.open_new_tab("http://www.google.com"))
elif choice == '9':
    print("awesome",webbrowser.open_new_tab("http://www.youtube.com/watch?v=iO_WxYC34eM"))
elif choice == '8':
    print('oops rebooting',subprocess.getoutput("reboot"))
elif choice == '3':
    out=subprocess.getstatusoutput("ping -c 2 8.8.8.8")
    if out[0] == 0:
     print('working properly')
    else:
     print('not connected')
elif choice == '7':
    print('enter the name ')
    a=input()
    print('creating directory created successfully',subprocess.getoutput("mkdir " +a))
elif choice == '6':
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print("your system's ipaddress is ",ip)
elif choice == '10':
    que=input('search anything  :-')
    print("google is awesome but havn't you heard of tor??",webbrowser.open_new_tab("http://www.google.com/search?q= "+que))
elif choice == '5':
    tem=input('enter city name  :-')
    print("now you see temperature",webbrowser.open_new_tab("http://www.google.com/search?q=temperature "+tem))







