# Lab Exercise
# Question_01
class Student1:
    pass


class Marks:
    pass


zahid = Student1()
passed = Marks()
check_student = isinstance(zahid, Student1)
print("Zahid is a instance of class Student--", check_student)
check_marks = isinstance(zahid, Marks)
print("Zahid is a instance of class Marks--", check_marks)
check_student = isinstance(passed, Student1)
print("passed is a instance of class Student--", check_student)
check_marks = isinstance(passed, Marks)
print("passed is a instance of class Marks--", check_marks)
check_student_subclass = isinstance(Student1, object)
print("Student class is a subclass of object--", check_student_subclass)
check_marks_subclass = isinstance(Marks, object)
print("Marks class is a subclass of object--", check_marks_subclass)


# Question_02
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


e1 = Student("Zahid", 60)
print("Previos Value:", e1.name, e1.marks)
e1.name = "Hasan"
e1.marks = 80
print("modified value:", e1.name, e1.marks)


# Question_03
class Student3:
    def __init__(self, ID, Name):
        self.ID = ID
        self.Name = Name


e1 = Student3("201902060", "Zahid")
print(e1.ID, e1.Name)
# adding new attribute to this class
e1.Marks = 82
print("New attribute=> Marks: ", e1.Marks)
# deleting attribute
del e1.Marks
print("Deleted attribute=> Marks: ", e1.Marks)


# Question_04
class Student4:
    def __init__(self, StudentID, StudentName):
        self.StudentID = StudentID
        self.StudentName = StudentName

    def function(self):
        print(f'Student name is {self.StudentName} & ID is {self.StudentID}')


e1 = Student4("201902060", "Zahid")
e1.function()
