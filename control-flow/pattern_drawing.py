# pattern_drawing.py

# Prompt the user to input the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Ensure the input is a positive integer
while size <= 0:
    print("Please enter a positive integer.")
    size = int(input("Enter the size of the pattern: "))

# Draw the square pattern using nested loops
row = 1
while row <= size:
    # Print asterisks in the current row
    for column in range(1, size + 1):
        print("*", end="")
    # Move to the next row
    print()
    row += 1
