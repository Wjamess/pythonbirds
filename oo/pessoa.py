# Classes devem começar com letra maiusculo ex ExemploPessoa:

class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Olá'

if __name__ == '__main__':
    dirce = Pessoa(nome='Dirce')
    wallace = Pessoa(dirce,nome='Wallace')
    print(Pessoa.cumprimentar(wallace))
    print(id(wallace))
    print(wallace.cumprimentar())
    print(wallace.nome)
    print(wallace.idade)
    for filho in wallace.filhos:
        print(filho.nome)
    wallace.sobrenome = 'Campos'
    del wallace.filhos
    print(wallace.sobrenome)
    print(wallace.__dict__)
    print(dirce.__dict__)
    #Pessoa.olhos = 3
    wallace.olhos = 4
    print(Pessoa.olhos)
    print(wallace.olhos)
    print(dirce.olhos)
    print(id(Pessoa.olhos), id(wallace.olhos), id(dirce.olhos))

