def rolar_dados(n):
    import random
    dados = []
    for i in range(n):
        dados.append(random.randint(1,6))
    return dados

def guardar_dado(dados_rolados, dados_guardados, numero):
    nova=[]
    dados_guardados.append(dados_rolados[numero])
    for i in range(len(dados_rolados)):
        if i != numero:
            nova.append(dados_rolados[i])
    return nova, dados_guardados

