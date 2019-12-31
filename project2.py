#!/usr/bin/env python3



import time,sys,subprocess,os,webbrowser

l1=[2,3,4,5]
dyn_input=sys.argv[1:]

sum=0

for i in dyn_input:
    sum=sum+int(i)
    print('element ',i,'added')
print(sum)









