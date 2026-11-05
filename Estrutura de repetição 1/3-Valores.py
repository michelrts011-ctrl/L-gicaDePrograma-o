num = 1
cont = 0
while num != 0:
    num = int(input("Digite qualquer número e use 0 para finalizar: "))
    if num < 0:
     cont += 1
print (cont , "Números negativo(s)")