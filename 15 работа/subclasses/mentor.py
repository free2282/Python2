from abc import ABC
from subclasses.course import Course
from typing import Callable
class Mentor(ABC):
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.courses = []
    def GetName(self):
        return self.name
    def GetSurname(self):
        return self.surname
    def GetCourses(self):
        return self.courses
    def AddCourse(self, course: Course):
        self.courses.append(course)
    def RemoveCourse(self, course: Course):
        courseFilter: Callable[[Course], bool] = lambda c: c.GetId() != course.GetId()
        self.courses = filter(courseFilter, self.courses)