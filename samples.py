import json
from time import sleep
from utils import read_int

def register_sample(samples):
    from datetime import datetime
    while True:
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
        sample = {
            'nome': name,
            'tipo': sample_type,
            'data': str(date),
            'obs' : observations
        }
        samples.append(sample)
        save_samples(samples)
        print('Amostra salva com sucesso!')
        cont = input('Deseja cadastrar outra amostra? (S/N) ').strip().upper()
        if cont != 'S':
            break

def list_samples(samples):
    if len(samples) == 0:
        print('Nenhuma amostra cadastrada ainda!')
    for i, sample in enumerate(samples):
        sleep(1)
        print('-'*30)
        print(f'{i+1}° amostra:'.center(30))
        print('-' * 30)
        print(f"   - Nome: {sample['nome']}")
        print(f"   - Tipo: {sample['tipo']}")
        print(f"   - Data da coleta: {sample['data']}")
        print(f"   - Observações: {sample['obs']}")

def delete_sample(samples):
    while True:
        if len(samples) == 0:
            print('Nenhuma amostra cadastrada!')
            return

        list_samples(samples)

        while True:
            try:
                choice = read_int('Digite o número da amostra que deseja remover: ')

                if choice <1 or choice > len(samples):
                    print('Essa amostra não existe! Verifique e tente novamente')
                else:
                    index = choice - 1
                    break
            except ValueError:
                print('ERRO: Digite apenas números')

        confirm = input(f'Tem certeza que deseja remover a amostra {choice}? (S/N)').strip().upper()
        if confirm == 'S':
            samples.pop(index)
            save_samples(samples)
            print('Amostra removida com sucesso!')
        else:
            print('Operação cancelada!')

        cont = input('Deseja remover outra amostra? (S/N) ').strip().upper()
        break

def search_sample(samples):
    # Se não houver amostras, não faz sentido entrar no loop de busca
    if len(samples) == 0:
        print('Nenhuma amostra cadastrada!')
        return

    while True:
        # Usamos o seu read_int para garantir que o usuário digite um número
        print('\n' + '=' * 30)
        print('      MENU DE BUSCA'.center(30))
        print('=' * 30)
        search = read_int('''
    1 - Buscar por Nome
    2 - Buscar por Tipo
    3 - Voltar ao Menu Principal

    Escolha uma opção: ''')

        if search == 1:
            name_to_find = str(input('Digite o nome da amostra: ')).lower().strip()
            found = False
            print('\nResultados encontrados:')

            for sample in samples:
                # Mudança: acessando por chave 'nome' em vez de [0]
                if name_to_find in sample['nome'].lower():
                    print(f"-> Nome: {sample['nome']} | Tipo: {sample['tipo']} | Data: {sample['data']}")
                    found = True

            if not found:
                print('Nenhuma amostra encontrada com esse nome.')

        elif search == 2:
            type_to_find = str(input('Digite o tipo da amostra: ')).lower().strip()
            found = False
            print('\nResultados encontrados:')

            for sample in samples:
                # Mudança: acessando por chave 'tipo' em vez de [1]
                if type_to_find in sample['tipo'].lower():
                    print(f"-> Nome: {sample['nome']} | Tipo: {sample['tipo']} | Data: {sample['data']}")
                    found = True

            if not found:
                print('Nenhuma amostra encontrada com esse tipo.')

        elif search == 3:
            print('Retornando ao menu principal...')
            break  # Este break sai do while da busca e volta para o main.py

        else:
            print('Opção inválida! Escolha 1, 2 ou 3.')

def save_samples(samples):
    with open('samples.json', 'w') as file:
        json.dump(samples, file, indent= 4)

def load_samples():
    try:
        with open('samples.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []