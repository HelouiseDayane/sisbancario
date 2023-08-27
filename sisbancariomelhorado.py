from datetime import datetime

class Cliente:

    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome
        self.conta_corrente = None


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
    clientes = []

    while True:
        opcao = input("Escolha uma opção: \n1 - Criar cliente \n2 - Sacar \n3 - Depositar \n4 - Extrato \n5 - Sair \n")

        if opcao == "1":
            cpf = input("Digite o CPF do cliente: ")
            nome = input("Digite o nome do cliente: ")

            # Verifica se o cliente já existe
            for cliente in clientes:
                if cliente.cpf == cpf:
                    print("Cliente já existe")
                    break

            # Cria um novo cliente
            cliente = Cliente(cpf, nome)
            clientes.append(cliente)

        elif opcao == "2":
            # Solicita o CPF do cliente
            cpf = input("Digite o CPF do cliente: ")

            # Verifica se o cliente existe
            for cliente in clientes:
                if cliente.cpf == cpf:
                    conta = cliente.conta_corrente
                    break

            # Se o cliente não existir, solicita a criação da conta corrente
            if conta is None:
                print("Cliente não tem conta corrente")
                break

            try:
                valor = float(input("Digite o valor a ser sacado: "))
                conta.sacar(valor)
            except ValueError as e:
                print(e)

        elif opcao == "3":
            # Solicita o CPF do cliente
            cpf = input("Digite o CPF do cliente: ")

            # Verifica se o cliente existe
            for cliente in clientes:
                if cliente.cpf == cpf:
                    conta = cliente.conta_corrente
                    break

            # Se o cliente não existir, solicita a criação da conta corrente
            if conta is None:
                print("Cliente não tem conta corrente")
                break

            valor = float(input("Digite o valor a ser depositado: "))
            conta.depositar(valor)

        elif opcao == "4":
            # Solicita o CPF do cliente
            cpf = input("Digite o CPF do cliente: ")

            # Verifica se o cliente existe
            for cliente in clientes:
                if cliente.cpf == cpf:
                    conta = cliente.conta_corrente
                    break

            # Se o cliente não existir, solicita a criação da conta corrente
            if conta is None:
                print("Cliente não tem conta corrente")
                break

            conta.extrato()

        elif opcao == "5":
            break

        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()
