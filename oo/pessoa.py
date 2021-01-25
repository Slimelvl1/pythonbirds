class Pessoa:
    def __init__(self, *filhos, nome=None, idade=20):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
     Pedro = Pessoa(nome='Pedro')
     Silvio = Pessoa(Pedro, nome='Silvio')
     print(Pessoa.cumprimentar(Silvio))
     print(id(Silvio))
     print(Silvio.cumprimentar())
     print(Silvio.nome)
     print(Silvio.idade)
     for filho in Silvio.filhos:
        print(Silvio.nome)







