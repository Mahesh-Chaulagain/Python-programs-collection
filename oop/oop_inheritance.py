class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f"i am {self.name} and i am {self.age} years old")

    def speak(self):
        print("i dont know what i say")

class Cat(Pet):   #inherit pet class
    def __init__(self,name,age,color):
        super().__init__(name,age) #super means reference for super class 
        self.color = color

    def speak(self): #override pet method
        print("meow")

    def show(self):
        print(f"i am {self.name} and i am {self.age} years old and i am {self.color}")

class Dog(Pet):   #inherit pet class      
    def speak(self): #override pet method
        print("bark")

class Fish(Pet):
    pass

p = Pet("ram",19)
p.speak()
c = Cat("bill",34,"red")
c.show()
d= Dog("jill",20)
d.speak()
f = Fish("goldfish",45)
f.speak()