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


cartela_de_pontos = {'regra_simples': {1:-1, 2:-1, 3:-1, 4:-1, 5:-1, 6:-1},'regra_avancada': {'sem_combinacao':-1,'quadra':-1,'full_house':-1,'sequencia_baixa':-1,'sequencia_alta':-1,'cinco_iguais':-1}}

rerrolagens = 0
dados_rolados = rolar_dados(5)
dados_guardados = []

imprime_cartela(cartela_de_pontos)

rodadas=0

while rodadas<12:
    print(f'Dados rolados: {dados_rolados}')
    print(f'Dados guardados: {dados_guardados}')
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    escolha = input()

    if escolha == '1':
        print("Digite o índice do dado a ser guardado (0 a 4):")
        indice = input()
        if indice.isdigit():
            indice = int(indice)
        else:
            continue
        if 0 <= indice < len(dados_rolados):
            dados_rolados, dados_guardados = guardar_dado(dados_rolados, dados_guardados, indice)

    elif escolha == '2':
        print("Digite o índice do dado a ser removido (0 a 4):")
        indice = input()
        if indice.isdigit():
            indice = int(indice)
        else:
            continue
        if 0 <= indice < len(dados_guardados):
            dados_rolados, dados_guardados = remover_dado(dados_rolados, dados_guardados, indice)
        
    elif escolha == '3':
        if rerrolagens < 2:
            rerrolagens = rerrolagens + 1
            dados_rolados = rolar_dados(len(dados_rolados))
        else:
            print("Você já usou todas as rerrolagens.")
    elif escolha == '4':
        imprime_cartela(cartela_de_pontos)
    elif escolha == 0:
        regra = None
        dados_totais = dados_guardados + dados_rolados
        print("Digite a combinação desejada:")
        combinacao = input()
        achou = False
        if combinacao.isdigit():
            combinacao = int(combinacao)
        if combinacao in cartela_de_pontos['regra_simples']:
            regra = 'regra_simples'
            achou = True
        elif combinacao in cartela_de_pontos['regra_avancada']:
            regra = 'regra_avancada'
            achou = True
        while not achou or cartela_de_pontos[regra][combinacao] != -1:
            if not achou:
                print("Combinação inválida. Tente novamente.")
            elif cartela_de_pontos[regra][combinacao] != -1:
                print("Essa combinação já foi utilizada.")
            combinacao = input()
            if combinacao.isdigit():
                combinacao = int(combinacao)
            if combinacao in cartela_de_pontos['regra_simples']:
                regra = 'regra_simples'
                achou = True
            elif combinacao in cartela_de_pontos['regra_avancada']:
                regra = 'regra_avancada'
                achou = True
            else:
                achou = False
        cartela_de_pontos = faz_jogada(dados_totais, combinacao, cartela_de_pontos)
        rodadas+=1
        rerrolagens = 0
        dados_rolados = rolar_dados(5)
        dados_guardados = []            
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