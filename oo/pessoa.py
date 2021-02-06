class Pessoa:
    def __init__(self, *filhos, nome=None, idade=18):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    joao = Pessoa(nome='Joao')
    eliane = Pessoa(joao,nome='Eliane')
    print(Pessoa.cumprimentar(eliane))
    print(id(eliane))
    print(eliane.cumprimentar())
    print(eliane.nome)
    print(eliane.idade)
    for filho in eliane.filhos:
        print(filho.nome)
