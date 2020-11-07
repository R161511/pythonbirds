# Create the Class, who define how the objects enviroment

class People: # OBJETO
    eyes = 2 # Atribute de classe ou default

    def __init__(self, *sons, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.sons = list(sons)

    def cumprimentar(self): # PARAMETRO
        return f'\033[30mHello\033[m{id(self)}'

if __name__ == '__main__':
    rafael = People(nome='Rafael')
    aline = People(rafael, nome='Aline')
    print(People.cumprimentar(aline))
    print(id(aline))
    print(aline.cumprimentar())
    print(aline.nome)
    print(aline.idade)
    for sons in aline.sons:
        print(sons.nome)
    aline.sobrenome = "Reis"
    del aline.sons
    aline.eyes = 1
    del aline.eyes
    print(aline.__dict__)
    print(rafael.__dict__)
    People.eyes = 3
    print(People.eyes)
    print(aline.eyes)
    print(rafael.eyes)
    print(id(People.eyes), id(aline.eyes), id(rafael.eyes))




