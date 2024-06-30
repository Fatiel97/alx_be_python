# multiplication_table.py

# Prompt the user to input a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table using a for loop
for i in range(1, 11):  # Loop from 1 to 10 inclusive
    result = number * i
    print(f"{number} * {i} = {result}")
