import math
import numpy as np
import curses

class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.courses = []

    def input_marks(self, course_id, mark):
        mark = math.floor(mark * 10) / 10
        course = [c for c in self.courses if c[0] == course_id][0]
        if course:
            student = [s for s in course[1] if s[0] == self.id][0]
            if student:
                student[1] = mark
                print(f"Marks updated for student {self.name}")
            else:
                print(f"Student {self.name} not found in course {course[1]}")
        else:
            print(f"Course {course_id} not found")

    def list_courses(self):
        print("\nCourses:")
        for i, course in enumerate(self.courses, start=1):
            print(f"{i}. {course[1]}")

    def list_students(self):
        print("\nStudents:")
        for i, student in enumerate(self.students, start=1):
            print(f"{i}. {student[1]}")

    def show_student_marks(self, course_id):
        course = [c for c in self.courses if c[0] == course_id][0]
        if course:
            print(f"\nMarks for course {course[1]}:")
            for student in course[1]:
                print(f"{student[1]}: {student[2]}")
        else:
            print(f"Course {course_id} not found")

    def calculate_gpa(self):
        credits = np.array([c[2] for c in self.courses])
        marks = np.array([s[1] for s in[c[1] for c in self.courses] for s in c[1] if s[0] == self.id])
        gpa = np.average(marks, weights=credits)
        return gpa


class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.students = []

    def input_students(self, student_id, name, dob):
        student = [s for s in self.students if s[0] == student_id][0] if student else None
        if student:
            student[1] = name
            student[2] = dob
            print(f"Student {name} updated")
        else:
            self.students.append((student_id, name, dob))
            print(f"Student {name} added")

    def list_students(self):
        print("\nStudents:")
        for i, student in enumerate(self.students, start=1):
            print(f"{i}. {student[1]}")


class StudentMarkSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self, num):
        for i in range(num):
            student_id = int(input(f"Student {i+1} id: "))
            name = input(f"Student {i+1} name: ")
            dob = input(f"Student {i+1} DoB: ")
            for student in self.students:
                student.input_students(student_id, name, dob)

    def input_courses(self, num):
        for i in range(num):
            course_id = int(input(f"Course {i+1} id: "))
            name = input(f"Course {i+1} name: ")
            self.courses.append(Course(course_id, name))

    def input_marks(self):
        course_id = int(input("Select a course id: "))
        for course in self.courses:
            if course.id == course_id:
                for student in course.students:
                    mark = float(input(f"Enter mark for student {student[1]}: "))
                    student[3] = mark

    def list_courses(self):
        for course in self.courses:
            course.list_students()

    def list_students(self):
        for student in self.students:
            student.list_courses()

    def show_student_marks(self, course_id):
        for course in self.courses:
            if course.id == course_id:
                course.show_student_marks(course_id)

    def calculate_average_gpa(self):
        gpas = np.array([student.calculate_gpa() for student in self.students])
        avg_gpa = np.average(gpas)
        return avg_gpa

    def sort_students_by_gpa(self):
        self.students = sorted(self.students, key=lambda student: student.calculate_gpa(), reverse=True)


def main(stdscr):
    sms = StudentMarkSystem()

    num_students = int(input("Enter number of students: "))
    sms.input_students(num_students)

    num_courses = int(input("Enter number of courses: "))
    sms.input_courses(num_courses)

    sms.input_marks()

    sms.list_courses()
    sms.list_students()

    course_id = int(input("Enter course id to show student marks: "))
    sms.show_student_marks(course_id)

    avg_gpa = sms.calculate_average_gpa()
    print(f"\nAverage GPA: {avg_gpa}")

    sms.sort_students_by_gpa()
    print("\nStudents sorted by GPA:")
    for student in sms.students:
        print(f"{student.name}: {student.calculate_gpa()}")


curses.wrapper(main)