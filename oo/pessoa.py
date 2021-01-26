class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=49):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
     Pedro = Pessoa(nome='Pedro',)
     Silvio = Pessoa(Pedro, nome='Silvio')
     print(Pessoa.cumprimentar(Silvio))
     print(id(Silvio))
     print(Silvio.cumprimentar())
     print(Silvio.nome)
     print(Silvio.idade)
     for filho in Silvio.filhos:
        print(filho.nome)
     Silvio.sobrenome = 'Freitas'
     del Silvio.filhos
     Silvio.olhos = 1
     print(Silvio.__dict__)
     print(Pedro.__dict__)
     Pessoa.olhos = 3
     print(Pessoa.olhos)
     print(Silvio.olhos)
     print(Pedro.olhos)
     print(id(Pessoa.olhos), id(Silvio.olhos), id(Pedro.olhos))









