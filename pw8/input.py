import json
import pickle
import gzip
import shutil
import threading

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
            mark = float(input(f"Entermark for student {student.name} in course {course.name}: "))
            marks.append(StudentMark(student.id, course.id, mark))
    with open("marks.pickle", "wb") as f:
        pickle.dump(marks, f)
    return marks

def save_data():
    students = []
    courses = []
    marks = []
    if os.path.exists("students.pickle"):
        with open("students.pickle", "rb") as f:
            students = pickle.load(f)
    if os.path.exists("courses.pickle"):
        with open("courses.pickle", "rb") as f:
            courses = pickle.load(f)
    if os.path.exists("marks.pickle"):
        with open("marks.pickle", "rb") as f:
            marks = pickle.load(f)
    data = {
        "students": students,
        "courses": courses,
        "marks": marks
    }
    method = "gzip"
    with gzip.open("students.dat", "wb") as f:
        if method == "gzip":
            f.write(gzip.compress(pickle.dumps(data)))
        elif method == "bz2":
            f.write(bz2.compress(pickle.dumps(data)))
        elif method == "lzma":
            f.write(lzma.compress(pickle.dumps(data)))

def load_data():
    if os.path.exists("students.dat"):
        with open("students.dat", "rb") as f:
            data = decompress_data(method)
            students = data["students"]
            courses = data["courses"]
            marks = data["marks"]
    else:
        students = []
        courses = []
        marks = []
    return students, courses, marks