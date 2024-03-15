import json
import pickle
import gzip
import shutil

def input_students(num: int) -> List[StudentMark]:
    students = []
    for i in range(num):
        student_id = int(input(f"Student {i+1} id: "))
        name = input(f"Student {i+1} name: ")
        dob = input(f"Student {i+1} DoB: ")
        students.append(StudentMark(student_id, name, dob))
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return students

def input_courses(num: int) -> List[Course]:
    courses = []
    for i in range(num):
        course_id = int(input(f"Course {i+1} id: "))
        name = input(f"Course {i+1} name: ")
        credit = int(input(f"Course {i+1} credit: "))
        courses.append(Course(course_id, name, credit))
    with open("courses.pickle", "wb") as f:
        pickle.dump(courses, f)
    return courses

def input_marks(students: List[StudentMark], courses: List[Course]):
    marks = []
    for course in courses:
        for student in students:
            mark = float(input(f"Enter mark for student {student.name} in course {course.name}: "))
            marks.append(StudentMark(student.id, course.id, mark))
    with open("marks.pickle", "wb") as f:
        pickle.dump(marks, f)
    return marks