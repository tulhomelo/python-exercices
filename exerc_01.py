''' Tulho Melo - RA 321213318 '''
''' Escreva um programa que recebe um número N como entrada e mostre esse número invertido como saída.
    Crie uma função para a solução desse problema.'''


def inverter_numero(num):
    '''Função que inverte um número'''
    str_invertida = ""
    num = str(num)
    # Iterando na string para inverter os caracteres
    for i in range(len(num)-1, -1, -1):
        str_invertida += num[i]
    # Converte string em inteiro
    return str_invertida


def imprimir_numero_invertido():
    '''Função que recebe um número e imprime o número inverso'''
    print("\nVamos receber um número e mostrá-lo invertido.\n")
    # Usuário entra com um número inteiro
    s_num = input("Informe um número inteiro: ")
    num = int(s_num)

    # Invertendo o número
    num_invertido = inverter_numero(num)
    # Imprime o número invertido
    print("Número invertido: ", num_invertido, "\n")


# Chamando a função que inverte o número
imprimir_numero_invertido()
