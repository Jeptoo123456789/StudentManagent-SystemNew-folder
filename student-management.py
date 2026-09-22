import json
import os

FILE_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.json")


# =========================
# LOAD STUDENTS
# =========================
def load_students():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (OSError, json.JSONDecodeError):
            return []
    return []


# =========================
# SAVE STUDENTS
# =========================
def save_students():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# =========================
# CALCULATE GRADE
# =========================
def calculate_grade(marks):

    if marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


# =========================
# ADD STUDENT
# =========================
def add_student():

    print("\n===== ADD STUDENT =====")

    student_id = input("Enter student ID: ").strip()

    # Check duplicate ID
    for student in students:
        if student["id"] == student_id:
            print("A student with this ID already exists.")
            return

    name = input("Enter student name: ").strip()
    gender = input("Enter gender: ").strip()
    course = input("Enter course: ").strip()

    while True:
        try:
            marks = float(input("Enter marks (0-100): "))

            if 0 <= marks <= 100:
                break
            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

    grade = calculate_grade(marks)

    student = {
        "id": student_id,
        "name": name,
        "gender": gender,
        "course": course,
        "marks": marks,
        "grade": grade
    }

    students.append(student)
    save_students()

    print("\nStudent added successfully!")
    print("Grade:", grade)


# =========================
# DISPLAY STUDENTS
# =========================
def display_students():

    print("\n===== ALL STUDENTS =====")

    if not students:
        print("No students registered.")
        return

    for number, student in enumerate(students, start=1):

        print(f"\nStudent {number}")
        print("----------------------")
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Gender:", student["gender"])
        print("Course:", student["course"])
        print("Marks:", student["marks"])
        print("Grade:", student["grade"])


# =========================
# SEARCH STUDENT
# =========================
def search_student():

    print("\n===== SEARCH STUDENT =====")

    student_id = input("Enter student ID: ").strip()

    for student in students:

        if student["id"] == student_id:

            print("\nStudent Found!")
            print("----------------------")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Gender:", student["gender"])
            print("Course:", student["course"])
            print("Marks:", student["marks"])
            print("Grade:", student["grade"])

            return

    print("Student not found.")


# =========================
# UPDATE STUDENT
# =========================
def update_student():

    print("\n===== UPDATE STUDENT =====")

    student_id = input("Enter student ID: ").strip()

    for student in students:

        if student["id"] == student_id:

            print("\nCurrent details:")
            print("Name:", student["name"])
            print("Gender:", student["gender"])
            print("Course:", student["course"])
            print("Marks:", student["marks"])

            print("\nLeave a field empty to keep the current value.")

            name = input("New name: ").strip()
            gender = input("New gender: ").strip()
            course = input("New course: ").strip()
            marks = input("New marks: ").strip()

            if name:
                student["name"] = name

            if gender:
                student["gender"] = gender

            if course:
                student["course"] = course

            if marks:

                try:
                    new_marks = float(marks)

                    if 0 <= new_marks <= 100:
                        student["marks"] = new_marks
                        student["grade"] = calculate_grade(new_marks)
                    else:
                        print("Marks must be between 0 and 100.")
                        return

                except ValueError:
                    print("Invalid marks.")
                    return

            save_students()

            print("Student information updated successfully.")
            return

    print("Student not found.")


# =========================
# DELETE STUDENT
# =========================
def delete_student():

    print("\n===== DELETE STUDENT =====")

    student_id = input("Enter student ID: ").strip()

    for student in students:

        if student["id"] == student_id:

            print("\nStudent found:")
            print("Name:", student["name"])
            print("ID:", student["id"])

            confirmation = input(
                "Are you sure you want to delete this student? (y/n): "
            ).lower()

            if confirmation == "y":

                students.remove(student)
                save_students()

                print("Student deleted successfully.")

            else:
                print("Deletion cancelled.")

            return

    print("Student not found.")


# =========================
# STATISTICS
# =========================
def statistics():

    print("\n===== STUDENT STATISTICS =====")

    if not students:
        print("No student records available.")
        return

    total = len(students)

    total_marks = sum(student["marks"] for student in students)

    average = total_marks / total

    highest = max(students, key=lambda student: student["marks"])

    lowest = min(students, key=lambda student: student["marks"])

    passed = sum(
        1 for student in students
        if student["marks"] >= 50
    )

    failed = total - passed

    print("Total students:", total)
    print("Average marks:", round(average, 2))

    print("\nHighest Marks")
    print("Name:", highest["name"])
    print("Marks:", highest["marks"])

    print("\nLowest Marks")
    print("Name:", lowest["name"])
    print("Marks:", lowest["marks"])

    print("\nPassed:", passed)
    print("Failed:", failed)


# =========================
# SORT STUDENTS
# =========================
def sort_students():

    print("\n===== SORT STUDENTS =====")

    if not students:
        print("No students available.")
        return

    print("1. Sort by name")
    print("2. Sort by marks")

    choice = input("Choose option: ")

    if choice == "1":
                sorted_students = sorted(
            students,
            key=lambda student: student["name"].lower()
        )

    elif choice == "2":

        sorted_students = sorted(
            students,
            key=lambda student: student["marks"],
            reverse=True
        )

    else:
        print("Invalid choice.")
        return

    print("\n===== SORTED STUDENTS =====")

    for student in sorted_students:

        print(
            f"{student['id']} | "
            f"{student['name']} | "
            f"{student['marks']} | "
            f"{student['grade']}"
        )


# =========================
# ADMIN LOGIN
# =========================
def login():

    print("\n==============================")
    print("   STUDENT MANAGEMENT SYSTEM")
    print("==============================")

    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "1234":
        print("\nLogin successful!")
        return True

    print("\nInvalid username or password.")
    return False


# =========================
# MAIN MENU
# =========================
def main_menu():

    while True:

        print("\n")
        print("====================================")
        print("      STUDENT MANAGEMENT SYSTEM")
        print("====================================")

        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Student Statistics")
        print("7. Sort Students")
        print("8. Save Records")
        print("9. Logout")
        print("====================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            statistics()

        elif choice == "7":
            sort_students()

        elif choice == "8":
            save_students()
            print("Records saved successfully.")

        elif choice == "9":
            print("Logging out...")
            break

        else:
            print("Invalid choice. Please try again.")


# =========================
# PROGRAM START
# =========================

if __name__ == "__main__":
    students = load_students()

    if login():
        main_menu()
    else:
        print("Access denied.")



