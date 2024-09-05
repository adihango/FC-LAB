def calculate_average_grade(grades):
    """Calculates the average grade for a student."""
    total_grades = sum(grades.values())
    num_courses = len(grades)
    return total_grades / num_courses

def determine_highest_lowest_scores(students):
    """Determines the highest and lowest scores among all students."""
    highest_score = 0
    lowest_score = 100  # Assuming grades are out of 100
    for student in students:
        for grade in student["grades"].values():
            if grade > highest_score:
                highest_score = grade
            if grade < lowest_score:
                lowest_score = grade
    return highest_score, lowest_score

def categorize_students(students, grade_threshold):
    """Categorizes students based on their average grade."""
    above_threshold = []
    below_threshold = []
    for student in students:
        average_grade = calculate_average_grade(student["grades"])
        if average_grade >= grade_threshold:
            above_threshold.append(student["student_name"])
        else:
            below_threshold.append(student["student_name"])
    return above_threshold, below_threshold

def analyze_student_grades(students):
    """Analyzes student grades and provides insights."""
    average_grades = {}
    highest_score, lowest_score = determine_highest_lowest_scores(students)
    above_threshold, below_threshold = categorize_students(students, 70)  # Adjust threshold as needed

    for student in students:
        average_grade = calculate_average_grade(student["grades"])
        average_grades[student["student_name"]] = average_grade

    print("Average Grades:")
    for student, grade in average_grades.items():
        print(f"{student}: {grade}")

    print("\nHighest Score:", highest_score)
    print("Lowest Score:", lowest_score)

    print("\nStudents Above Threshold:", above_threshold)
    print("Students Below Threshold:", below_threshold)

# Sample student data
students = [
    {"student_name": "Ankur", "grades": {"Math": 85, "Science": 92, "English": 78}},
    {"student_name": "Priya", "grades": {"Math": 90, "Science": 88, "English": 95}},
    {"student_name": "Rahul", "grades": {"Math": 75, "Science": 80, "English": 70}}
]

analyze_student_grades(students)