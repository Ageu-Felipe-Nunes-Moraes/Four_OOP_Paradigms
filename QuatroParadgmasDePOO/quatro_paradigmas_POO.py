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

    def fazer_som(self):
        print("--")

# Classe filha da classe Animal e pai da classe Cobra
class AnimalSilvestre(Animal):
    def __init__(self, grupo, especie):
        super().__init__()
        self._grupo = grupo
        self._especie = especie

# Classe filha da classe Animal e pai da classe Cachorro e Gato
class AnimalDomestico(Animal):
    def __init__(self, nome_animal, nome_dono):
        super().__init__()
        self._nome_animal = nome_animal
        self._nome_dono = nome_dono

# Classe filha da classe AnimalSilvestre e "neta" da Classe Animal
class Cobra(AnimalSilvestre):
    def __init__(self, grupo, especie):
        super().__init__(grupo, especie)

    def fazer_som(self):
        return "Ssssssssssssss!"
    
    def mostra_info(self):
        print(f"GRUPO: {self.grupo}")
        print(f"ESPÉCIE: {self.especie}")

# Classe filha da classe AnimalDomestico e "neta" da Classe Animal
class Cachorro(AnimalDomestico):
    def __init__(self, nome, dono):
        super().__init__(nome, dono)

    def fazer_som(self):
        return "Au Au!"

    def mostra_info(self):
        print(f"NOME ANIMAL: {self.nome_animal}")
        print(f"NOME DONO: {self.nome_dono}")

# Classe filha da classe AnimalDomestico e "neta" da Classe Animal
class Gato(AnimalDomestico):
    def __init__(self, nome, dono):
        super().__init__(nome, dono)

    def fazer_som(self):
        return "Miau!"
    
    def mostra_info(self):
        print(f"NOME ANIMAL: {self.nome_animal}")
        print(f"NOME DONO: {self.nome_dono}")

# IMPLEMENTAÇÃO DO MAIN
if __name__ == "__main__":
    animais = [Cachorro("BOLT", "LUIZ"), Gato("THUNDERCAT", "MÁRIO"), Cobra("RÉPTIL", "COBRA")]

    for animal in animais:
        print(animal.fazer_som())

# É UM CÓDIGO QUE PODE FACILMENTE SER ALTERADO, FORTALECENDO CORRETAMENTE O CONCEITO DE ENCAPSULAMENTO

# É UM CÓDIGO QUE SE ABSTRAI DAS COMPLEXIDADES E DEMONSTRA O CONCEITO DE ABSTRAÇÃO
