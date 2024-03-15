# 1.student.mark.py

def input_students(num):
    """Input student information: id, name, DoB"""
    return [(i, input(f"Student {i+1} name: "), input(f"Student {i+1} DoB: ")) for i in range(num)]

def input_courses(num):
    """Input course information: id, name"""
    return [(i, input(f"Course {i+1} name: ")) for i in range(num)]

def input_marks(students, courses):
    """Select a course, input marks for students in this course"""
    course_id = int(input("Select a course id: ")) - 1
    for student in students:
        student_id = int(input(f"Enter student {student[0]} id: ")) - 1
        mark = int(input(f"Enter mark for student {student[1]}: "))
        course = [c for c in courses if c[0] == course_id][0]
        student = [s for s in students if s[0] == student_id][0]
        student += (course[1], mark)
def list_courses(courses):
    """List courses"""
    print("\nCourses:")
    for i, course in enumerate(courses, start=1):
        print(f"{i}. {course[1]}")

def list_students(students):
    """List students"""
    print("\nStudents:")
    for i, student in enumerate(students, start=1):
        print(f"{i}. {student[1]}")

def show_student_marks(course_id, students):
    """Show student marks for a given course"""
    course = [c for c in courses if c[0] == course_id][0]
    print(f"\nMarks for course {course[1]}:")
    for student in students:
        if student[-2] == course[1]:
            print(f"{student[1]}: {student[-1]}")

if __name__ == "__main__":
    num_students = int(input("Enter number of students: "))
    students = input_students(num_students)

    num_courses = int(input("Enter number of courses: "))
    courses = input_courses(num_courses)

    input_marks(students, courses)

    list_courses(courses)
    list_students(students)

    course_id = int(input("Enter course id to show student marks: ")) - 1
    show_student_marks(course_id, students)