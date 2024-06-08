# CONCEITOS DE PROGRAMAÇÃO ORIENTADA A OBJETOS:
# Abstração: o que importa dentro de um código é o que ele faz e não como ele faz
# Encapsulamento: organizar o código de maneira inteligente de tal forma que alterações futuras sejam viáveis
# Polimorfismo: quando uma classe possui a capacidade de se adaptar as necessidades de classes distintas
# Herança: quando uma classe filha recebe como herança os métodos e atributos de uma classe pai para usar como se fossem dela


# POLIMORFISMO, HERANÇA, ENCAPSULAMENTO E ABSTRAÇÃO
# Classe pai(polimórfica)
class Animal:
    def __init__(self):
        return None

    def make_sound(self):
        print("--")

# Classe filha da classe Animal e pai da classe Cobra
class WildAnimal(Animal):
    def __init__(self, group, species):
        super().__init__()
        self._group = group
        self._species = species

# Classe filha da classe Animal e pai da classe Cachorro e Gato
class DomesticAnimal(Animal):
    def __init__(self, animal_name, owner_name):
        super().__init__()
        self._animal_name = animal_name
        self._owner_name = owner_name

# Classe filha da classe AnimalSilvestre e "neta" da Classe Animal
class Snake(WildAnimal):
    def __init__(self, group, species):
        super().__init__(group, species)

    def make_sound(self):
        return "Ssssssssssssss!"
    
    def mostra_info(self):
        print(f"GRUPO: {self.group}")
        print(f"ESPÉCIE: {self.species}")

# Classe filha da classe AnimalDomestico e "neta" da Classe Animal
class Dog(DomesticAnimal):
    def __init__(self, name, owner):
        super().__init__(name, owner)

    def make_sound(self):
        return "Au Au!"

    def mostra_info(self):
        print(f"NOME ANIMAL: {self.animal_name}")
        print(f"NOME DONO: {self.owner_nam}")

# Classe filha da classe AnimalDomestico e "neta" da Classe Animal
class Cat(DomesticAnimal):
    def __init__(self, name, owner):
        super().__init__(name, owner)

    def make_sound(self):
        return "Miau!"
    
    def mostra_info(self):
        print(f"NOME ANIMAL: {self.animal_name}")
        print(f"NOME DONO: {self.owner_nam}")

# IMPLEMENTAÇÃO DO MAIN
if __name__ == "__main__":
    animals = [Dog("BOLT", "LUIZ"), Cat("THUNDERCAT", "MÁRIO"), Snake("RÉPTIL", "COBRA")]

    for animal in animals:
        print(animal.make_sound())

# É UM CÓDIGO QUE PODE FACILMENTE SER ALTERADO, FORTALECENDO CORRETAMENTE O CONCEITO DE ENCAPSULAMENTO

# É UM CÓDIGO QUE SE ABSTRAI DAS COMPLEXIDADES E DEMONSTRA O CONCEITO DE ABSTRAÇÃO
