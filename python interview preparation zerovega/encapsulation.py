class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks  # private variable

    def get_marks(self):
        return self.__marks

# Example 1: Basic Encapsulation with Private Variable
class Student:
    def __init__(self, name, marks):
        self.__name = name     # private variable
        self.__marks = marks   # private variable

     # getter method
    def get_marks(self):
            return self.__marks
        
    # setter method
    def set_marks(self, new_marks):
            if new_marks >= 0:
                self.__marks = new_marks
            else:
                print("Marks canot be negative!")

s1 = Student("Vikas", 85)

print(s1.get_marks())         # accessing through getter

s1.set_marks(90)
print(s1.get_marks())         # updated marks

s1.set_marks(-10)             # invalid