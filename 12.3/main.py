from models.mentor.Lecturer import Lecturer
from models.mentor.Reviewer import Reviewer
from models.student.Student import Student


class AverageCalc:

    def __init__(self, grades_list: list[dict], name_to_find: str):
        self.__grades_list = grades_list
        self.__name_to_find = name_to_find

    def __float__(self):
        sum = 0
        count = 0
        for element in self.__grades_list:
            element_keys = element.keys()
            if self.__name_to_find in element_keys:
                grade = element[self.__name_to_find]
                sum = sum + grade
                count = count + 1
        average_grade = 0.0
        if count != 0:
            average_grade = sum / count
        return average_grade

    def get_name_to_find(self):
        return self.__name_to_find


def main():
    best_student = Student("Joel", "Embiid", "M")
    best_student.add_course_in_progress("Python")
    best_student.add_course_in_progress("Java")
    best_student.add_finished_courses("ML")

    not_best_student = Student("Lebron", "James", "M")
    not_best_student.add_course_in_progress('Python')

    almost_best_student = Student("Stephen", "Curry", "M")
    almost_best_student.add_course_in_progress("Python")

    cool_lecturer = Lecturer('Some', 'Buddy')
    cool_lecturer.add_course("Python")

    not_so_cool_lecturer = Lecturer("Vince", "Carter")
    not_so_cool_lecturer.add_course("Python")

    bad_lecturer = Lecturer("Jason", "Tatum")
    bad_lecturer.add_course("Python")

    cool_reviewer = Reviewer('Some', 'Buddy')
    cool_reviewer.add_course("Python")
    cool_reviewer.rate_home_work(best_student, "Python", 10)
    cool_reviewer.rate_home_work(not_best_student, "Python", 8)
    cool_reviewer.rate_home_work(almost_best_student, "Python", 9)
    cool_reviewer + "Java"

    students_grades_list = [best_student.get_grades(), almost_best_student.get_grades(), not_best_student.get_grades()]

    average_calc_students = AverageCalc(students_grades_list, "Python")

    print(f"Средняя оценка студентов за курс {average_calc_students.get_name_to_find()} от проверяющих: ",
          float(average_calc_students))

    best_student.rate_lecturer("Python", cool_lecturer, 10)
    best_student.rate_lecturer("Python", not_so_cool_lecturer, 7)
    best_student.rate_lecturer("Python", bad_lecturer, 4)

    lecturers_grades_list = [cool_lecturer.get_grades(), not_so_cool_lecturer.get_grades(), bad_lecturer.get_grades()]

    average_calc_lecturers = AverageCalc(lecturers_grades_list, "Python")

    print(f"Средняя оценка лекторов за курс {average_calc_lecturers.get_name_to_find()} от студентов: ",
          float(average_calc_lecturers))

    print("Лучше ли первый студент второго? ", best_student > not_best_student)

    print()

    print(cool_lecturer)

    print()

    print(best_student)

    print()

    print("Имя студента: ", best_student.get_name())
    print("Имя преподавателя: ", cool_lecturer.get_name())
    print("Оценки лектора по курсам: ", cool_lecturer.get_grades())
    print("Оценки студента по курсам: ", best_student.get_grades())


main()
