# 1.
print("Numbers from 1 to 100:")
for i in range(1, 101):
    print(i, end=" ")
print("\n")

# 2. 
table_num = int(input("Enter a number for multiplication table: "))
print(f"Multiplication Table of {table_num}:")
for i in range(1, 11):
    print(f"{table_num} x {i} = {table_num * i}")
print()

# 3. 
n = int(input("Enter N to find sum from 1 to N: "))
total = 0
for i in range(1, n + 1):
    total += i
print(f"Sum of numbers from 1 to {n} is: {total}\n")

# 4.
word = input("Enter a word to count vowels: ")
vowel_count = 0
for char in word.lower():
    if char in "aeiou":
        vowel_count += 1
print(f"Number of vowels in '{word}': {vowel_count}\n")

# 5. 
print("Prime numbers between 1 and 100:")
for num in range(2, 101):
    is_prime = True
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()