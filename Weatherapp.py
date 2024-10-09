import matplotlib.pyplot as plt 
import requests

def collect_weather_data():
    print("Enter temperatures for 5 days:")
    temp_day1 = float(input("Day 1: "))
    temp_day2 = float(input("Day 2: "))
    temp_day3 = float(input("Day 3: "))
    temp_day4 = float(input("Day 4: "))
    temp_day5 = float(input("Day 5: "))

    return temp_day1, temp_day2, temp_day3, temp_day4, temp_day5

def calculate_average(temp1, temp2, temp3, temp4, temp5):
    total = temp1 + temp2 + temp3 + temp4 + temp5
    return total / 5

def find_highest(temp1, temp2, temp3, temp4, temp5):
    return max(temp1, temp2, temp3, temp4, temp5)

def find_lowest(temp1, temp2, temp3, temp4, temp5):
    return min(temp1, temp2, temp3, temp4, temp5)

def present_results(average, highest, lowest):
    print("\nWeather Analysis Results:")
    print(f"Average Temperature: {average:.2f}")
    print(f"Highest Temperature: {highest}")
    print(f"Lowest Temperature: {lowest}")

def plot_temperatures_line_chart(temp1, temp2, temp3, temp4, temp5):
    temperatures = [temp1, temp2, temp3, temp4, temp5]
    
    plt.figure(figsize=(10, 5))
    plt.plot(temperatures, marker='o', color='b')
    plt.title('Temperature Data Analysis')
    plt.xlabel('Days')
    plt.ylabel('Temperature')
    plt.grid(True)
    plt.show()

def main():
    temp_day1, temp_day2, temp_day3, temp_day4, temp_day5 = collect_weather_data()

    average = calculate_average(temp_day1, temp_day2, temp_day3, temp_day4, temp_day5)
    highest = find_highest(temp_day1, temp_day2, temp_day3, temp_day4, temp_day5)
    lowest = find_lowest(temp_day1, temp_day2, temp_day3, temp_day4, temp_day5)
    
    present_results(average, highest, lowest)
    plot_temperatures_line_chart(temp_day1, temp_day2, temp_day3, temp_day4, temp_day5)

if __name__ == "__main__":
    main()