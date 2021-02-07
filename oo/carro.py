"""
Você deve criar uma classe carro que vai prossuir dois atributos compostos por outras duas classes:

1) Motor
2) Direção

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Método acelerar, que deverá incrementar a velocidade de uma unidade
3) Método frear que deverá decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de controlar o sentido de direção. Ela oferece os seguintes atributos:
1) Valore de direção com valores possiveis: Norte, Sul, Leste, Oeste
2) Método girar_a_direita
2) Método girar_a_esquerda

  N
O   L
  S

    Exemplo:
    >>> motor = Motor() # ponto 1
    >>> motor.velocidade # ponto 2
    0
    >>> motor.acelerar() # ponto 3
    >>> motor.velocidade # ponto 4
    1
    >>> motor.acelerar() # ponto 5
    >>> motor.velocidade # ponto 6
    2
    >>> motor.acelerar() # ponto 7
    >>> motor.velocidade # ponto 8
    3
    >>> motor.frear() # ponto 9
    >>> motor.velocidade # ponto 10
    1
    >>> motor.frear() # ponto 11
    >>> motor.velocidade # ponto 12
    0
    >>> # Testando Direcao # ponto 13
    >>> direcao = Direcao() # ponto 14
    >>> direcao.valor # ponto 15
    'Norte'
    >>> direcao.gira_direita # ponto 15b
    {'Norte': 'Nordeste', 'Nordeste': 'Leste', 'Leste': 'Sudeste', 'Sudeste': 'Sul', 'Sul': 'Sudoeste', 'Sudoeste': 'Oeste', 'Oeste': 'Noroeste', 'Noroeste': 'Norte'}
    >>> direcao.gira_esquerda # ponto 15c
    {'Nordeste': 'Norte', 'Leste': 'Nordeste', 'Sudeste': 'Leste', 'Sul': 'Sudeste', 'Sudoeste': 'Sul', 'Oeste': 'Sudoeste', 'Noroeste': 'Oeste', 'Norte': 'Noroeste'}
    >>> direcao.girar_a_direita() # ponto 16
    >>> direcao.valor # ponto 17
    'Nordeste'
    >>> direcao.girar_a_direita() # ponto 16b
    >>> direcao.valor # ponto 17b
    'Leste'
    >>> direcao.girar_a_direita() # ponto 18
    >>> direcao.valor # ponto 19
    'Sudeste'
    >>> direcao.girar_a_direita() # ponto 18b
    >>> direcao.valor # ponto 19b
    'Sul'
    >>> direcao.girar_a_direita() # ponto 20
    >>> direcao.valor # ponto 21
    'Sudoeste'
    >>> direcao.girar_a_direita() # ponto 20b
    >>> direcao.valor # ponto 21b
    'Oeste'
    >>> direcao.girar_a_direita() # ponto 22
    >>> direcao.valor # ponto 23
    'Noroeste'
    >>> direcao.girar_a_direita() # ponto 22b
    >>> direcao.valor # ponto 23b
    'Norte'
    >>> direcao.girar_a_esquerda() # ponto 24
    >>> direcao.valor # ponto 25
    'Noroeste'
    >>> direcao.girar_a_esquerda() # ponto 24b
    >>> direcao.valor # ponto 25b
    'Oeste'
    >>> direcao.girar_a_esquerda() # ponto 25
    >>> direcao.valor # ponto 26
    'Sudoeste'
    >>> direcao.girar_a_esquerda() # ponto 25b
    >>> direcao.valor # ponto 26b
    'Sul'
    >>> direcao.girar_a_esquerda() # ponto 27
    >>> direcao.valor # ponto 28
    'Sudeste'
    >>> direcao.girar_a_esquerda() # ponto 27b
    >>> direcao.valor # ponto 28b
    'Leste'
    >>> direcao.girar_a_esquerda() # ponto 29
    >>> direcao.valor # ponto 30
    'Nordeste'
    >>> direcao.girar_a_esquerda() # ponto 29b
    >>> direcao.valor # ponto 30b
    'Norte'
    >>> carro = Carro(direcao, motor) # ponto 31
    >>> carro.calcular_velocidade() # ponto 32
    0
    >>> carro.acelerar() # ponto 33
    >>> carro.calcular_velocidade() # ponto 34
    1
    >>> carro.acelerar() # ponto 35
    >>> carro.calcular_velocidade() # ponto 36
    2
    >>> carro.frear() # ponto 37
    >>> carro.calcular_velocidade() # ponto 38
    0
    >>> carro.calcular_direcao() # ponto 39
    'Norte'
    >>> carro.girar_a_direita() # ponto 40
    >>> carro.calcular_direcao() # ponto 41
    'Nordeste'
    >>> carro.girar_a_esquerda() # ponto 42
    >>> carro.calcular_direcao() # ponto 43
    'Norte'
    >>> carro.girar_a_esquerda() # ponto 44
    >>> carro.calcular_direcao() # ponto 45
    'Noroeste'
"""
class Motor:
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        if self.velocidade < 0:
            self.velocidade = 0

    def velocidade(self):
        return self.velocidade

class Direcao:
    #gira_direita = {'Norte':'Leste','Leste':'Sul','Sul':'Oeste','Oeste':'Norte'}
    #gira_esquerda = {'Norte': 'Oeste', 'Oeste': 'Sul', 'Sul': 'Leste', 'Leste': 'Norte'}

    def __init__(self, valor='Norte'):
        self.valor = valor
        self.direcoes = ['Norte', 'Nordeste','Leste', 'Sudeste', 'Sul', 'Sudoeste', 'Oeste', 'Noroeste']

        self.gira_direita = {}
        self.gira_esquerda = {}
        primeira = ''
        anterior = ''
        for sentido in self.direcoes:
            if primeira == '':
                primeira = sentido
            else:
                self.gira_direita[anterior] = sentido
                self.gira_esquerda[sentido] = anterior

            anterior = sentido
        if primeira != '':
            self.gira_direita[anterior] = primeira
            self.gira_esquerda[primeira] = anterior

    def girar_a_direita(self):
        self.valor = self.gira_direita[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.gira_esquerda[self.valor]

    def valor(self ):
        return self.valor


class Carro:
    def __init__(self, direcao=Direcao(), motor=Motor()):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        return self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda()

if __name__ == '__main__':
    motor = Motor()
    print('Velocidade', motor.velocidade)

    motor.acelerar()
    print('Velocidade', motor.velocidade)

    motor.acelerar()
    print('Velocidade', motor.velocidade)

    motor.acelerar()
    print('Velocidade', motor.velocidade)

    motor.frear()
    print('Velocidade', motor.velocidade)

    motor.frear()
    print('Velocidade', motor.velocidade)

    # Testando Direcao
    direcao = Direcao()
    print('direcao', direcao.valor)

    direcao.girar_a_direita()
    print('direcao', direcao.valor)

    direcao.girar_a_direita()
    print('direcao', direcao.valor)

    direcao.girar_a_direita()
    print('direcao', direcao.valor)

    direcao.girar_a_direita()
    print('direcao', direcao.valor)

    direcao.girar_a_esquerda()
    print('direcao', direcao.valor)

    direcao.girar_a_esquerda()
    print('direcao', direcao.valor)

    direcao.girar_a_esquerda()
    print('direcao', direcao.valor)

    direcao.girar_a_esquerda()
    print('direcao', direcao.valor)

    carro = Carro(direcao, motor)
    print('velocidade carro', carro.calcular_velocidade())

    carro.acelerar()
    print('velocidade carro', carro.calcular_velocidade())

    carro.acelerar()
    print('velocidade carro', carro.calcular_velocidade())

    carro.frear()
    print('velocidade carro', carro.calcular_velocidade())

    print('direcao carro',carro.calcular_direcao())

    carro.girar_a_direita()
    print('direcao carro',carro.calcular_direcao())

    carro.girar_a_esquerda()
    print('direcao carro',carro.calcular_direcao())

    carro.girar_a_esquerda()
    print('direcao carro',carro.calcular_direcao())


