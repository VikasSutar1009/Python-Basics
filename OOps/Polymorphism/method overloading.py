class Greet:
    def say_hello(self, name=None):
        if name:
            print(f"Hello, {name}")
        else:
            print("Hello!")
        
g = Greet()
g.say_hello()              #output:Hello!
g.say_hello("Vikas")       #output:Hello, Vikas