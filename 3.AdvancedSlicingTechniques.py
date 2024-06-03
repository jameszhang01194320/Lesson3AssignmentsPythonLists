# 3. Advanced Slicing Techniques
# Objective: The aim of this assignment is to master the art of slicing in Python lists.
# Problem Statement: You have a list of daily temperatures for a month, and you'd like to extract specific data from it.


# Task 1: Given the list of temperatures:
# temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
# Extract the temperatures for the second week (7 days) of the month. Expected Outcome:
# 83, 85, 86, 87, 88, 89, 90,
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

start_index_second_week = 7  # Index for the beginning of the second week (7 days after Sunday)
second_week_temperatures = temperatures[start_index_second_week:start_index_second_week + 7]
print(f"Temperatures for the second week: {second_week_temperatures}")


# Task 2: Extract all the temperatures above 100.
high_temperatures = [temp for temp in temperatures if temp > 100]
print(f"Temperatures above 100: {high_temperatures}")

# Task 3: Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.
reversed_temperatures = temperatures[::-1]
sliced_temperatures = reversed_temperatures[4:10] 
# Print the extracted temperatures
print(f"Temperatures from the 5th to 10th day (reversed list): {sliced_temperatures}")