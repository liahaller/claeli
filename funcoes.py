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
    dicio=[]
    soma1=0
    soma2=0
    soma3=0
    soma4=0
    soma5=0
    soma6=0
    for i in range(len(dados)):
        if dados[i]==1:
            soma1+=dados[i]
        elif dados[i]==2:
            soma2+=dados[i]
        elif dados[i]==3:
            soma3+=dados[i]
        elif dados[i]==4:
            soma4+=dados[i]
        elif dados[i]==5:
            soma5+=dados[i]
        elif dados[i]==6:
            soma6+=dados[i]
    dicio[1]= soma1
    dicio[2]= soma2
    dicio[3]= soma3
    dicio[4]= soma4
    dicio[5]= soma5
    dicio[6]= soma6

    return dicio

      