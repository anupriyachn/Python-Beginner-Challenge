import json
import os

# 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "students_data.json")


def load_students():
    """Load saved student records from file safely."""
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            content = file.read().strip()
            return json.loads(content) if content else []
    except (json.JSONDecodeError, IOError):
        return []


def save_students(students):
    """Save student records permanently to file."""
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student(students):
    """Collect name, roll number, and marks, then save."""
    print("\n--- Add New Student ---")
    name = input("Enter student name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return

    roll_no = input("Enter roll number: ").strip()
    if not roll_no:
        print("Error: Roll number cannot be empty.")
        return

    for student in students:
        if student["roll_no"] == roll_no:
            print(f"Error: Roll number '{roll_no}' already exists!")
            return

    try:
        marks_raw = input("Enter marks separated by spaces (e.g. 85 90 78): ").strip()
        marks = [float(m) for m in marks_raw.split()]
        if not marks:
            print("Error: Please enter at least one mark.")
            return
    except ValueError:
        print("Error: Invalid marks! Enter numeric values only.")
        return

    students.append({
        "name": name,
        "roll_no": roll_no,
        "marks": marks
    })
    save_students(students)
    print(f"Success: Student '{name}' (Roll No: {roll_no}) added and saved!")


def view_all_students(students):
    """Display all saved student records in a clean table format."""
    print("\n--- All Student Records ---")
    if not students:
        print("No student records found.")
        return

    print(f"{'Roll No':<12} | {'Name':<20} | {'Marks'}")
    print("-" * 55)
    for student in students:
        marks_str = ", ".join(str(m) for m in student["marks"])
        print(f"{student['roll_no']:<12} | {student['name']:<20} | {marks_str}")


def search_student(students):
    """Search for a student using their roll number."""
    print("\n--- Search Student ---")
    roll_no = input("Enter roll number to search: ").strip()
    for student in students:
        if student["roll_no"] == roll_no:
            print(f"Record Found -> Roll No: {student['roll_no']} | Name: {student['name']} | Marks: {student['marks']}")
            return
    print(f"No student found with roll number '{roll_no}'.")


def calculate_average_marks(students):
    """Calculate and display average marks for a specific student."""
    print("\n--- Calculate Average Marks ---")
    roll_no = input("Enter roll number: ").strip()
    for student in students:
        if student["roll_no"] == roll_no:
            avg = sum(student["marks"]) / len(student["marks"])
            print(f"Student: {student['name']} (Roll No: {roll_no})")
            print(f"Marks: {student['marks']} -> Average Marks: {avg:.2f}")
            return
    print(f"No student found with roll number '{roll_no}'.")


def main():
    students = load_students()
    while True:
        print("\n====================================")
        print("     STUDENT MANAGEMENT SYSTEM      ")
        print("====================================")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student by roll number")
        print("4. Calculate average marks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_all_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            calculate_average_marks(students)
        elif choice == "5":
            print("Records saved. Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a number between 1 and 5.")


if __name__ == "__main__":
    main()