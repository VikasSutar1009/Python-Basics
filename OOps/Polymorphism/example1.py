class Bird:
    def fly(self):
        print("Some birds can fly")

class Ostrich(Bird):
    def fly(self):
        print("Ostrich can't fly")

def flying_test(bird):
    bird.fly()

flying_test(Bird())
flying_test(Ostrich())