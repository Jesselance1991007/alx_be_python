# pattern_drawing.py

# Prompt user for input
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# While loop for rows
while row < size:
    # For loop for columns
    for col in range(size):
        print("*", end="")  # print without newline
    print()  # move to next row
    row += 1
