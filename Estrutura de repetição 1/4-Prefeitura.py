somaSalarios = 0
somaFilhos = 0
maiorSalario = 0
quantidade = 0
ate100 = 0

while True:
    salario = float(input("Digite o salário: "))
    if salario < 0:
        break
    filhos = int(input("Digite o número de filhos: "))
    
    somaSalarios += salario
    somaFilhos += filhos
    quantidade += 1

    if salario > maiorSalario:
        maiorSalario = salario
    if salario <= 100:
        ate100 += 1

mediaSalario = somaSalarios / quantidade
mediaFilhos = somaFilhos / quantidade
percentual = (ate100 / quantidade) * 100

print("Média do salário:", mediaSalario)
print("Média de filhos:", mediaFilhos)
print("Maior salário:", maiorSalario)
print("Percentual com salário até R$100:", percentual, "%")