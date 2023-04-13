import csv
from datetime import datetime
from Funcionario import Funcionario


class FakeDB:

    Funcionarios = []

    def autoFillFuncionarios(self):
        with open('funcionarios.txt') as csvfile:
            linereader = csv.reader(csvfile, delimiter=';')
            for row in linereader:
                obj = Funcionario()
                obj.codigo = int(row[0])
                obj.nome = row[1]
                obj.sobrenome = row[2]
                obj.dataCadastro = datetime.strptime(row[3], '%d/%m/%Y').date()
                self.Funcionarios.append(obj)

    def __init__(self):
        self.autoFillFuncionarios()
