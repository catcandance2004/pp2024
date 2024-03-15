import tkinter as tk
from pw8.input import input_students, input_courses, input_marks
from pw8.output import print_students, print_courses, print_marks
from pw8.domains.student import Student
from pw8.domains.course import Course
from pw8.domains.marks import Mark

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Student Mark Management System")
        self.geometry("800x600")

        self.students = []
        self.courses = []
        self.marks = []

        self.student_input_frame = tk.Frame(self)
        self.student_input_frame.pack()

        self.course_input_frame = tk.Frame(self)
        self.course_input_frame.pack()

        self.mark_input_frame = tk.Frame(self)
        self.mark_input_frame.pack()

        self.student_listbox = tk.Listbox(self.student_input_frame)
        self.student_listbox.pack(side=tk.LEFT)

        self.course_listbox = tk.Listbox(self.course_input_frame)
        self.course_listbox.pack(side=tk.LEFT)

        self.mark_listbox = tk.Listbox(self.mark_input_frame)
        self.mark_listbox.pack(side=tk.LEFT)

        self.student_input_button = tk.Button(self.student_input_frame, text="Input Students", command=self.input_students)
        self.student_input_button.pack(side=tk.LEFT)

        self.course_input_button = tk.Button(self.course_input_frame, text="Input Courses", command=self.input_courses)
        self.course_input_button.pack(side=tk.LEFT)

        self.mark_input_button = tk.Button(self.mark_input_frame, text="Input Marks", command=self.input_marks)
        self.mark_input_button.pack(side=tk.LEFT)

        self.print_students_button = tk.Button(self, text="Print Students", command=self.print_students)
        self.print_students_button.pack()

        self.print_courses_button = tk.Button(self, text="Print Courses", command=self.print_courses)
        self.print_courses_button.pack()

        self.print_marks_button = tk.Button(self, text="Print Marks", command=self.print_marks)
        self.print_marks_button.pack()

    def input_students(self):
        num_students = int(input("Enter number of students: "))
        self.students = input_students(num_students)
        self.student_listbox.delete(0, tk.END)
        for student in self.students:
            self.student_listbox.insert(tk.END, student.name)

    def input_courses(self):
        num_courses = int(input("Enter number of courses: "))
        self.courses = input_courses(num_courses)
        self.course_listbox.delete(0, tk.END)
        for course in self.courses:
            self.course_listbox.insert(tk.END, course.name)

    def input_marks(self):
        self.marks = input_marks(self.students, self.courses)
        self.mark_listbox.delete(0, tk.END)
        for mark in self.marks:
            student_name = next(filter(lambda s: s.id == mark.student_id, self.students)).name
            course_name = next(filter(lambda c: c.id == mark.course_id, self.courses)).nameself.mark_listbox.insert(tk.END, f"{student_name} - {course_name} - {mark.mark}")

    def print_students(self):
        print_students(self.students)

    def print_courses(self):
        print_courses(self.courses)

    def print_marks(self):
        print_marks(self.marks)

if __name__ == "__main__":
    app = App()
    app.mainloop()