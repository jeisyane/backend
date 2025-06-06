class Animal:
    def falar(self):
        pass  # Método genérico, sobrescrito pelas subclasses


class Cachorro(Animal):
    def falar(self):
        return "Au au"


class Gato(Animal):
    def falar(self):
        return "Miau"


def fazer_animal_falar(animal):
    print(animal.falar())  # Aqui entra o polimorfismo

