def add_numbers(a, b):
    """
    This function adds two numbers and returns the sum.

    Args:
      a: The first number.
      b: The second number.

    Returns:
      The sum of a and b.
    """
    sum = a + b
    return sum

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate the sum
result = add_numbers(num1, num2)

# Print the result
print("The sum of", num1, "and", num2, "is", result)