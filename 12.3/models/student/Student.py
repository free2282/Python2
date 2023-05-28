from models.mentor.Lecturer import Lecturer


class Student:
    def __init__(self, name: str, surname: str, gender: str):
        self.__name = name
        self.__surname = surname
        self.__gender = gender
        self.__finished_courses = []
        self.__courses_in_progress = []
        self.__grades = {}

    def add_finished_courses(self, course_name: str):
        self.__finished_courses.append(course_name)

    def add_course_in_progress(self, course_name: str):
        self.__courses_in_progress.append(course_name)

    def set_grade(self, course_name: str, grade: int):
        self.__grades[course_name] = grade

    def rate_lecturer(self, course_name: str, lecturer: Lecturer, grade: int):
        if (self.__finished_courses.__contains__(course_name) or self.__courses_in_progress.__contains__(
                course_name)):
            lecturer.set_grade(course_name, grade)

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_finished_courses(self):
        return self.__finished_courses

    def get_courses_in_progress(self):
        return self.__courses_in_progress

    def get_grades(self):
        return self.__grades

    def calculate_average_grade(self) -> float:
        elements_sum = 0
        elements_number = 0

        for key in self.__grades.keys():
            elements_sum = elements_sum + self.__grades[key]
            elements_number = elements_number + 1

        if (elements_number != 0):
            average_grade = elements_sum / elements_number
        else:
            average_grade = 0.0

        return average_grade

    def __get_courses_in_progress_as_string(self):
        result_string = ""
        for index, course in enumerate(self.__courses_in_progress):
            if index == 0:
                result_string = course
            else:
                result_string = result_string + f", {course}"
        return result_string

    def __get_finished_courses_as_string(self):
        result_string = ""
        for index, course in enumerate(self.__finished_courses):
            if index == 0:
                result_string = course
            else:
                result_string = result_string + f", {course}"
        return result_string

    def __str__(self):
        return f"Имя: {self.__name}\nФамилия: {self.__surname}\nСредняя оценка за лекции: {self.calculate_average_grade()}\nКурсы в процессе изучения: {self.__get_courses_in_progress_as_string()} \nЗавершенные курсы: {self.__get_finished_courses_as_string()}"

    def __lt__(self, other):
        return self.calculate_average_grade() < other.calculate_average_grade()

    def __gt__(self, other):
        return self.calculate_average_grade() > other.calculate_average_grade()

    def __hash__(self):
        return hash((self.__name, self.__surname, self.__gender))
