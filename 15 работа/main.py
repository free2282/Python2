from subclasses.lecture import Lecturer
from subclasses.reviewer import Reviewer
from subclasses.student import Student
from subclasses.course import Course
import statistics


def Flatten(list):
    return [item for sublist in list for item in sublist]


def CalcAvgGrade(gradeables, courseId: int):
    return statistics.mean(Flatten(map(lambda gradeable: gradeable(courseId), gradeables)))

pythonCourse1 = Course(1, "Python")
pythonCourse2 = Course(1, "Python")
pythonCourse3 = Course(1, "Python")
csharpCourse = Course(2, "C#")
cppCourse = Course(3, "C++")

lecturer1 = Lecturer('Lecture', '1')
lecturer1.AddCourse(pythonCourse1)
pythonCourse1.SetLecturer(lecturer1)

lecturer2 = Lecturer('Lecture', '2')
lecturer2.AddCourse(pythonCourse2)
pythonCourse2.SetLecturer(lecturer2)

lecturer3 = Lecturer('Lecture', '3')
lecturer3.AddCourse(pythonCourse3)
pythonCourse3.SetLecturer(lecturer3)

student1 = Student("Ryan ", "Gosling")

student1.AddCourse(pythonCourse1)
student1.AddCourse(pythonCourse2)
student1.AddCourse(pythonCourse3)
student1.AddCourse(csharpCourse)
student1.AddCourse(cppCourse)

student1.StartCourse(pythonCourse1.GetId())
student1.StartCourse(csharpCourse.GetId())
student1.FinishCourse(cppCourse.GetId())

student2 = Student("name2", "surname2")
student2.AddCourse(pythonCourse1)
student2.StartCourse(pythonCourse1.GetId())

reviewer = Reviewer('name1', 'surname1')
reviewer + pythonCourse1
reviewer.SetStudentGrade(student1, pythonCourse1.GetId(), 9)
reviewer.SetStudentGrade(student2, pythonCourse1.GetId(), 5)
reviewer + csharpCourse
students = [student1, student2]



print(f"Средняя оценка за домашнее задание по студентам в рамках курса по {pythonCourse1.GetTitle()} {pythonCourse1.GetId()}: ",
      CalcAvgGrade(students, pythonCourse1.GetId()))

student1.RateLecturer(pythonCourse1.GetId(), 3)
student2.RateLecturer(pythonCourse1.GetId(), 7)

lecturers = [lecturer1, lecturer2, lecturer3]

print(f"Средняя оценка за лекции лекторов в рамках курса по {pythonCourse1.GetTitle()}: ",
      CalcAvgGrade(lecturers, pythonCourse1.GetId()))

print("\nПервый студет умнее второго" if (student1 > student2)
      else "\nВторой студент умнее первого")

print(f"\nReviewer:\n{reviewer}")
print(f"\nLecturer1:\n{lecturer1}")
print(f"\nStudent1:\n{student1}\n")

print(f"Lecturer grades by courses: {lecturer1.GetGrades()}")
print(f"Student grades by courses: {student1.GetGrades()}")