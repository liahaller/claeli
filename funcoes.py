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
    for i in range(len(lista)-1):
        if lista[i]+1 in lista:
            j += 1
        if j >= 4:
            break
        if lista[i]+1 not in lista:
            j = 1
    if j >= 4:
        return 15
    else:
        return 0
    
def calcula_pontos_sequencia_alta(dados):
    j = 1
    dados = sorted(dados)
    lista=[]
    for i in range(len(dados)):
        if dados[i] not in lista:
            lista.append(dados[i])
    for i in range(len(lista)-1):
        if lista[i]+1 in lista:
            j += 1
        if j >= 5:
            break
        if lista[i]+1 not in lista:
            j = 1
    if j >= 5:
        return 30
    else:
        return 0
    
def calcula_pontos_full_house(dados):
    soma=0
    dicio={1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for i in range(len(dados)):
        dicio[dados[i]] += 1
    if 2 in dicio.values() and 3 in dicio.values():
        for i in range(len(dados)):
            soma += dados[i]
    return soma

def calcula_pontos_quadra(dados):
    soma=0
    dicio={1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for i in range(len(dados)):
        dicio[dados[i]] += 1
    for ocorrencias in dicio.values():
        if ocorrencias >= 4:
            for i in range(len(dados)):
                soma += dados[i]
            break
    return soma

def calcula_pontos_quina(dados):
    dicio={1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for i in range(len(dados)):
        dicio[dados[i]] += 1
    for ocorrencias in dicio.values():
        if ocorrencias >= 5:
            return 50
    return 0

def calcula_pontos_regra_avancada(dados):
    dicio = {'cinco_iguais': calcula_pontos_quina(dados), 'full_house': calcula_pontos_full_house(dados), 'quadra': calcula_pontos_quadra(dados), 'sem_combinacao': calcula_pontos_soma(dados), 'sequencia_alta': calcula_pontos_sequencia_alta(dados), 'sequencia_baixa': calcula_pontos_sequencia_baixa(dados)}
    return dicio

def faz_jogada(dados, categoria, cartela_de_pontos):
    regra=0
    for tipo in cartela_de_pontos.keys():
        if categoria in tipo:
            regra=tipo
    if regra=='regra_avancada':
        cartela_de_pontos[regra][categoria]= calcula_pontos_regra_simples(dados)[categoria]
    return cartela_de_pontos

      