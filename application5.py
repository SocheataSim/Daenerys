
tuition = 10000
year = 1


while year <= 10:
    tuition += tuition * 0.05  
    year += 1  # Fixed: Correctly increment year(was y + 1)

print("Tuition in 10 years:", round(tuition, 2))  # Output the tuition in 10 years (rounded)


total_cost = 0

for i in range(4):
    total_cost += tuition 
    tuition += tuition * 0.05  # Increase tuition by 5% for the next year

print("Total cost for four years' tuition after 10 years:", round(total_cost, 2))  # Output total cost (rounded)
