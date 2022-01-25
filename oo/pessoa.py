class Pessoa:
    def __init__(self, *filhos, nome=None, idade=None):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    maite = Pessoa(nome='Maite', idade=0)
    denian = Pessoa(maite, noa, nome='Denian', idade=21)
    print(Pessoa.cumprimentar(denian))
    print(id(denian))
    print(denian.cumprimentar())
    print(denian.nome)
    print(denian.idade)
    for filho in denian.filhos:
        print(filho.nome)
