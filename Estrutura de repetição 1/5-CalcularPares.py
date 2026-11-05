num = 0
numPares = 0
somaNumPares = 0
media = 0.0

while True:
    num = float(input("Digite um número: "))
    if num == 0:
        break
    elif num % 2 == 0:
     numPares += 1
     somaNumPares += num
print ("Média: ",somaNumPares/numPares)