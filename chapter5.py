# import math
# radius = int(input())
# while radius < 10:
    
#     area = radius **2 * math.pi
#     print(f"Circle area when {radius} is {area:.2f}")
#     radius +=1 #radius = radius +1
# i = 10
# while i<10:
#     print(i)
    #i+=1 #if there i+= it will endless loop 
    
# for i in range(1,10, 2):#condition, (0,10):0-9, (..,.., 2): here mean step, if it's 2 it outof rang
#     print(i)
    # radius = 1
    # area = radius **2 * math.pi
    # print("Circle area when {radius} is {area:}")
# for i in range(1,10):
#     #print(i, "|", end="")
#     print()
#     for j in range(1,10):
#         print(format(i * j, "10d"), end="")#end="" Ensures that the print statement in the same line
# sum = 0
# number = 0

# while number < 20:
#     number+=1
    
#     if number == 10 or number == 11:
#         continue 
#     sum+=number
# print("The number is ",number)
# print("The sum is",sum)
# count = 0
# while count<10:
#     print("Programming is fun")
#     count+=1
# sum =0 
# i=1
# while i < 10:
#     sum +=i
#     i+=1
#     print("The sum",sum)
# LOOP Random
# import random
# number1 = random.randint(0,9)
# number2 = random.randint(0,9)
# if number1<number2:
#     number1,number2 = number2,number1
# answer = eval(input("What is " + str(number1) +" - "+ str(number2) + "?"))
# while number1-number2 != answer:
#     answer=eval(input("You are wrong!Try Again! What is " + str(number1) + " - " + str(number2) + "?"))

# print("You got it! ")
# import random
# number1 = random.randint(0, 9)
# number2 = random.randint(0, 9)

# if number1 < number2:
#     number1, number2 = number2, number1

# answer = eval(input("What is " + str(number1) + " - " + str(number2) + "? "))

# while number1 - number2 != answer:
#     answer = eval(input("You are wrong! Try Again! What is " + str(number1) + " - " + str(number2) + "? "))

# print("You got it!")
#multiplication table
print("            Multiplication Table")
print(" |",end ="")
for j in range(1,10):
    print(" ",j,end="")
    print()
print("-------------------------------------------------")
for i in range(1,10):
    print(i," |",end="")
for j in range(1,10):
    print(format(i*j,"4d"),end="")
print()

 



