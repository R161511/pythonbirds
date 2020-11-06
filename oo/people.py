# Create the Class, who define how the objects enviroment

class People: # OBJETO
    def __init__(self, nome=None, idade=35):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self): # PARAMETRO
        return f'\033[30mHello\033[m{id(self)}'

if __name__ == '__main__':
    p = People('Aline')
    print(People.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = "\033[33mRafael\033[m"
    print(p.nome)
    print(p.idade)


