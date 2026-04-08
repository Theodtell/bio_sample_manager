def read_int(msg):
    while True:
        try:
            val = int(input(msg))
            return val
        except ValueError:
            print('ERRO: Digite um número inteiro válido.')