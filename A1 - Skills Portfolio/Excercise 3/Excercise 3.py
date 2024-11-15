import os

# File path
FILE_PATH = "studentMarks.txt"

# Function to load student data from file
def load_data():
    students = []
    with open(FILE_PATH, 'r') as file:
        num_students = int(file.readline().strip())
        for line in file:
            parts = line.strip().split(',')
            student_code = int(parts[0])
            name = parts[1]
            marks = list(map(int, parts[2:5]))
            exam_mark = int(parts[5])
            students.append({
                "code": student_code,
                "name": name,
                "course_marks": marks,
                "exam_mark": exam_mark
            })
    return students

# Function to calculate total and percentage marks
def calculate_results(student):
    total_coursework = sum(student["course_marks"])
    total_marks = total_coursework + student["exam_mark"]
    percentage = (total_marks / 160) * 100
    return total_coursework, student["exam_mark"], percentage, get_grade(percentage)

# Function to get grade based on percentage
def get_grade(percentage):
    if percentage >= 70:
        return 'A'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 50:
        return 'C'
    elif percentage >= 40:
        return 'D'
    else:
        return 'F'

# Menu functions
def view_all_students(students):
    total_percentage = 0
    for student in students:
        coursework, exam, percentage, grade = calculate_results(student)
        total_percentage += percentage
        print(f"Name: {student['name']}, Code: {student['code']}, Coursework: {coursework}, Exam: {exam}, "
              f"Percentage: {percentage:.2f}%, Grade: {grade}")
    avg_percentage = total_percentage / len(students)
    print(f"\nTotal Students: {len(students)}, Average Percentage: {avg_percentage:.2f}%\n")

def view_individual_student(students):
    print("\nSelect a student by their number or name:")
    for i, student in enumerate(students, start=1):
        print(f"{i}. {student['name']} (Code: {student['code']})")
    choice = input("Enter student number or name: ")
    student = next((s for s in students if choice == s['name'] or choice == str(s['code'])), None)
    if student:
        coursework, exam, percentage, grade = calculate_results(student)
        print(f"\nName: {student['name']}, Code: {student['code']}, Coursework: {coursework}, Exam: {exam}, "
              f"Percentage: {percentage:.2f}%, Grade: {grade}\n")
    else:
        print("Student not found.\n")

def show_highest_score(students):
    highest_student = max(students, key=lambda s: sum(s["course_marks"]) + s["exam_mark"])
    coursework, exam, percentage, grade = calculate_results(highest_student)
    print(f"Student with Highest Score:\nName: {highest_student['name']}, Code: {highest_student['code']}, "
          f"Coursework: {coursework}, Exam: {exam}, Percentage: {percentage:.2f}%, Grade: {grade}\n")

def show_lowest_score(students):
    lowest_student = min(students, key=lambda s: sum(s["course_marks"]) + s["exam_mark"])
    coursework, exam, percentage, grade = calculate_results(lowest_student)
    print(f"Student with Lowest Score:\nName: {lowest_student['name']}, Code: {lowest_student['code']}, "
          f"Coursework: {coursework}, Exam: {exam}, Percentage: {percentage:.2f}%, Grade: {grade}\n")

# Main menu
def main():
    if not os.path.exists(FILE_PATH):
        print("File not found. Please ensure 'studentMarks.txt' is in the correct location.")
        return
    
    students = load_data()
    while True:
        print("\nMenu:")
        print("1. View all student records")
        print("2. View individual student record")
        print("3. Show student with highest total score")
        print("4. Show student with lowest total score")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            view_all_students(students)
        elif choice == "2":
            view_individual_student(students)
        elif choice == "3":
            show_highest_score(students)
        elif choice == "4":
            show_lowest_score(students)
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
