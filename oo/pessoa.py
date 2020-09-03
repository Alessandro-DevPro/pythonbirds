class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=46):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola {id(self)}'

    @staticmethod
    def metodo_statico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(renzo, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho'
    del luciano.sobrenome
    luciano.olhos = 1
    print(luciano.__dict__)
    print(renzo.__dict__)
    print(luciano.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos),id(luciano.olhos),id(renzo.olhos))
    print(Pessoa.metodo_statico(), luciano.metodo_statico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
