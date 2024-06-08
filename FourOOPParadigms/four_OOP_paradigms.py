# OBJECT-ORIENTED PROGRAMMING CONCEPTS:
# Abstraction: what matters within a code is what it does, not how it does it
# Encapsulation: organizing the code intelligently so that future changes are feasible
# Polymorphism: when a class has the ability to adapt to the needs of different classes
# Inheritance: when a child class inherits methods and attributes from a parent class to use as if they were its own



# POLYMORPHISM, INHERITANCE, ENCAPSULATION, AND ABSTRACTION
# Parent class (polymorphic)
class Animal:
    def __init__(self):
        return None

    def make_sound(self):
        print("--")

# Child class of the Animal class and parent class of the Snake class
class WildAnimal(Animal):
    def __init__(self, group, species):
        super().__init__()
        self._group = group
        self._species = species

# Child class of the Animal class and parent class of the Dog and Cat classes
class DomesticAnimal(Animal):
    def __init__(self, animal_name, owner_name):
        super().__init__()
        self._animal_name = animal_name
        self._owner_name = owner_name

# Child class of the WildAnimal class and "grandchild" of the Animal class
class Snake(WildAnimal):
    def __init__(self, group, species):
        super().__init__(group, species)

    def make_sound(self):
        return "Ssssssssssssss!"
    
    def mostra_info(self):
        print(f"GRUPO: {self.group}")
        print(f"ESPÉCIE: {self.species}")

# Child class of the DomesticAnimal class and "grandchild" of the Animal class
class Dog(DomesticAnimal):
    def __init__(self, name, owner):
        super().__init__(name, owner)

    def make_sound(self):
        return "Au Au!"

    def mostra_info(self):
        print(f"NOME ANIMAL: {self.animal_name}")
        print(f"NOME DONO: {self.owner_nam}")

# Child class of the DomesticAnimal class and "grandchild" of the Animal class
class Cat(DomesticAnimal):
    def __init__(self, name, owner):
        super().__init__(name, owner)

    def make_sound(self):
        return "Miau!"
    
    def mostra_info(self):
        print(f"NOME ANIMAL: {self.animal_name}")
        print(f"NOME DONO: {self.owner_nam}")

# MAIN IMPLEMENTATION

if __name__ == "__main__":
    animals = [Dog("BOLT", "LUIZ"), Cat("THUNDERCAT", "MÁRIO"), Snake("RÉPTIL", "COBRA")]

    for animal in animals:
        print(animal.make_sound())

# IT IS A CODE THAT CAN EASILY BE CHANGED, CORRECTLY STRENGTHENING THE CONCEPT OF ENCAPSULATION

# IT IS A CODE THAT ABSTRACTS AWAY THE COMPLEXITIES AND DEMONSTRATES THE CONCEPT OF ABSTRACTION
