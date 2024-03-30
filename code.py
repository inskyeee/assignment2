# Here we define a function that takes user input and validates it
def get_user_values():
    """
    This function prompts the user to input two positive integers and validates the input.
    
    Returns:
    tuple: A tuple containing two valid positive integers input by the user.
    """
    while True:
        try:
            a = int(input("Enter the first positive integer: "))
            b = int(input("Enter the second positive integer: "))
            if a > 0 and b > 0:
                return a, b
            else:
                print("Both numbers must be positive integers. Please try again.")
        except ValueError:
            print("Invalid input. Please enter positive integers only.")


# Here we define a function that implements the Euclidean Algorithm to find the GCD of two numbers
def gcd():
    """
    This function calculates the Greatest Common Divisor (GCD) of two integers using the Euclidean Algorithm.
    It takes two integers as input (by calling get_user_values() function) from the user and returns their GCD.
    
    Returns:
    int: The greatest common divisor of a and b.
    """
    # Get user input
    a, b = get_user_values()

    while b != 0:
        temp = b    # assigning the value of b to a temporary variable, so that we can update b
        b = a % b   # finding the remainder of a divided by b and assigning it to b
        a = temp    # assigning the value of b to a
    return a

# Example usage of the gcd function
# Calculate the GCD of 48 and 18
example_gcd = gcd(270, 192)

print(example_gcd)
