from typing import List, Tuple

class Course:
    def __init__(self, id: int, name: str, credit: int):
        self.id = id
        self.name = name
        self.credit = credit
        self.students = []

    def input_students(self, student_id: int, name: str, dob: str, mark: float):
        student = [s for s in self.students if s.id == student_id][0] if student else None
        if student:
            student.name = name
            student.dob = dob
            student.mark = mark
            print(f"Student {name} updated")
        else:
            self.students.append(Student(student_id, name, dob, mark))
            print(f"Student {name} added")

    def list_students(self):
        print("\nStudents:")
        for i, student in enumerate(self.students, start=1):
            print(f"{i}. {student.name}")