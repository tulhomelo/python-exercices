import random

''' Tulho Melo - RA 321213318 '''
'''
Chefe e Chefina jogam dado. Em cada turno, eles jogam um par de dados, cada um. Eles consideram um bom turno se a soma dos valores dos dois dados for maior que 6. Escreva um programa que apresente como saída desse jogo a seguinte estrutura:

- - -Chefina joga
Valor somado nos dois dados: x

- - - Chefe joga
Valor somado nos dois dados: y

- - - Continuar jogo S ou N: 

Se a escolha for S, então uma nova rodada acontece. Caso contrário, o programa encerra. Use o módulo 'random' do python com o método 'randint()'. Dê uma pesquisada sobre esse método. Use, também, a função input(“mensagem”) para receber entrada de dados. Exemplo:

    n = input(“Informe um numero: “)
    print(n)
'''


def jogo_dados(turno):
    '''Define como o jogo funciona'''

    # Começando um novo turno
    print("\nIniciando o turno", turno, "do jogo de dados.")
    print("\n\tChefina X Chefe")
    # Dados da Chefina
    print("\nChefina joga")
    chefina_dado_1 = random.randint(1, 6)
    chefina_dado_2 = random.randint(1, 6)
    soma_dados_chefina = chefina_dado_1 + chefina_dado_2
    print("Valor somado nos dois dados: ", soma_dados_chefina)

    # Dados do Chefe
    print("\nChefe joga")
    chefe_dado_1 = random.randint(1, 6)
    chefe_dado_2 = random.randint(1, 6)
    soma_dados_chefe = chefe_dado_1 + chefe_dado_2
    print("Valor somado nos dois dados: ", soma_dados_chefe)

    # Verificação dos turnos
    if (soma_dados_chefina > 6 and soma_dados_chefe > 6):
        print("\n>> Tanto Chefina quanto Chefe tiveram um bom turno.")
    elif (soma_dados_chefina > 6):
        print("\n>> Somente a Chefina teve um bom turno.")
    elif (soma_dados_chefe > 6):
        print("\n>> Somente o Chefe teve um bom turno.")
    else:
        print("\n>> Nenhum dos dois teve um bom turno.")

    # Lower para tratar as entradas do usuários
    resposta = (input("\nContinuar jogo S ou N: ")).lower()
    # Verifica se o jogo continua
    if (resposta == "s" or resposta == "sim"):
        print("\nComençando nova partida!")
        turno += 1
        jogo_dados(turno)
    else:
        print("\nJogo finalizado!\n")


# Inicia o jogo
jogo_dados(1)
