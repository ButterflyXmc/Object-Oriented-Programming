# this is just us defining a structure
# 1. We haven't done anything with it yet, its just a structure!!!
# Rule -  needs to have self as the first argument
class Employee:
    def __init__(self, f_name, l_name, pay=15):
        self.first_name = f_name
        self.last_name = l_name
        self.pay = pay
        self.location = None
    
    def say_name(self):
        print(self.first_name, self.last_name)

    # def pay_rise(self, amount):
    #     self.pay = 
    
    

# 2. Using it - we call the class name with a list of argument
emp_one = Employee("John", "Doe")
emp_two = Employee("Jane", "Doe")
emp_three = Employee("Eric", "Doe", 20)

#! no need for this anymore
# print(emp_one.first_name, emp_one.last_name)
# print(emp_two.first_name, emp_two.last_name)

# 3.can use this to print
emp_one.say_name()
emp_two.say_name()
print(emp_three.pay)

# if you want to convert to dictionary
# print(emp_one.__dict__)






# !......................................NOTES..............................................
# this is just us defining a structure
# We havent done anything with it yet, its just a structure!!!
# .... kind of like a prop function in vue...

#* class - the key word
#* code needed for an employee in our system
#* rn we created an empty table
#class Employee:
#   pass
# * defining an init function that takes any argument
# every class fucntion needs to have self. Python will take care of the self. Anything beyond self, we have to take care.
#  def __init__(self)
# * pass objects (f_name,l_name)

#* using the class
# - we call the class name with a list of argument

# # now each emplyee I create, they'll always defalut to 15 
        #* self.pay = 15
# If i want to overwrite it, i need to define it in the bracket
#*def __init__(self, f_name, l_name, pay=15):
