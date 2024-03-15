from typing import List, Tuple
import math

class Student:
    def __init__(self, id: int, name: str, dob: str):
        self.id = id
        self.name = name
        self.dob = dob
        self.courses = []

    def input_marks(self, course_id: int, mark: float):
        mark = math.floor(mark * 10) / 10
        course = [c for c in self.courses if c.id == course_id][0]
        if course:
            student = [s for s in course.students if s.id == self.id][0]
            if student:
                student.mark = mark
                print(f"Marks updated for student {self.name}")
            else:
                print(f"Student {self.name} not found in course {course.name}")
        else:
            print(f"Course {course_id} not found")

    def list_courses(self):
        print("\nCourses:")
        for i, course in enumerate(self.courses, start=1):
            print(f"{i}. {course.name}")

    def show_student_marks(self, course_id: int):
        course = [c for c in self.courses if c.id == course_id][0]
        if course:
            print(f"\nMarks for course {course.name}:")
            for student in course.students:
                print(f"{student.name}: {student.mark}")
        else:
            print(f"Course {course_id} not found")

    def calculate_gpa(self) -> float:
        credits = np.array([c.credit for c in self.courses])
        marks = np.array([s.mark for s in[c.students for c in self.courses] for s in c.students if s.id == self.id])
        gpa = np.average(marks, weights=credits)
        return gpa