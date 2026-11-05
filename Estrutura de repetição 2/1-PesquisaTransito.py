codigoCidade = 0
numeroVeiculos = 0
numeroAcidentes = 0
menorAcidente = float('inf')
maiorAcidente = float('inf')
cidadeMaior = 0
cidadeMenor = 0
somaTodasCidades = 0
somaSCVeiculos = 0
qtdSC = 0
somaRSVeiculos = 0
qtdRS = 0
somaPRVeiculos = 0
qtdPR = 0
somaSCAcidentes = 0
somaRSAcidentes = 0
somaPRAcidentes = 0

for i in range (12):
    codigoCidade = int(input("Digite o código da cidade: "))
    numeroVeiculos = int(input("Digite o número de veículos: "))
    numeroAcidentes = int(input("Digite o número de acidentes: "))

    if numeroAcidentes > maiorAcidente:
     maiorAcidente = numeroAcidentes
     cidadeMaior = codigoCidade
 
    if numeroAcidentes < menorAcidente:
     menorAcidente = numeroAcidentes
     cidadeMenor = codigoCidade

    somaTodasCidades += numeroVeiculos

    if codigoCidade >= 11 and codigoCidade <= 14:
     somaSCVeiculos += numeroVeiculos
     somaSCAcidentes += numeroAcidentes
     qtdSC += 1
 
    elif codigoCidade >= 21 and codigoCidade <= 24:
     somaRSVeiculos += numeroVeiculos
     somaRSAcidentes += numeroAcidentes
     qtdRS += 1
 
    elif codigoCidade >= 31 and codigoCidade <= 34:
     somaPRVeiculos += numeroVeiculos
     somaPRAcidentes += numeroAcidentes
     qtdPR += 1

print("A média de veículos no Brasil é: ", (somaTodasCidades / 12))
print("A média de veículos em SC é: ", (somaSCVeiculos / qtdSC))
print("A média de acidentes em SC é: ", (somaSCAcidentes / qtdSC))
print("A média de veículos em RS é: ", (somaRSVeiculos / qtdRS))
print("A média de acidentes em RS é: ", (somaRSAcidentes / qtdRS))
print("A média de veículos em PR é: ", (somaPRVeiculos / qtdPR))
print("A média de acidentes em PR é: ", (somaPRAcidentes / qtdPR))