class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name} Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score

    def display_info(self):
        super().display_info()
        print(f"Grade: {self.score}")

class Animals:
    def __init__(self, name) -> None:
        self.name = name

class Dogs(Animals):
    def bark(self):
        print(f"{self.name} is barking." )

if __name__ == "__main__":
    person1 = Person('Tom', 20)
    person1.display_info()
    student1 = Student('Mike', 18, 60)
    student1.display_info()
    dog1 = Dogs("WangWang")
    dog1.bark()