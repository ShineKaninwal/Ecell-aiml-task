
students_predefined = [
    {"roll_no": 101, "name": "Shine",   "subject": "Math",     "marks": 100.0},
    {"roll_no": 102, "name": "Avni",     "subject": "Science",  "marks": 92.0},
    {"roll_no": 103, "name": "Manvi", "subject": "English",  "marks": 76.0},
    {"roll_no": 104, "name": "Jaya",   "subject": "History",  "marks": 85.0},
    {"roll_no": 105, "name": "Devanshi",     "subject": "Computer", "marks": 95.0},
]

def display_students(students):
    if not students:
        print("No student records to display.")
        return
    print("\n--- Student Records ---")
    for s in students:
        print(f"Roll No: {s['roll_no']}, Name: {s['name']}, Subject: {s['subject']}, Marks: {s['marks']}")

def highest_marks(students):
    if not students:
        print("No students to evaluate for highest marks.")
        return
    topper = max(students, key=lambda x: x["marks"])
    print("\n--- Highest Marks ---")
    print(f"Roll No: {topper['roll_no']}, Name: {topper['name']}, Subject: {topper['subject']}, Marks: {topper['marks']}")

def average_marks(students):
    if not students:
        print("No students to calculate average.")
        return
    total = sum(s["marks"] for s in students)
    avg = total / len(students)
    print(f"\n--- Average Marks ---\nAverage = {avg:.2f}")

def input_students(n=5):
    """Collect n valid student records from user. Keeps asking until n valid entries are entered."""
    students = []
    print(f"\nEnter details for {n} students (press Enter after each input):")
    while len(students) < n:
        idx = len(students) + 1
        print(f"\n--- Student {idx} ---")
        try:
            roll_no_raw = input("Enter Roll No (integer): ").strip()
            if roll_no_raw == "":
                print("Roll No cannot be empty. Try again.")
                continue
            roll_no = int(roll_no_raw)

            name = input("Enter Name: ").strip()
            if not name:
                print("Name cannot be empty. Try again.")
                continue

            subject = input("Enter Subject: ").strip()
            if not subject:
                print("Subject cannot be empty. Try again.")
                continue

            marks_raw = input("Enter Marks (number 0-100): ").strip()
            if marks_raw == "":
                print("Marks cannot be empty. Try again.")
                continue
            marks = float(marks_raw)
            if marks < 0 or marks > 100:
                print("Marks should be between 0 and 100. Try again.")
                continue

            students.append({
                "roll_no": roll_no,
                "name": name,
                "subject": subject,
                "marks": marks
            })
        except ValueError as ve:
            print("Invalid input:", ve, "- please re-enter this student's details.")
            continue
    return students

if __name__ == "__main__":
    print("PART A: Predefined Students")
    display_students(students_predefined)
    highest_marks(students_predefined)
    average_marks(students_predefined)

    print("\nPART B: User Entered Students")
    students_input = input_students(5)
    display_students(students_input)
    highest_marks(students_input)
    average_marks(students_input)
