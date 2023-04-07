from ContaBancaria import ContaBancaria

conta = ContaBancaria()
print(f'Data abertura: {conta.getDataAbertura()}')
print(f'Data abertura formatada: {conta.getDataAberturaFormatada()}')
print(f'Saldo: {conta.getSaldo()}')
print(f'Saldo formatado: {conta.getSaldoFormatado()}')
print(f'Deposito de R$ 1.500,50: {conta.depositar(1500.50)}')
print(f'Saldo formatado: {conta.getSaldoFormatado()}')
print(f'Saque de R$ 100,50: {conta.sacar(100.50)}')
print(f'Saldo formatado: {conta.getSaldoFormatado()}')
print(f'Tentativa saque R$ 1.401,00: {conta.sacar(1401)}')
print(f'Saldo formatado: {conta.getSaldoFormatado()}')