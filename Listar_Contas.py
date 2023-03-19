import textwrap

def menu():
    menu = """\n
    ============ MENU ============
    [0]\tSair
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\t Novo usuário
    ==> """
    return input(textwrap.dedent(menu))

def sacar():
    pass

def depositar():
    pass

def exibir_extrato(saldo, /, *, extrato):
    pass
def criar_usuario(usuarios):
    pass
def filtrar_usuario(cpf,usarios):
    pass
def criar_conta(agencia, numero_conta, usuarios):
    pass

def main():
    saldo = 0
    limite = 400
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []
    LIMITE_SAQUES = 4
    AGENCIA = '0001'

    while True:
        opcao = int(input(menu))
        if opcao == 1:
            valor = float(input('Informe o valor do depósito:'))
            saldo, extrato = depositar(saldo, valor, extrato)

            # if valor > 0:
            #     saldo += valor
            #     extrato += f'Depósito: R$ {valor:.2f}\n '
            #
            # else:
            #     print('Operação falhou! o valor informado é inválido.')

        elif opcao == 2:
            valor = float(input('Informe o valor do saque: '))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato= extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques= LIMITE_SAQUES,

            )

            # excedeu_saldo = valor > saldo
            #
            # excedeu_limite = valor > limite
            #
            # excedeu_saques = numero_saques >= LIMITE_SAQUES
            #
            # if excedeu_saldo:
            #     print('Operação falhou! Você não tem saldo suficiente.')
            # elif excedeu_limite:
            #     print('Operação falhou! o valor de saque excede limite')

            # elif excedeu_saques:
            #     print('Operação falhou! Número máximo de saques excedido.')
            #
            # elif valor > 0:
            #     saldo -= valor
            #     extrato += f'Saque: R$ {valor:.2f}\n'
            #     numero_saques += 1
            #
            # else:
            #     print('Operação falhou! o valor informado é inválido.')

        elif opcao == 3:
            print('\n====================Extrato=====================')
            print('Não foram realizadas movimentações.' if not extrato else extrato)
            print(f'\nSaldo: R$ {saldo:.2f}')
            print('=' * 50)

        elif opcao == 0:
            break

        else:
            print('operação inválida, por favor selecione novamente a operação desejada.')
main()