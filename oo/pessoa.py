class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade= 75):
        self.idade = f'{idade} anos'
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {(self)}'


if __name__ == '__main__':
    natan = Pessoa(nome ='Natan', idade = 17)
    maia = Pessoa(natan, nome =  'Maia')
    print(Pessoa.cumprimentar('Natan'))
    print(id(maia))
    print(maia.cumprimentar())
    print(natan.idade)
    for filho in maia.filhos:
        print(filho.nome)
    maia.sobrenome = 'Pereira'
    del maia.filhos
    maia.olhos = 1
    del maia.olhos
    Pessoa.olhos = 3
    print(maia.__dict__)
    print(natan.__dict__)
    print(natan.olhos)
    print(maia.olhos)
    print(Pessoa.olhos)
    print(id(Pessoa.olhos), id(maia.olhos), id(natan.olhos))