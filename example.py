class Person:

    def __init__ (self, fname, lname):
        self.fname = fname
        self.lname = lname 

    def hello(self):
        print("Hello")

    def report(self):
        print(f"My name is {self.fname} and {self.lname}")

class Agent(Person):

    def reveal(self, passcode):

        if passcode == 123:
            print("I am a secret Agent.")
        else:
            self.report()

x = Person("Hasib", "Hasan")
x.report()