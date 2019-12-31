#!/usr/bin/python3

#using exception
import pyttsx3

try:
    n1=input("plz enter first number:- ")
    n2=input("plz enter second number:- ")
    sum=int(n1)+int(n2)
    print(sum)

except (NameError,ValueError):
        print("plz enter numbers only!!!!!!")
        s=pyttsx3.init()
        s.say("please enter numbers brother")
        s.runANdWait()














except :
    print("anything")
finally :
    print("finally runs always ")

