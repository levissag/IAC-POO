from FakeDB import FakeDB


fakeDB = FakeDB()
anoPesquisa = int(input("Informe ano do contrato: "))

print(f'\nFuncionarios que fazem aniversario de contrato - em {anoPesquisa}')
for funcionario in fakeDB.Funcionarios:
    if funcionario.getDataCadastro().year == anoPesquisa:
        print(f'Nome: {funcionario.getNome()} / data: {funcionario.getDataCadastro()}')
