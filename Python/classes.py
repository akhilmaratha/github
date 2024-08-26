class Human:
    type_of_animal="Mammal"
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
    def greet(self,name:str):
        return f"Hi i am {self.name},how are you {name}"
john = Human("John",24)
print(f"hi I am, {john.name} i an {john.age} year old, I am a {john.__class__.type_of_animal}") 

