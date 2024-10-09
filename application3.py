count_positive = 0
count_negative = 0
total = 0
count = 0

while True:
    num = int(input("Enter an integer, the input ends if it is 0: "))
    
    if num == 0:  # Corrected comparison here (was if num = 0)
        break
    
    if num > 0:
        count_positive += 1
    elif num < 0:
        count_negative += 1
    
    total += num
    count += 1

if count > 0:  # Avoid division by zero
    average = total / count
else:
    average = 0  # Handle no input case

print("Positive numbers:", count_positive)
print("Negative numbers:", count_negative)
print("Total:", total)
print("Average:", average)
