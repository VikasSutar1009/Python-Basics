class Calculator:
    def add(self, *args):
        return sum(args)
    
calc = Calculator()
print(calc.add(2,3))
print(calc.add(1,2,3,4,5))