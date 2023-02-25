# this is just us defining a structure
# We haven't done anything with it yet, its just a structure!!!
class Employee:
    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name
    
    def say_name(self):
        print(self.first_name, self.last_name)

# Using it - we call the class name with a list of argument
emp_one = Employee("John", "Doe")
emp_two = Employee("Jane", "Doe")

print(emp_one.first_name, emp_one.last_name)
print(emp_two.first_name, emp_two.last_name)

# if you want to convert to dictionary
print(emp_one.__dict__)






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