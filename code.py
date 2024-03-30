# Here we define a function that implements the Euclidean Algorithm to find the GCD of two numbers
def gcd(a, b):
    """
    This function calculates the Greatest Common Divisor (GCD) of two integers using the Euclidean Algorithm.
    
    Parameters:
    a (int): The first positive integer.
    b (int): The second positive integer.
    
    Returns:
    int: The greatest common divisor of a and b.
    """
    while b != 0:
        temp = b    # assigning the value of b to a temporary variable, so that we can update b
        b = a % b   # finding the remainder of a divided by b and assigning it to b
        a = temp    # assigning the value of b to a
    return a

# Example usage of the gcd function
# Calculate the GCD of 48 and 18
example_gcd = gcd(270, 192)

print(example_gcd)
