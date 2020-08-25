class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = f'{idade} anos'
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {(self)}'


if __name__ == '__main__':
    natan = Pessoa(nome ='Natan')
    maia = Pessoa(natan, nome =  'Maia')
    print(Pessoa.cumprimentar('Natan'))
    print(id(maia))
    print(maia.cumprimentar())
    print(natan.idade)
    for filho in maia.filhos:
        print(filho.nome)
