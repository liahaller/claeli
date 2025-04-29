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
    return [nova, dados_guardados]

def remover_dado(dados_rolados,dados_guardados,numero):
    dados_guardados_novo = []
    dados_rolados.append(dados_guardados[numero])
    for i in range(len(dados_guardados)):
        if i != numero:
            dados_guardados_novo.append(dados_guardados[i])
    return[dados_rolados,dados_guardados_novo]

def calcula_pontos_regra_simples(dados):
    dicio={1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for i in range(len(dados)):
        dicio[dados[i]] += dados[i]
    return dicio

def calcula_pontos_soma(dados_rolados):
    soma = 0
    for i in range(len(dados_rolados)):
        soma += dados_rolados[i]
    return soma

def calcula_pontos_sequencia_baixa(dados):
    j = 1
    dados = sorted(dados)
    lista=[]
    for i in range(len(dados)):
        if dados[i] not in lista:
            lista.append(dados[i])
    for i in range(len(lista)):
        if lista[i]+1 in lista:
            j += 1
        else:
            j = 1
    if j >= 4:
        return 15
    else:
        return 0 


      