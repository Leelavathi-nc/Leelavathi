# Function to check if a number is prime
def is_prime(n):
    # Check if n is less than 2, which is not a prime number
    if n < 2:
        return False

    # Check if n is divisible by any number from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False

    # If n is not divisible by any number from 2 to n-1, then it is a prime number
    return True

# Test the function with some example numbers
print(is_prime(5))   # Output: True
print(is_prime(10))  # Output: False
print(is_prime(23))  # Output: True
