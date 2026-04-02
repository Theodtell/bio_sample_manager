from time import sleep
from samples import register_sample, list_samples, delete_sample, search_sample
samples = []

while True:
    sleep(0.5)
    print('-'*30)
    print('  ====MENU===='.center(30))
    print('Selecione a função desejada:'.center(30))
    print('-' * 30)
    option = int(input('''
    1 - Cadastrar amostras
    2 - Listar amostras
    3 - Remover amostra
    4 - Buscar amostra 
    5- Sair do programa 
    '''))
    if option == 1:
        register_sample(samples)
    elif option == 2:
        list_samples(samples)
    elif option == 3:
        delete_sample(samples)
    elif option == 4:
        search_sample(samples)
    elif option == 5:
        print('Finalizando programa...')
        print('-' * 30)
        sleep(1)
        print('Programa finalizado com sucesso!')
        break
    else:
        print('Opção inválida')

