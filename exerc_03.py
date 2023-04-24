
'''
3- A maioria dos desenvolvedores praticam programação resolvendo problemas de lógica em diversas plataformas (https://www.codechef.com/practice, por exemplo). Jenneffer almeja a posição de engenharia de software e, portanto, pretende estudar e praticar bastante. Ela decide que deve resolver pelo menos 10 problemas por semana, durante 4 semanas. Escreva um programa que, dada a quantidade de problemas que ela realmente resolveu em cada semana, P1, P2, P3, e P4, informe se Jenneffer conseguiu cumprir sua meta e, quando verdade, informe em que semana ela cumpriu essa meta.
'''


def estudo_programacao():
    print("\nResumo dos estudos em programação do mês.")
    print("\nA seguir você deve informar a quantidade de problemas resolvidos por semana:")
    # Iniciando um dicionário (dict) para guardar as quantidades por semana
    problemas_resolvidos_semana = {'P1' : None, 'P2' : None, 'P3' : None, 'P4' : None}
    # Preenchendo o dict com a quantidade de problemas resolvidos
    for semana in problemas_resolvidos_semana:
        problemas_resolvidos_semana[semana] = int(input(f"Semana {semana}: "))
    # Variável para contagem de semanas em que a meta foi cumprida
    meta_semana = 0
    # Verificando se a quantidade de problemas resolvidos é igual ou maior que 10
    for semana, qtd_problemas in problemas_resolvidos_semana.items():
        if qtd_problemas >= 10:
            meta_semana += 1
            print(f"Meta na {semana} foi cumprida!")

    # Verificando se a meta foi batida
    if meta_semana == 4:
        print("\nParabéns! Meta cumprida em todas as semanas.\n")
    elif meta_semana > 0:
        print(f"\nA meta foi cumprida em {meta_semana} semana(s) ao todo.\n")
    else:
        print("\nA meta não foi cumprida em nenhuma semana.\n")


# Inicia a função que calcula o programa de estudos semanal
estudo_programacao()