from funcoes import rolar_dados
from funcoes import guardar_dado
from funcoes import remover_dado
from funcoes import calcula_pontos_regra_simples
from funcoes import calcula_pontos_soma
from funcoes import calcula_pontos_sequencia_baixa
from funcoes import calcula_pontos_sequencia_alta
from funcoes import calcula_pontos_full_house
from funcoes import calcula_pontos_quadra
from funcoes import calcula_pontos_quina
from funcoes import calcula_pontos_regra_avancada
from funcoes import faz_jogada
from funcoes import imprime_cartela

cartela_de_pontos = {
    'regra_simples': {1:-1, 2:-1, 3:-1, 4:-1, 5:-1, 6:-1},
    'regra_avancada': {
        'full_house':-1, 
        'quadra':-1, 
        'cinco_iguais':-1,
        'sequencia_baixa':-1,
        'sequencia_alta':-1, 
        'sem_combinacao':-1
    }
}

rerrolagens = 0
dados_rolados = rolar_dados(5)
dados_guardados = []

imprime_cartela(cartela_de_pontos)
print(f'Dados rolados: {dados_rolados}')
print(f'Dados guardados: {dados_guardados}')
escolha= input("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
rodadas=0

while rodadas<12:
    print(f'Dados rolados: {dados_rolados}')
    print(f'Dados guardados: {dados_guardados}')
    escolha= input("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

    if escolha == '1':
        indice = int(input("Digite o índice do dado a ser guardado (0 a 4):"))
        dados_rolados, dados_guardados = guardar_dado(dados_rolados, dados_guardados, indice)

    elif escolha == '2':
        indice= int(input("Digite o índice do dado a ser removido (0 a 4):"))
        dados_rolados, dados_guardados = remover_dado(dados_rolados, dados_guardados, indice)
        
    elif escolha == '3':
        if rerrolagens < 2:
            rerrolagens = rerrolagens + 1
            dados_rolados = rolar_dados(len(dados_rolados))
        else:
            print("Você já usou todas as rerrolagens.")
    elif escolha == '4':
        imprime_cartela(cartela_de_pontos)
    elif escolha == '0':
        dados_totais = []
        for i in range(len(dados_guardados)):
            dados_totais.append(dados_guardados[i])
            dados_totais.append(dados_rolados[i])
        combinacao= input("Digite a combinação desejada:")
        achou = 0
        for tipo in cartela_de_pontos:
            if combinacao in cartela_de_pontos[tipo]:
                if cartela_de_pontos[tipo][combinacao] == -1:
                    cartela_de_pontos = faz_jogada(dados_totais, combinacao, cartela_de_pontos)
                    rodada+=1
                else:
                    print("Essa combinação já foi utilizada.")
                achou = achou + 1
            if achou == 0:
                print("Combinação inválida. Tente novamente.")
    else:
        print("Opção inválida. Tente novamente.")
            


soma_simples = 0
soma_total = 0
for valor in cartela_de_pontos['regra_simples'].values():
    soma_simples = soma_simples + valor
    soma_total = soma_total + valor
for valor in cartela_de_pontos['regra_avancada'].values():
    soma_total = soma_total + valor
if soma_simples >= 63:
    soma_total = soma_total + 35

imprime_cartela(cartela_de_pontos)
print(f'Pontuação total: {soma_total}')