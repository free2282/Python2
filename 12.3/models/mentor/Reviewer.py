from models.mentor.base.Mentor import Mentor
from models.student import Student


class Reviewer(Mentor):

    def rate_home_work(self, student: Student, course: str, grade: int):
        student.set_grade(course, grade)
        
    def __str__(self):
        return f"Имя: {self._name}\nФамилия: {self._surname}"

    def print_courses(self):
        for elemement in self.get_courses_attached():
            if elemement != None:
                print(elemement)

    def __add__(self, other: str):
        self.add_course(other)

    def __sub__(self, other: str):
        self.remove_course(other)

    def __hash__(self):
        return hash((self._name, self._surname))
