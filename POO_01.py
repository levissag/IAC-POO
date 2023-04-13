from FakeDB import FakeDB


fakeDB = FakeDB()
letrasNome = input("Informe as 3 primeiras letras do NOME para pesquisa: ").lower()

for funcionario in fakeDB.Funcionarios:
    if funcionario.getNome().lower().startswith(letrasNome):
        print(f'{funcionario.getNome()}')
