# Create the Class, who define how the objects enviroment

class People: # OBJETO
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



