#1.
students_count = 60 #integer
average_marks = 85.5 # float
course_name = "Python"#string
is_completed = False # boolean


print(students_count, "->", type(students_count))
print(average_marks, "->", type(average_marks))
print(course_name, "->", type(course_name))
print(is_completed, "->", type(is_completed), "\n")

#2.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F\n")

# 3. 
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

area = length * width
perimeter = 2 * (length + width)
print("Area of rectangle:", area)
print("Perimeter of rectangle:", perimeter, "\n")

# 4.
a = 10
b = 20

print("Comparison Operators (a=10, b=20):")
print("a == b:", a == b)
print("a != b:", a != b)
print("a < b:", a < b)
print("a > b:", a > b)

print("\nLogical Operators:")
print("a < b and b == 20:", a < b and b == 20)
print("a > b or b == 20:", a > b or b == 20)
print("not (a == b):", not (a == b))