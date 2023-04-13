from FakeDB import FakeDB


fakeDB = FakeDB()
letrasSobrenome = input("Informe as 3 primeiras letras do SOBRENOME para pesquisa: ").lower()
encontrados = []

for funcionario in fakeDB.Funcionarios:
    if letrasSobrenome in funcionario.getSobrenome().lower():
        encontrados.append(funcionario)

print(f'Foram encontrados {len(encontrados)} registros')

for funcionario in encontrados:
    funcionario.toString()