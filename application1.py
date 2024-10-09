kg = 1
pound = 20

print("Kilograms   Pounds   |   Pounds   Kilograms")
while kg <= 10 and pound <= 50:
    pounds = kg * 2.2  
    kilograms = pound * 0.45  
    
    # Printing the table in a formatted way for better readability
    print(f"{kg:<10} {pounds:<10.2f} |   {pound:<10} {kilograms:<10.2f}")
    
    # Increment the kg and pound values correctly
    kg += 2   # Fixed the error here (was kg + 2)
    pound += 5  
