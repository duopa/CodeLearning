class Student:
    pass

class MyStudent(Student):
    pass

stu = Student()

print(type(stu))
print(type(Student))

print(MyStudent.__bases__)
print(Student.__bases__)
print(type.__bases__)

print(type(object))