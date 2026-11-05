num = 0.0
numPares = 0.0
somaNumPares = 0.0
media = 0.0

while True:
    num = float(input("Digite um número: "))
    if num < 0:
        break
    elif num >= 0:
     numPares += 1
     somaNumPares += num
print ("Média: ",somaNumPares/numPares)