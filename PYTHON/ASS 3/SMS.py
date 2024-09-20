class Person:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

class Student(Person):
    def __init__(self, name, age, id, grade, enrolled_courses):
        super().__init__(name, age, id)
        self.grade = grade
        self.enrolled_courses = enrolled_courses

class Teacher(Person):
    def __init__(self, name, age, id, subject, assigned_courses):
        super().__init__(name, age, id)
        self.subject = subject
        self.assigned_courses = assigned_courses

class Course:
    def __init__(self, course_name, course_id):
        self.course_name = course_name
        self.course_id = course_id
        self.enrolled_students = []

    def calculate_average_grade(self):
        if not self.enrolled_students:
            return None
        total_grades = sum(student.grade for student in self.enrolled_students)
        return total_grades / len(self.enrolled_students)

class School:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.courses = []

    def enroll_student(self, student, course):
        student.enrolled_courses.append(course)
        course.enrolled_students.append(student)

    def assign_teacher(self, teacher, course):
        teacher.assigned_courses.append(course)
        course.teacher = teacher

    def view_students_in_course(self, course):
        print(f"Students in {course.course_name}:")
        for student in course.enrolled_students:
            print(f"{student.name} (Grade: {student.grade})")

    def view_courses_of_student(self, student):
        print(f"Courses enrolled by {student.name}:")
        for course in student.enrolled_courses:
            print(course.course_name)

    def calculate_average_grade_in_course(self, course):
        return course.calculate_average_grade()

# Create sample students, teachers, and courses
student1 = Student("Alice", 18, "123", 90, [])
student2 = Student("Bob", 17, "456", 85, [])
student3 = Student("Charlie", 16, "789", 95, [])

teacher1 = Teacher("Mr. Smith", 35, "100", "Math", [])
teacher2 = Teacher("Ms. Johnson", 30, "200", "Science", [])

course1 = Course("Math", "MATH101")
course2 = Course("Science", "SCI101")

# Enroll students and assign teachers
school = School()
school.enroll_student(student1, course1)
school.enroll_student(student2, course1)
school.enroll_student(student3, course1)

school.assign_teacher(teacher1, course1)

# Calculate average grade
average_grade = school.calculate_average_grade_in_course(course1)
print(f"Average grade in {course1.course_name}: {average_grade}")