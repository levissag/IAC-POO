import random
from FakeDB import FakeDB


fakeDB = FakeDB()
numSorteio = 5

print(f'\n{numSorteio} Funcionarios aleatorios selecionados')

sorteio = (random.sample(fakeDB.Funcionarios, numSorteio))

for i in sorteio:
    print(f'{i.getNome()}')
