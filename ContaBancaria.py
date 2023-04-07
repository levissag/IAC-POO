from datetime import date


class ContaBancaria:

    __saldo = 0.0
    __DATA_ABERTURA = date.today()

    def __init__(self):
        self.__saldo = 0.0
        self.__dataAbertura = date.today()

    def depositar(self, saldo):
        self.__saldo = self.__saldo + saldo
        return True

    def sacar(self, saque):
        if saque <= self.__saldo:
            self.__saldo = self.__saldo - saque
            return True
        else:
            return False

    def getSaldo(self):
        return self.__saldo

    def getDataAbertura(self):
        return self.__dataAbertura

    def getDataAberturaFormatada(self):
        dataFormatada = self.__dataAbertura.strftime("%d/%m/%Y")
        return dataFormatada

    def getSaldoFormatado(self):
        saldoFormatado = "R$ {:,.2f}".format(self.__saldo)
        return saldoFormatado
