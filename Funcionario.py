from datetime import date


class Funcionario:

    codigo = 0
    nome = ''
    sobrenome = ''
    dataCadastro = date.today()

    def __init__(self):
        self.codigo = 0
        self.nome = ''
        self.sobrenome = ''
        self.dataCadastro = date.today()

    def getCodigo(self):
        return self.codigo

    def getNome(self):
        return self.nome

    def getSobrenome(self):
        return self.sobrenome

    def getDataCadastro(self):
        return self.dataCadastro

    def toString(self):
        print(f'Codigo = {self.codigo} | ', end='')
        print(f'Nome = {self.nome} | ', end='')
        print(f'Sobrenome = {self.sobrenome} | ', end='')
        print(f'Data de Cadastro = {self.dataCadastro} ')
