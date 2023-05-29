from subclasses.mentor import Mentor
from subclasses.student import Student
from subclasses.course import Course
class Reviewer(Mentor):
    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)
    def PrintCourses(self):
        for elemement in self.GetCourses():
            print(elemement)
    def __add__(self, course: Course):
        self.AddCourse(course)
    def __sub__(self, course: Course):
        self.RemoveCourse(course)
    def __hash__(self):
        return hash((self.name, self.surname))
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"
    def SetStudentGrade(self, student: Student, courseId: int, grade: int):
        student.SetGrade(courseId, grade)