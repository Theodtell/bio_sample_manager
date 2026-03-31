from time import sleep
samples = []



while True:
    sleep(1)
    print('-'*30)
    print('====MENU====')
    print('Selecione a função desejada:')
    option = int(input('''
    1 - Cadastrar amostras
    2 - Listar amostras 
    3- Sair do programa 
    '''))
    if option not in (1, 2, 3):
        print('ERRO! Opção incorreta!')
        continue

    if option == 1:
        while True:
            name = str(input('Digite o nome da amostra: '))
            if name.strip() != '':
                break
            print('O nome não pode ficar vazio')
        while True:
            sample_type = str(input('Digite o tipo da amostra: '))
            if sample_type.strip() != '':
                break
            print('O tipo de amostra não pode ficar vazio')
        while True:
            date = str(input('Digite a data da coleta: '))
            if date.strip() != '':
                break
            print('A data não pode ficar vazia')
        observations = str(input('Observações da amostra: '))
        sample = [name, sample_type, date, observations]
        samples.append(sample)
        print('Amostra salva com sucesso!')

    elif option == 2:
        for i, sample in enumerate(samples):
            print('-'*30)
            print(f'{i+1}° amostra:')
            print(f'   - Nome: {sample[0]}')
            print(f'   - Tipo: {sample[1]}')
            print(f'   - Data da coleta: {sample[2]}')
            print(f'   - Observações da amostra: {sample[3]}')
        if len(samples) == 0:
            print('Nenhuma amostra cadastrada ainda!')
    elif option == 3:
        break
print('Finalizando programa...')
print('-' * 30)
sleep(1)
print('Programa finalizado com sucesso!')
