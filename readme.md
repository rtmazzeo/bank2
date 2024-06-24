### Sistema Bancário em Python utilizando POO - :brazil:
Este repositório contém a solução desenvolvida para o Desafio Sistema Bancário em Python utilizando Programação Orientada a Objetos (POO). O projeto consiste na criação de um sistema bancário utilizando POO para gerenciar contas, clientes, transações e históricos.

## Descrição do Projeto
O projeto implementa as seguintes funcionalidades:

<strong>Depósito:</strong> Permite depositar valores positivos na conta bancária. Agora, com a utilização de POO, os depósitos são registrados como transações em objetos específicos de cada conta. Cada depósito é armazenado no histórico da conta e pode ser visualizado na operação de extrato.

<strong>Saque:</strong> O sistema permite realizar saques com as seguintes restrições:

- Limite diário de 3 saques.
- Limite máximo de R$ 500,00 por saque.
- Verificação de saldo suficiente para realizar o saque.

Os saques são registrados como transações e armazenados no histórico da conta. Caso o usuário não tenha saldo suficiente ou tenha atingido o limite de saques diários, uma mensagem apropriada é exibida.

<strong>Extrato:</strong> Lista todos os depósitos e saques realizados na conta, mostrando o saldo atual ao final. Se não houver movimentações, é exibida a mensagem "Não foram realizadas movimentações". Os valores são formatados no padrão R$ XXXX.XX.

## Código Desenvolvido
O código está estruturado em classes que representam os principais componentes do sistema bancário:

## Classes Principais
<strong>Cliente:</strong> Representa um cliente do banco, podendo possuir múltiplas contas.

<strong>PessoaFisica:</strong> Subclasse de Cliente, inclui atributos como CPF, nome e data de nascimento.

<strong>Conta:</strong> Classe base para contas bancárias, com métodos para depósito e saque.

<strong>ContaCorrente:</strong> Subclasse de Conta, adiciona limite de crédito e controle de saques diários.

<strong>Historico:</strong> Armazena o histórico de transações de uma conta.

<strong>Transacao:</strong> Classe abstrata para representar transações bancárias.

<strong>Deposito:</strong> Subclasse de Transacao, representa um depósito.

<strong>Saque:</strong> Subclasse de Transacao, representa um saque.
