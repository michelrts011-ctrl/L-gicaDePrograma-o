alimentoNaoPerecivel = 0
alimentoPerecivel = 0
vestuario = 0
higiene = 0
limpeza = 0
total = 0

while True:
    cod = int(input("Digite o código do produto: "))
    if cod == 0:
        break
    elif cod >0 and cod < 16:
        match cod:
            case 1:
                print ("Alimento não-perecível")
                alimentoNaoPerecivel += 1
            case 2|3|4:
                print ("Alimento perecível")
                alimentoPerecivel += 1
            case 5|6:
                print ("Vestuário")
                vestuario += 1
            case 7:
                print ("Higiene pessoal")
                higiene += 1
            case 8|9|10|11|12|13|14|15:
                print ("Limpeza e utensilios domésticos")
                limpeza += 1
    else:
     print ("codigo invalido")

print ("A quantidade de alimento não-perecível é ", alimentoNaoPerecivel)
print ("A quantidade de alimento perecível é ",alimentoPerecivel )
print ("A quantidade de vestuário é ", vestuario)
print ("A quantidade de higiene pessoal é ", higiene)
print ("A quantidade de limpeza e utensilios domésticos é ", limpeza)