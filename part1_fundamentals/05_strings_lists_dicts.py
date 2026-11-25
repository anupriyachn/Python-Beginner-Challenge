# 1. 
subjects = ["Mathematics", "Physics", "Computer Science", "English", "Electronics"]
print("Subjects List:")
for subject in subjects:
    print("-", subject)
print()

# 2. 
marks = []
print("Enter 5 marks:")
for i in range(5):
    m = float(input(f"Enter mark {i + 1}: "))
    marks.append(m)

print("Total Marks:", sum(marks))
print("Average Marks:", sum(marks) / len(marks))
print("Highest Mark:", max(marks))
print("Lowest Mark:", min(marks), "\n")

# 3. 
student = {
    "name": "Anupriya Singh Chouhan",
    "roll_number": 126,
    "marks": 99.9
}
print("Student Dictionary:", student)
print(f"Name: {student['name']}, Roll No: {student['roll_number']}, Marks: {student['marks']}\n")

# 4. 
names = ["Anupriya", "Aabha", "Arti", "Atishay", "Bharat"]
search_name = input("Enter a name to search in the list: ").strip()
if search_name in names:
    print(f"'{search_name}' exists in the list!\n")
else:
    print(f"'{search_name}' does NOT exist in the list.\n")

# 5. 
text = input("Enter a string to count character frequency: ")
char_freq = {}
for ch in text:
    char_freq[ch] = char_freq.get(ch, 0) + 1

print("Character frequencies:", char_freq)