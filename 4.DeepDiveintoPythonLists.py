# 4. Deep Dive into Python Lists
# Objective: The aim of this assignment is to integrate various list operations and methods to solve a complex problem.
# Problem Statement: You're organizing a school event, and you have lists containing student names, their grades, and the activities they're interested in.

# Task 1: Given the lists:
# students = ["John", "Doe", "Jane", "Smith"]
# grades = [85, 90, 78, 88]
# activities = ["Football", "Music", "Art", "Dance"]
# Filter out students who have grades below 80. Print the name, grade and activiy. Expected Outcome "Jane", 78, "Art"
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

# Create a list to store results
students_have_grades_below_80 = []
for i in range(len(students)):
    student = students[i]
    grade = grades[i]
    activity = activities[i]
    # Check if grade is below 80
    if grade < 80:
        students_have_grades_below_80.append((student, grade, activity))  # Use tuple for data grouping
# Print the students_have_grades_below_80
for student, grade, activity in students_have_grades_below_80:
    print(f"{student}, {grade}, {activity}")

# Task 2: For the remaining students, add students name in a new list named students_approved. Expected Outcome: students_approved = ["John", "Doe", "Smith"]
students_approved = []

# Loop through student data (assuming data lengths are aligned)
for i in range(len(students)):
    student = students[i]
    grade = grades[i]
    activity = activities[i]
    if grade >= 80:
        students_approved.append(student)  # Add to approved list if grade is 80 or above

# Task 3: Print the list students_approved
# Print the students who are approved (grade 80 or above)
print(f"\nStudents approved (grade 80 or above): {students_approved}")