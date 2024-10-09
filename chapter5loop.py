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
# number = random.randint(0,100)
# print("Let play quessing number game from 0 to 100")
# guess =-1
# while guess!=number:
#     guess=eval(input("Enter a number"))
#     if guess = number:
#        print("you are right!")
#     elif guess<number:
#         print("Your number is too low")
#     else :
#         print("Your number is too high")
# print("You got it !")
# import time
# import random
# count = 0
# corectCount = 0
# NUMBER_COUNT = 5
# startTime= time.time()
# number1=random.randint(0,10)
# number2=random.randint(0,10)
# while  count<NUMBER_COUNT:
#     if number1<number2:
#         number1,number2=number2,number1
#     answer=eval(input("What is "+str(number1)+"-"+str(number2)+"?"))
#     if answer == number1-number2:
#        print("You are right!")
#        corectCount+=1
#     else:
#         print("You are wrong ! The answer is",number1-number2)
#     count+=1    
# Endtime=time.time()
# Testtime=int(Endtime-startTime)
# print("Correct Count is",corectCount,"out of",NUMBER_COUNT,"\nTest time is",Testtime)
# import time
# import random

# count = 0
# corectCount = 0
# NUMBER_COUNT = 5
# startTime = time.time()

# while count < NUMBER_COUNT:
#     number1 = random.randint(0, 10)
#     number2 = random.randint(0, 10)
    
#     if number1 < number2:
#         number1, number2 = number2, number1
        
#     answer = eval(input("What is " + str(number1) + " - " + str(number2) + "? "))
    
#     if answer == number1 - number2:  # Corrected comparison operator
#         print("You are right!")
#         corectCount += 1
#     else:
#         print("You are wrong! The answer is", number1 - number2)
        
#     count += 1  # Increment count for every question

# Endtime = time.time()
# Testtime = int(Endtime - startTime)  # Corrected time calculation

# print("Correct Count is", corectCount, "out of", NUMBER_COUNT)
# print("Test time is", Testtime, "seconds")
# number =eval(input("Enter number"))
# max = number
# while number != 0:
#     number = eval(input("Enter number"))
#     if number > max:
#        max = number
# print("Max is",max)
# print("number is",number)
print("            Multiplication Table")
print(" |",end ="")
for j in range(1,10):
    print(" ",j,end="")
print()
print("-------------------------------------------------")
for i in range(1,10):
    if i % 2==0:
        continue
    print(i," |",end="")
    for j in range(1,10):
       
        print(format(i * j, "4d "),end=" ")
    print()
# print("            Multiplication Table")
# print(" |",end ="")
# for j in range(1,10):
#     print(" ", j, end="")
# print()  # Move to the next line
# print("-------------------------------------------------")
# for i in range(1,10):
#     print(i, " |", end="")
#     for j in range(1,10):
#         print(format(i * j, "4d"), end=" ")  # Proper formatting of the multiplication result
#     print()  # Move to the next line after printing a row

