from FakeDB import FakeDB


fakeDB = FakeDB()
mesPesquisa = int(input("Informe mês do contrato: "))

for funcionario in fakeDB.Funcionarios:
    if funcionario.getDataCadastro().month == mesPesquisa:
        print(f'{funcionario.getNome()} | {funcionario.getDataCadastro()}')
