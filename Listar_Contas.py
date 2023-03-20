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
    [6]\tNovo usuário
    ==> """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print("\n == Depósito realizado com sucesso! ===")
    else:
        print("\n Operação falhou! o valor informado não é válido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print('Operação falhou! Você não tem saldo suficiente.')
    elif excedeu_limite:
        print('Operação falhou! o valor de saque excede limite')

    elif excedeu_saques:
        print('Operação falhou! Número máximo de saques excedido.')

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        numero_saques += 1

    else:
        print('Operação falhou! o valor informado é inválido.')

    return  saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print('\n====================Extrato=====================')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo: R$ {saldo:.2f}')
    print('=' * 50)
def criar_usuario(usuarios):
    cpf = input('informe o cpf (somente números: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Já existe usuário com esse CPF! ')
        return
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ')
    usuarios.append({'nome': nome, 'data_cascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    print('=== Usuário criado com sucesso ===')

def filtrar_usuario(cpf,usarios):
    usuarios_filtrados = [usuario for usuario in usarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else  None
    pass
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o cpf do usuário: ')
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print('\n=== Conta criada com Sucesso! ===')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    print('\n Usuário não encontrado, fluxo de criação de conta encerrado! ')

def listar_contas():
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


        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)
        #

        elif opcao == 4:
            numero_conta = len(contas) +1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                conta.append(conta)


        elif opcao == 5:
            listar_contas(contas)



        elif opcao == 6:
            criar_usuario(usuarios)

        elif opcao == 0:
            break

        else:
            print('operação inválida, por favor selecione novamente a operação desejada.')
main()