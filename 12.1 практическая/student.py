class Student(object):
    name = "Ivan"
    age = 18
    groupNumber = "10A"

    def __init__(self, name, age, groupNumber) -> None:
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self) -> str:
        return self.name

    def getAge(self) -> int:
        return self.age

    def getGroupNumber(self) -> str:
        return self.groupNumber

    def setGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber

    def setNameAge(self, name, age):
        self.name = name
        self.age = age


def main():
    student_1 = Student("Sanya", 12, "9A")
    student_2 = Student("Petya", 13, "8A")
    student_2.setNameAge("Petr", 8)
    student_3 = Student("Vasya", 9, "7A")
    student_3.setGroupNumber("7B")
    student_4 = Student("Nastya", 13, "8B")
    student_5 = Student("Masha", 17, "9B")

    print(student_5.getAge())
    print(student_5.getName())
    print(student_5.getGroupNumber())


main()