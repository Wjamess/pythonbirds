"""
Você deve criar uma classe crrro que vai possuir dois atributos compostos por outras duas classes:

1) Motor
2) Direção

O motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Método acelerar, que deverá incrementar a velocidade de uma unidade
3) Método frear que devera decrementar a velocidade em duas velocidades

A direção terá a responsabilidade decontrolar a direção. Ela oferece os seguintes atributos:
1) Valor de direção com valores possiveis: Norte, Sul, Leste, Oeste.
2) Método girar_direita
3) Método girar_esquerda

    N
O       L
    S

    Exemplo:
    >>>  # Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcão
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
"""
#quando temos constantes, podemos declarar elas em caixa alta
NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

class Direcao:
#PROBLEMA RESULVIDO COM DICIONARIO
    rotacao_a_direita_dct = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
                         }

    rotacao_a_esquerda_dct = {
        NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE
    }
    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]

#PROBLEMA UTILIZANDNO O IF E ELIF
    # def girar_a_direita(self):
    #     if self.valor == NORTE:
    #         self.valor = LESTE
    #     elif self.valor == LESTE:
    #         self.valor = SUL
    #     elif self.valor == SUL:
    #         self.valor = OESTE
    #     elif self.valor == OESTE:
    #         self.valor = NORTE

    # def girar_a_esquerda(self):
    #     if self.valor == NORTE:
    #         self.valor = OESTE
    #     elif self.valor == OESTE:
    #         self.valor = SUL
    #     elif self.valor == SUL:
    #         self.valor = LESTE
    #     elif self.valor == LESTE:
    #         self.valor = NORTE





class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor




