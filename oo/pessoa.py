class Pessoa:
    def __init__(self, nome = None):
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
    # print(Pessoa.cumprimentar(p))
    # print(id(p))
    # print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Natan'
    print(p.nome)