def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def factorialRecursive(n):
    if (n == 0):
        return 1
    return n * factorialRecursive(n - 1)


# Test
num = 5
print(f"Factorial of {num} is: {factorialRecursive(num)}")