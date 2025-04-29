def rolar_dados(n):
    import random
    dados = []
    for i in range(n):
        dados.append(random.randint(1,6))
    return dados
