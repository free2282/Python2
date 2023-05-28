from abc import ABC


class Mentor(ABC):
    def __init__(self, name: str, surname: str):
        self._name = name
        self._surname = surname
        self._courses_attached = []

    def add_course(self, course_name: str):
        self._courses_attached.append(course_name)

    def remove_course(self, course_name: str):
        self._courses_attached.remove(course_name)

    def get_name(self):
        return self._name

    def get_surname(self):
        return self._surname

    def get_courses_attached(self):
        return self._courses_attached
