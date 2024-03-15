import importlib
import pw5.input as input_module
import pw5.output as output_module
import pw5.domains as domains_module

if __name__ == "__main__":
    Student = domains_module.Student
    Course = domains_module.Course
    StudentMark = domains_module.StudentMark

    input_module = importlib.reload(input_module)
    output_module = importlib.reload(output_module)

    output_module.main(Student, Course, StudentMark)