class Person:
    def __init__(self, name, examDay):
        self.name = name
        self.examDay = examDay

    def introduce(self):
        print(f"What's good {self.name}?")
        if self.examDay:  # Check if examDay is True
            print("You're sigma")
        else:
            print("You're still beta")

def greetTheSigma(name):
    return f"What's good {name}"

# Control flow starts here
examDay = True  # Set this to True or False based on your scenario
person = Person("Chad", examDay)

# Introduce the person
person.introduce()

# A math block to simulate an operation
try:
    x = 1 - 0  # This should work fine
except ZeroDivisionError:
    print("Math error fr fr")
