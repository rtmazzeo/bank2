from abc import ABC, abstractmethod
from datetime import date

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta._saldo += self.valor
        conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if conta._saldo >= self.valor:
            conta._saldo -= self.valor
            conta.historico.adicionar_transacao(self)
            return True
        return False

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self, cliente, numero, agencia):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @staticmethod
    def nova_conta(cliente, numero, agencia):
        return Conta(cliente, numero, agencia)

    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            return True
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            return True
        return False

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, agencia, limite, limite_saques):
        super().__init__(cliente, numero, agencia)
        self.limite = limite
        self.limite_saques = limite_saques
        self.saques_realizados = 0

    def sacar(self, valor):
        if self.saques_realizados < self.limite_saques and valor <= (self._saldo + self.limite):
            if super().sacar(valor):
                self.saques_realizados += 1
                return True
        return False

# Exemplo de uso:
def main():
    cliente = PessoaFisica(cpf="12345678900", nome="João da Silva", data_nascimento=date(1985, 5, 15), endereco="Rua A, 123")
    conta = ContaCorrente(cliente, numero=12345, agencia="0001", limite=1000, limite_saques=3)
    cliente.adicionar_conta(conta)
    
    print("Saldo inicial:", conta.saldo)
    cliente.realizar_transacao(conta, Deposito(1000))
    print("Saldo após depósito:", conta.saldo)
    cliente.realizar_transacao(conta, Saque(200))
    print("Saldo após saque:", conta.saldo)
    
    for transacao in conta.historico.transacoes:
        if isinstance(transacao, Deposito):
            print(f"Depósito de R$ {transacao.valor:.2f}")
        elif isinstance(transacao, Saque):
            print(f"Saque de R$ {transacao.valor:.2f}")

if __name__ == "__main__":
    main()
