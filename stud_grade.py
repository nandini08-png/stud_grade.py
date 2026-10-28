# Student Grade Calculator
# Suitable for running through a Jenkins pipeline

def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def display_student_result(name, marks):
    print("\n" + "=" * 40)
    print("       STUDENT GRADE CALCULATOR")
    print("=" * 40)

    print("Student Name:", name)
    print("-" * 40)

    total = 0

    for subject, mark in marks.items():
        print(f"{subject}: {mark}/100")
        total += mark

    average = total / len(marks)
    grade = calculate_grade(average)

    print("-" * 40)
    print("Total Marks:", total, "/", len(marks) * 100)
    print(f"Average Marks: {average:.2f}%")
    print("Final Grade:", grade)

    if average >= 50:
        print("Result: PASS")
    else:
        print("Result: FAIL")

    print("=" * 40)


def main():
    # Sample student data for automated Jenkins execution
    student_name = "Shreya"

    student_marks = {
        "Computer Science": 85,
        "Python Programming": 90,
        "Mathematics": 78,
        "Computer Networks": 88,
        "Software Engineering": 92
    }

    display_student_result(student_name, student_marks)


if __name__ == "__main__":
    main()