class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = None
        self.set_salary(salary)
    
    def set_salary(self, salary):
        if salary >= 5000:
            self.__salary = salary
        else:
            print("Salary cannot be less than 5000!")

    def get_salary(self):
            return self.__salary

emp1 = Employee("Vikas", 6000)
print(emp1.get_salary())

emp1.set_salary(8000)
print(emp1.get_salary())