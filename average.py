__author__ = 'Gary'
import re

def average(n):
    total=0
    n=n.split(",")
    #print(type(n[1]))
    a=[]
    for k in range(0,len(n)):
        #print(n[k])
        if re.match('\-?[0-9]|^[0-9]\.[0-9]$',n[k])==None:
             pass
        else:
           print(n[k])
           a.append(float(n[k]))

    print(a)
    for i in range(0,len(a)):
        total=total+a[i]
    average=total/len(a)
    return average

def main():
    n=input("enter you numbers to get your average:")
    try:
        print(average(n))
    except :
        print("forgot something?")

main()
