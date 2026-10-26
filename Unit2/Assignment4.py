# Calculate the nth Fibonacci Number Efficiently

def fibonacci(n):
    if n < 0:
        return "Invalid input! Enter a non-negative integer."

    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b

    return a


# Main Program
n = int(input("Enter the value of n: "))

result = fibonacci(n)

print("The", n, "th Fibonacci number is:", result)