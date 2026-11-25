# 1. 
num = int(input("Enter an integer to check Even/Odd: "))
if num % 2 == 0:
    print(f"{num} is Even\n")
else:
    print(f"{num} is Odd\n")

# 2. 
marks = float(input("Enter marks (0-100): "))
if marks >= 90:
    print("Grade: A+\n")
elif marks >= 80:
    print("Grade: A\n")
elif marks >= 70:
    print("Grade: B\n")
elif marks >= 60:
    print("Grade: C\n")
elif marks >= 50:
    print("Grade: D\n")
else:
    print("Grade: F (Fail)\n")

# 3. 
year = int(input("Enter a year to check Leap Year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year\n")
else:
    print(f"{year} is not a Leap Year\n")

# 4. 
print("--- Simple Calculator ---")
a = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid operator")