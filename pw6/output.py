import curses
import gzip
import shutil
import pickle
import os

def main_screen(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.nodelay(1)
    stdscr.timeout(100)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    stdscr.attron(curses.color_pair(1))

def print_centered(stdscr, text):
    height, width = stdscr.getmaxyx()
    x = (width // 2) - (len(text) // 2)
    y = height // 2
    stdscr.addstr(y, x, text)

def print_menu(stdscr, options):
    height, width = stdscr.getmaxyx()
    y = height // 2
    x = width // 2
    i = 1
    for option in options:
        if i == 1:
            stdscr.addstr(y, x, f"{i}. {option}", curses.A_STANDOUT)
        else:
            stdscr.addstr(y, x, f"{i}. {option}")
        i += 1
        y += 1

def get_input(stdscr):
    return stdscr.getch()

def compress_data(data, method):
    with gzip.open("students.dat", "wb") as f:
        if method == "gzip":
            f.write(gzip.compress(pickle.dumps(data)))
        elif method == "bz2":
            f.write(bz2.compress(pickle.dumps(data)))
        elif method =="lzma":
            f.write(lzma.compress(pickle.dumps(data)))

def decompress_data(method):
    with gzip.open("students.dat", "rb") as f:
        data = pickle.loads(gzip.decompress(f.read()))
    return data

def main(stdscr):
    print_centered(stdscr, "Student Mark System")
    options = ["Input Students", "Input Courses", "Input Marks", "List Students", "List Courses", "Show Student Marks", "Calculate GPA", "Sort Students by GPA", "Quit"]
    if "students.dat" in os.listdir():
        with open("students.dat", "rb") as f:
            data = decompress_data(method)
            students = data["students"]
            courses = data["courses"]
            marks = data["marks"]
    else:
        num_students = int(input("Enter number of students: "))
        students = input_students(num_students)

        num_courses = int(input("Enter number of courses: "))
        courses = input_courses(num_courses)

        marks = input_marks(students, courses)

        data = {
            "students": students,
            "courses": courses,
            "marks": marks
        }

        method = input("Select a compression method (gzip, bz2, lzma): ")
        compress_data(data, method)

    while True:
        print_menu(stdscr, options)
        key = get_input(stdscr)
        if key == ord("1"):
            # input_students(num_students)
            pass
        elif key == ord("2"):
            # input_courses(num_courses)
            pass
        elif key == ord("3"):
            # input_marks(students, courses)
            pass
        elif key == ord("4"):
            for course in courses:
                course.list_students()
        elif key == ord("5"):
            for course in courses:
              course.list_courses()
        elif key == ord("6"):
            course_id = int(input("Enter course id to show student marks: "))
            for course in courses:
                if course.id == course_id:
                    course.show_student_marks()
        elif key == ord("7"):
            for student in students:
                print(f"{student.name}: {student.calculate_gpa()}")
        elif key == ord("8"):
            students = sorted(students, key=lambda student: student.calculate_gpa(), reverse=True)
        elif key == ord("9"):
            break