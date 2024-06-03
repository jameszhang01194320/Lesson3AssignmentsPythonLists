# 2. Advanced List Methods and Identity Operators

# Task 1: Given the two lists:
# submitted = ["Alice", "Bob", "Charlie", "David"]
# attended = ["Charlie", "Eve", "Alice", "Frank"]
# Find out which students both submitted their assignments and attended the class.
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

# List to store students who attended and submitted
submitted_and_attended = []
for student in submitted:
    # Check if the student is also in the attended list
    if student in attended:
        submitted_and_attended.append(student)

print(f"Students who submitted and attended: {submitted_and_attended}")


# Task 2: Check if the two lists are identical in terms of their content, regardless of order.

# Check if the lists have the same length 
if len(submitted) != len(attended):
    print("The lists are not identical.")
else:
    for student in attended:
        if student not in submitted:
            print("The lists are not identical.")
            break  # Exit the loop if a mismatch is found
    else:
        print("The lists are identical.")  # Only print if the loop completes without a mismatch



# Task 3: Using list methods, remove any student from the attended list who did not submit their assignment.
for student in attended:
    if student not in submitted:
        attended.remove(student)  # Remove from the original attended list
# Print the modified attended list
print(f"Students who attended and submitted: {attended}")
