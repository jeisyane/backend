class Animal:
    def falar(self):
     pass

class Cachorro(Animal):
    def falar(self):
        return "Au au"


class Galinha(Animal):
    def falar(self):
        return "PÓ , PÓ"


class Papagaio(Animal):
    def falar(self):
        return "Curupaco!"

animais = [Cachorro(), Galinha(), Papagaio()]

for animal in animais:
    print(animal.falar())

