# Create the Class, who define how the objects enviroment

class People: # OBJETO
    def cumprimentar(self): # PARAMETRO
        return f'\033[30mHello\033[m{id(self)}'

if __name__ == '__main__':
    p = People()
    print(People.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())


