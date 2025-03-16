import re
import random

def validar_cpf(cpf):
    cpf = re.sub(r'[^0-9]', '', cpf)

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * len(cpf):
        print('Você enviou dados sequenciais.')
        return False

    soma_1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito_1 = (soma_1 * 10) % 11
    digito_1 = digito_1 if digito_1 < 10 else 0

    soma_2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito_2 = (soma_2 * 10) % 11
    digito_2 = digito_2 if digito_2 < 10 else 0

    if cpf[-2:] == f'{digito_1}{digito_2}':
        return True
    else:
        return False

def gerar_cpf():
    cpf_base = ''.join([str(random.randint(0, 9)) for _ in range(9)])
    soma_1 = sum(int(cpf_base[i]) * (10 - i) for i in range(9))
    digito_1 = (soma_1 * 10) % 11
    digito_1 = digito_1 if digito_1 < 10 else 0

    soma_2 = sum(int(cpf_base[i]) * (11 - i) for i in range(10))
    digito_2 = (soma_2 * 10) % 11
    digito_2 = digito_2 if digito_2 < 10 else 0

    return f'{cpf_base}{digito_1}{digito_2}'

def gerar_multiplos_cpfs(qtd):
    cpfs_gerados = []
    for _ in range(qtd):
        cpf = gerar_cpf()
        while not validar_cpf(cpf):
            cpf = gerar_cpf()
        cpfs_gerados.append(cpf)
    return cpfs_gerados

quantidade = int(input('Quantos CPFs você deseja gerar? '))

cpfs = gerar_multiplos_cpfs(quantidade)

for i, cpf in enumerate(cpfs, 1):
    print(f'CPF gerado ({i}): {cpf}')
