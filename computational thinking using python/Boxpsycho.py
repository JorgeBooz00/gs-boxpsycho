import time
#uso dao módulo time para registrar a data e horario do remedio tomado

medicamentos = []
quantidades = []
horarios = []
registros = [[] for _ in medicamentos]
def cadastroMedicamento():
    '''
    os parametros medicamento, quantidade e horario são definidos dentro da função e adicionam valores as listas
    :return: printa os medicamentos registrados
    '''
    qtdRemedios = int(input("Quantos medicamentos deseja cadastrar?\n"))
    if qtdRemedios > 0:
        i = 0
        while i < qtdRemedios:
            medicamento = input("\nDigite o nome do medicamento: ")
            quantidade = input("Digite a quantidade de comprimidos: ")
            print("\033[95mExemplo de horário para às 10 da manhã e noite: 10 e 22\033[0m")
            horario = input("Digite o(s) horário(s) que o(s) medicamento(s) deve(m) ser tomado(s): ")
            if medicamento == "" or quantidade == "" or horario == "":
                print("\nAlgum requisito não foi preenchido, por favor insira novamente\n")
            else:
                if medicamento.upper() not in medicamentos:
                    medicamentos.append(medicamento.upper())
                    quantidades.append(quantidade)
                    horarios.append(horario)
                    i += 1
                else:
                    print("\nMEDICAMENTO JÁ CADASTRADO, INSIRA NOVAMENTE")

        print("\nMedicamentos cadastrados com sucesso!")
        print("Lista de medicamentos:")
        for j in range(len(medicamentos)):
            print(f'''
    Nome: {medicamentos[j]} 
    Quantidade: {quantidades[j]} 
    Horário(s): {horarios[j]}h''')
    else:
        print("Nenhum medicamento cadastrado")

def registroUso():
    '''
    essa função registra o horario a data e o horario que o usuario fez o uso de medicamento com o método strftime do módulo time
    :return:
    '''

    if not medicamentos:
        print("Nenhum medicamento registrado.")
        return

    for i in range(len(medicamentos)):
        print(f'{i + 1}.{medicamentos[i]}')

    usado = int(input("Pelo número, qual medicamento foi usado? "))

    if 1 <= usado <= len(medicamentos):
        while len(registros) < len(medicamentos):
            registros.append([])

        if len(registros[usado - 1]) == 0:
            registros[usado - 1].append([])

        registro = time.strftime("%d-%m-%Y %H:%M")
        registros[usado - 1][0].append(registro)
        print(f'{medicamentos[usado - 1]} tomado às {registro}')
    else:
        print("Número de medicamento inválido.")

def editarRemedio():
    '''
    Essa função permite editar o nome, quantidade indicada e horários de administração de um medicamento.
    '''
    # essa parte da função garante que possuem medicamentos cadastrados, esta presente em todas as funções
    if not medicamentos:
        print("Nenhum medicamento registrado.")
        return

    for i in range(len(medicamentos)):
        print(f'{i + 1}.{medicamentos[i]}')

    editar = int(input("Pelo número, qual medicamento deseja editar? ")) - 1

    if 0 <= editar < len(medicamentos):
        novoNome = input("Digite o novo nome do medicamento: ")
        novaQuantidade = input("Digite a nova quantidade do medicamento: ")
        novosHorarios = input("Digite os novos horários do medicamento: ")

        medicamentos[editar] = novoNome.upper()
        quantidades[editar] = novaQuantidade
        horarios[editar] = novosHorarios

        print(f'Medicamento editado com sucesso!\n'
              f'Novos dados:\n'
              f'Nome: {medicamentos[editar]}\n'
              f'Quantidade: {quantidades[editar]}\n'
              f'Horários: {horarios[editar]}')
    else:
        print("Número de medicamento inválido.")

def removerMedicamento():
    '''
    Essa função permite remover um medicamento da lista.
    '''
    # Essa parte da função garante que existem medicamentos, está presente em todas as funções
    if not medicamentos:
        print("Nenhum medicamento registrado.")
        return

    for i in range(len(medicamentos)):
        print(f'{i + 1}.{medicamentos[i]}')

    remover = int(input("Pelo número, qual medicamento deseja remover? ")) - 1

    if 0 <= remover < len(medicamentos):
        medicamento_removido = medicamentos.pop(remover)
        quantidade_removida = quantidades.pop(remover)
        horario_removido = horarios.pop(remover)

        # Garanta que a lista de registros seja atualizada corretamente
        if registros:
            registros.pop(remover)
        else:
            print("A lista de registros já está vazia.")

        print(f'Medicamento removido com sucesso!\n'
              f'Dados removidos:\n'
              f'Nome: {medicamento_removido}\n'
              f'Quantidade: {quantidade_removida}\n'
              f'Horários: {horario_removido}')
    else:
        print("Número de medicamento inválido.")

def relatorioDeUso():
    '''
    Essa função exibe um relatório de uso para cada medicamento.
    '''
    # Essa parte da função garante que existem registros de uso.
    if not registros:
        print("Nenhum uso registrado.")
        return

    for i in range(len(medicamentos)):
        print(f'\nRelatório de Uso para {medicamentos[i]}:')
        if registros[i]:
            for j, registro in enumerate(registros[i][0], start=1):
                print(f'{j}.{registro}')
        else:
            print("Nenhum registro de uso para este medicamento.")

def medicamentosDisponiveis():
    '''
    Esta função exibe informações sobre os medicamentos disponíveis, incluindo nome, quantidade e horários.
    '''
    # Essa parte da função garante que existem medicamentos cadastrados, está presente em todas as funções
    if not medicamentos:
        print("Nenhum medicamento registrado.")
        return
    #

    for i in range(len(medicamentos)):
        print(f'\nInformações sobre {medicamentos[i]}:')
        print(f'Nome: {medicamentos[i]}')
        print(f'Quantidade: {quantidades[i]}')
        print(f'Horário(s): {horarios[i]}h')

while True:
    print(f'''
1. Médico
2. Paciente
0.sair
''')
    usuario = int(input("Escolha a opção: "))
    match usuario:
    #esse match case entra no layout do usuario ou do medico
        case 1:
            login = str(input("digite o login: "))
            senha = str(input("digite a senha: "))
            while True:
                print(f'''
                                    \033[94mBox\033[0mps\033[95my\033[0mcho
                             olá {login}, como podemos te ajudar?
        
                             1. Cadastrar medicamento
                             2. Editar medicamento
                             3. Remover medicamento
                             4. Relatório de uso
                             0. Sair
                        ''')

                opcao = int(input("Escolha: "))

                match opcao:
                #esse match case executa a função feita pelo usuário
                    case 1:
                        cadastroMedicamento()
                    case 2:
                        editarRemedio()
                    case 3:
                        removerMedicamento()
                    case 4:
                        relatorioDeUso()
                    case _:
                        print("até mais")
                        break
        case 2:
            login = str(input("digite o login: "))
            senha = str(input("digite a senha: "))
            while True:
                print(f'''
                                         \033[94mBox\033[0mps\033[95my\033[0mcho
                             olá {login}, como podemos te ajudar?
        
                             1. Medicamentos para uso
                             2. Registrar uso
                             0. Sair
        
                        ''')

                opcao = int(input("Escolha: "))

                match opcao:
                    case 1:
                        medicamentosDisponiveis()
                    case 2:
                        registroUso()
                    case _:
                        print("até mais")
                        break
        case _:
            print("Até Mais")
            break