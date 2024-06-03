# 1. Python List Transformation

# Task 1: Given the list of grades:
# grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
# Sort the grades in descending order and display the sorted list.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
print(grades)

# Task 2: Calculate the average grade and display it.
sum_of_grades = sum(grades)
total_grades = len(grades)
average_grade = sum_of_grades / total_grades
print(f"The average grade is: {average_grade:.2f}")

# Task 3: Replace any grade below 80 with the value Failed.
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
for i in range(len(grades)):
    if grades[i] < 80:
        grades[i] = "Failed"

# Print the modified grades list
print(grades)
