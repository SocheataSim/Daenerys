kg = 1

while kg <= 20:#
    pounds = round(kg * 2.2, 1)  # Converts kg to pounds and rounds to 1 decimal place
    print(kg, "     ", pounds)   # Prints kg and corresponding pounds
    kg += 2  # Fixed the bug in this line: kg was not being incremented correctly
    # Increment kg by 2 after each iteration
