#age1 = 10
#String : data type in "" Ex: boolean: str = "" or String = ""
# boolean = 1
# print(type(boolean)) #type to find class ''
# if True:#"True" must be in Upper case
#     print ("Hello world")
# print("Hello"+ str(1))
# age = 30//4# / is float number // is rounded number, ** is exponent 
# print(age)
# age = float(30)#convert from class to class
# print(type(age))
# age = int(30.51)
# print(type(age))\

# Question 1

# Write a Python program that does the following:

# 1. Takes input from the user for a temperature value in Celsius.
# 2. Converts the Celsius temperature to Fahrenheit using the formula: 

# F = (9/5)*C + 32
# Where
# F is Fahrenheit and 
# C is Celsius.

# 3. Prints the converted temperature in Fahrenheit.

# '''

# your code here
# temperature = float(input("Enter temperature in Celsius: "))
# fahrenheit = (9/5)*temperature + 32
# print("Temperature in Fahrenheit is ",fahrenheit)
# Question 2

# Write a Python program that calculates and prints the area of a circle. The program should:

# 1. Take the radius of the circle as input from the user.
# 2. Use the formula Area = pi * radius * radius to calculate the area.
# 3. Print the calculated area.
# import math
# # Area = round(Area,2)
# radius = int(input("Enter radius :"))
# Area = radius**2 * math.pi
# print(f"The area of circle is {Area:.2f}")
# Question 3

# Write a Python program that calculates and prints the average rating of a movie based on user reviews. The program should:

# 1. Take input from the user for three different user ratings (as integers) for a movie (e.g., on a scale of 1 to 5).
# 2. Calculate the average rating of the movie.
# 3. Print the average rating with a friendly message.
# rate1 = int(input("Enter your rating 1 from 1 to 5 :"))
# rate2 = int(input("Enter your rating 2 from 1 to 5 :"))
# rate3 = int(input("Enter your rating 3 from 1 to 5 :"))
# average = (rate1	+ rate2 + rate3)/3
# print("Average rating is ",average)

# print("Hello my name is {}.I'm {} years old").format(name,age)

# print("Hello","how are you?",sep = "___")# if we want to seperate 
# print("Hello", end = " Two space ")
# print("World")
print("What's Python?")
print("Python is a programming language.")