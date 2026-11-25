# 1. 
def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print("Largest of (12, 45, 29):", largest_of_three(12, 45, 29), "\n")

# 2. 
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number to check if prime: "))
print(f"Is {num} prime? -> {is_prime(num)}\n")

# 3. 
def calculate_average(marks_list):
    if not marks_list:
        return 0
    return sum(marks_list) / len(marks_list)

sample_marks = [78, 85, 92, 88, 76]
print("Average of", sample_marks, "is:", calculate_average(sample_marks), "\n")

# 4. 
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

print("--- Function-Based Calculator ---")
n1 = float(input("Enter first number: "))
op = input("Choose operation (+, -, *, /): ")
n2 = float(input("Enter second number: "))

if op == "+":
    print("Result:", add(n1, n2))
elif op == "-":
    print("Result:", subtract(n1, n2))
elif op == "*":
    print("Result:", multiply(n1, n2))
elif op == "/":
    print("Result:", divide(n1, n2))
else:
    print("Invalid operation")