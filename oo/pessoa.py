class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=None):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    maite = Pessoa(nome='Maite', idade=0)
    denian = Pessoa(maite, nome='Denian', idade=21)
    print(Pessoa.cumprimentar(denian))
    print(id(denian))
    print(denian.cumprimentar())
    print(denian.nome)
    print(denian.idade)
    for filho in denian.filhos:
        print(filho.nome)
    denian.sobrenome = 'Machado'
    print(denian.__dict__)
    del denian.sobrenome
    print(denian.__dict__)
    print(maite.__dict__)
    print(Pessoa.olhos)
    print(denian.olhos)
    print(maite.olhos)
    denian.olhos = 1
    print()
    print(denian.olhos)
    print(denian.__dict__)
    print(Pessoa.olhos)
    print(maite.olhos)
    Pessoa.olhos = 3
    print()
    print(Pessoa.olhos)
    print(denian.__dict__)
    print(denian.olhos)
    print(maite.olhos)
    print()
    del denian.olhos
    print(Pessoa.olhos)
    print(denian.__dict__)
    print(denian.olhos)
    print(maite.olhos)

