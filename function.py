import sys
import random
def randomNumber():
    for i in range(3):
        random_value = random.randint(1,9)
        if random_value % 5 == 0:
            continue
        print("Random value is ",random_value)
    
def even_odd(result):
    if result % 2 == 0:
        print("Even")
    else:
        return "Odd"

def sunfunction():
    sum =0 
    for i in range(1,10):  
        sum+=i
    return sum
# print(sunfunction())

sumvalue = sunfunction()
print(sumvalue)
even_odd(sumvalue)

#to connect between files in same project
#from FunctionApps(file name ) import (function name) if all functions use import *
#from math import pi 
#print(pi)
#import time 
#print(time.time())
#what if from different project
# #import os   
#from projectname,abovefilename,filename import*