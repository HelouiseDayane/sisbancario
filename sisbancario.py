from datetime import datetime

class ContaCorrente:

    def __init__(self, numero_conta, saldo):
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.transacoes = []
        self.saque_diario = 0

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append((datetime.now(), "Deposito", valor))

    def sacar(self, valor):
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")
        if self.saque_diario >= 3:
            raise ValueError("Limite de saques diários atingido")
        if valor > 500:
            raise ValueError("Limite de saque por operação atingido")
        self.saldo -= valor
        self.saque_diario += 1
        self.transacoes.append((datetime.now(), "Saque", valor))

    def extrato(self):
        for data, tipo, valor in self.transacoes:
            print(f"{data}: {tipo}: {valor}")


def main():
    conta = ContaCorrente(123456789, 1000)

    while True:
        opcao = input("Escolha uma opção: \n1 - Sacar \n2 - Depositar \n3 - Extrato \n4 - Sair \n")

        if opcao == "1":
            try:
                valor = float(input("Digite o valor a ser sacado: "))
                conta.sacar(valor)
            except ValueError as e:
                print(e)

        elif opcao == "2":
            valor = float(input("Digite o valor a ser depositado: "))
            conta.depositar(valor)

        elif opcao == "3":
            conta.extrato()

        elif opcao == "4":
            break

        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()
