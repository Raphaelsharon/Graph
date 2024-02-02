# Criar o graph

caminhos = list() # Criando os caminhos e definindo o peso

print("Inicio caminhos\n")

# Nomes dos nós

print("\nDigite 0 quando terminar a tebela!\n")

while True:
    de = str(input("Digite de onde parte o caminho: "))
    if de == "0":
        break
    para = str(input("Digite para onde vai o caminho: "))
    dist = int(input("Digite o peso do caminho: "))
    caminhos.append({"De" : de, "Para" : para, "Dist" : dist})

# Nomes dos nós

cidades = list()  

print("\n!!!Inicio cidades!!!\n")

no_1 = str(input("Digite o nome do no: ")) # inicio cidades
cidades.append({"No" : no_1, "Custo" : "Dummy", "Dec_Otima" : "Dummy"})
    
print("Digite 0 quando chegar a penultima linha da tabela!\n")
  
while True:
    no = str(input("Digite o nome do no: "))
    if no == "0":
        break
    cidades.append({"No" : no, "Custo" : "Dummy", "Dec_Otima" : "Dummy"})

no_2 = str(input("Digite o nome do utimo no: ")) # fim cidades
cidades.append({"No" : no_2, "Custo" : "Dummy", "Dec_Otima" : "Dummy"})

dados = {"Caminhos" : caminhos, "Cidades" : cidades}

#Encontrando uma Cidade

def Encontra_Cidade(cidade, dados):
    for i, elemento in enumerate(dados["Cidades"]):
        if elemento["No"] == cidade:
            break
    return elemento["Custo"], i 

#Função Recursiva para o Cálculo do Caminho Minimo
def Caminho_Minimo(dados,cidade = no_2, flag = True):
    
    if cidade == no_1:  # Condição de Contorno
        custo = 0
        melhor = 0
        dec_otima = "Dummy"
    else: 
        melhor = 10**6
        for caminho in dados["Caminhos"]:
            if caminho["Para"] == cidade:
                custo, posicao = Encontra_Cidade(caminho["De"], dados)
                if custo == "Dummy": #Chamada Recursiva
                    custo, dados = Caminho_Minimo(dados, caminho["De"], False)
                custo += caminho["Dist"]
                if custo < melhor:
                    melhor = custo
                    dec_otima = caminho["De"]
    custo, posicao = Encontra_Cidade(cidade, dados)
    dados["Cidades"][posicao]["Custo"] = melhor
    dados["Cidades"][posicao]["Dec_Otima"] = dec_otima
    
    if not flag:
        return melhor, dados
    else:
        politica_otima = list()
        while cidade != no_1:
            politica_otima.append(cidade)
            custo, posicao = Encontra_Cidade(cidade, dados)
            cidade = dados["Cidades"][posicao]["Dec_Otima"]
        politica_otima.append(cidade)
        politica_otima.reverse()
        return melhor, politica_otima
    
melhor, dec_otima = Caminho_Minimo(dados, no_2)
print("O melhor Caminho e:", dec_otima, "\nE seu Custo e de:", melhor)