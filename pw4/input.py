from typing import List, Tuple
import numpy as np
from pw4.domains.student_mark import StudentMark
from pw4.domains.course import Course

def input_students(num: int) -> List[StudentMark]:
    students = []
    for i in range(num):
        student_id = int(input(f"Student {i+1} id: "))
        student_name = input(f"Student {i+1} name: ")
        student_dob = input(f"Student {i+1} DoB: ")
        student_mark = float(input(f"Student {i+1} mark: "))
        students.append(StudentMark(student_id, student_name, student_dob, student_mark))
    return students

def input_courses(num: int) -> List[Course]:
    courses = []
    for i in range(num):
        course_id = int(input(f"Course {i+1} id: "))
        course_name = input(f"Course {i+1} name: ")
        course_credit = int(input(f"Course {i+1} credit: "))
        courses.append(Course(course_id, course_name, course_credit))
    return courses