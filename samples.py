from time import sleep

def register_sample(samples):
    from datetime import datetime
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
        date_str = str(input('Digite a data da coleta (dd/mm/aaaa): '))
        try:
            date = datetime.strptime(date_str, '%d/%m/%Y').date()
            break
        except ValueError:
            print('Data inválida! Use o formato dd/mm/aaaa')

    observations = str(input('Observações da amostra: '))
    sample = [name, sample_type, date, observations]
    samples.append(sample)
    print('Amostra salva com sucesso!')

def list_samples(samples):
    if len(samples) == 0:
        print('Nenhuma amostra cadastrada ainda!')
    for i, sample in enumerate(samples):
        sleep(1)
        print('-'*30)
        print(f'{i+1}° amostra:'.center(30))
        print('-' * 30)
        print(f'   - Nome: {sample[0]}')
        print(f'   - Tipo: {sample[1]}')
        print(f'   - Data da coleta: {sample[2]}')
        print(f'   - Observações: {sample[3]}')

def delete_sample(samples):
    if len(samples) == 0:
        print('Nenhuma amostra cadastrada!')
        return

    list_samples(samples)

    while True:
        choice = int(input('Digite o número da amostra que deseja remover: '))

        if choice <1 or choice > len(samples):
            print('Essa amostra não existe! Verifique e tente novamente')
            continue

        index = choice - 1
        break
    confirm = input(f'Tem certeza que deseja remover a amostra {choice}? (S/N)').strip().upper()
    if confirm == 'S':
        samples.pop(index)
        print('Amostra removida com sucesso!')
    else:
        print('Operação cancelada!')

def search_sample(samples):
    if len(samples) == 0:
        print('Nenhuma amostra cadastrada!')
        return

    while True:
        search = int(input('''  Você deseja buscar por:   
    1 - Nome da amostra
    2 - tipo da amostra
    '''))
        if search == 1:
            name = str(input('Digite o nome da amostra: ')).lower()

            found = False

            for sample in samples:
                sample_name = sample[0].lower()

                if name in sample_name:
                    print(f'Nome: {sample[0]} | Tipo: {sample[1]} | Data: {sample[2]} | Observação: {sample[3]}')
                    found = True
            if not found:
                print('Nenhuma amostra encontrada com esse nome')

        elif search == 2:
            search_type = str(input('Digite o tipo da amostra: ')).lower()

            found = False

            for sample in samples:
                sample_type_value = sample[1].lower()

                if search_type in sample_type_value:
                    print(f'Nome: {sample[0]} | Tipo: {sample[1]} | Data: {sample[2]} | Observação: {sample[3]}')
                    found = True
            if not found:
                print('Nenhuma amostra encontrada com esse tipo')
            break