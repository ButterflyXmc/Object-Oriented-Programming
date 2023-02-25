# To inherit an exception
class ValueTooSmall(Exception):
    def __init__(self):
        super().__init__("The value is too small")


# Exception can be given any argument, any msg
# exep1 = Exception("You hit a exception")

# this will be empty as there is no args rn
exep1 = Exception()

# this will print the exception from the __init__
exep2 = ValueTooSmall()

print(exep1)
print(exep2)

# value = int(input("Enter a number: "))
# if (value < 10):
#     raise ValueTooSmall()

#&............. Inheritance example.............
class Person:
    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name
# This function prints first and last name
    def say_name(self):
        print(self.first_name, self.last_name)


class Student(Person):
    def __init__(self, f_name, l_name, major):
        super().__init__(f_name, l_name)
        self.gpa = 2.5
        self.major = major

class EngineeringStudent(Student):
    def __init__(self, f_name, l_name, major):
        super().__init__(f_name, l_name, "Engineering")


class PsychStudents(Student):
    def __init__(self, f_name, l_name, major):
        super().__init__(f_name, l_name, "Psychology")


class Employee(Person):
    def __init__(self, f_name, l_name, pay=15):
        super().__init__(f_name, l_name)
        self.pay = pay
        self.location = None
    def pay_rise(self, amount):
        self.pay = self.pay + amount


emp_one = Employee("John", "Doe")
emp_two = Employee("Jane", "Doe")
emp_three = Employee("Eric", "Doe", 20)


emp_one.say_name()
emp_two.say_name()

print(emp_one.pay)
print(emp_three.pay)


#!...............NOTES...............
# Super - says go to my parent class and try to do something with the parent class def