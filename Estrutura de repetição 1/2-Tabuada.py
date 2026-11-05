numero = int(input("Digite o número da tabuada: "))
limite = int(input("Digite até onde quer calcular: "))

for cont in range(1, limite + 1):
    print(numero, "x", cont, "=", numero * cont)