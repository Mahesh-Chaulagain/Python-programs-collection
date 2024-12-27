class Person:
    number_of_people = 0 #class attribute ,defined for the entire class,will not change with objects

    def __init__(self,name):
        self.name = name
        Person.add_person()

    @classmethod #decorator to deonote this specific method is a class method
    def number_of_people_(cls): #class method which is not specific to instance,meant to be called on the class itself 
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people +=1

p1 = Person("tim")
p2 = Person("jill")

print(Person.number_of_people_())
# Person.number_of_people = 6 #update th clas attribute
