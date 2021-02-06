from builtins import print


class Pessoa:
    def __init__(self, nome=None, idade=18, *filhos, ):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    joao = Pessoa('Joao',13)
    eliane = Pessoa('Eliane',44, joao)
    michel = Pessoa('Michel',25)
    dayane = Pessoa('Dayane',22)
    sidnei = Pessoa('Sidnei',50, michel,dayane)
    print(Pessoa.cumprimentar(eliane))
    print(id(eliane))
    print(eliane.cumprimentar())
    print(eliane.nome,eliane.idade)
    for filho in eliane.filhos:
        print('filho',filho.nome, filho.idade   )
    print(sidnei.nome, sidnei.idade)
    for filho in sidnei.filhos:
        print('filho',filho.nome, filho.idade)

    sidnei.sobrenome = 'Francisco' #atribuição dinamica, autilizar apenas em casos esporádicos
    print(sidnei.__dict__)
    print(eliane.__dict__)

    del sidnei.idade #não é uma boa pratica deletar atributos no código
    print(sidnei.__dict__)
    print(eliane.__dict__)



