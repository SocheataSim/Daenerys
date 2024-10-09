# print("What's Python?")
# print("Python is a programming language.")
# print('Q: What\'s Python Programming?')# \ escape character 
# print('A: "Python" is a programming language')
# How to convert other bases to decimal
# print(int("1010",base = 2))
# print(int("1010",2))
# print(int("12", base = 8))
print(int("1110",base = 2))
print(int("21",base = 8))
print(int("C",base = 16))
print(int("P",base = 32))
# countdown number
import time
for i in range(10,-1,-1):
    print(f"Count down number in {i}",end = "\n")
    time.sleep(1)
print("Happy new year !")
