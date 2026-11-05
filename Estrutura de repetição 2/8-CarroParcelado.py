pr = 0
valorF = 0
valorP = 0
valorC = int(input("Digite o valor do carro: "))
pag = int(input("Digite a forma de pagamento(1- A vista e 2- Parcelado): "))

if pag == 1:
    valorF = valorC * 0.8
    print (valorF)
if pag == 2:
    pr = int(input("Quantas parcelas?\n[1] - 6\n[2] - 12\n[3] - 18\n[4] - 24\n[5] - 30\n[6] - 36\n[7] - 42\n[8] - 48\n[9] - 54\n[10] - 60\nDigite aqui:"))
    if pr == 1:
     valorP = (valorC / 6)*1.03
     valorF = valorP * 6
     print ("R$",valorF, "a quantidade de parcelar é 6, o valor da parcela", valorP)
    elif pr == 2:
     valorP = (valorC / 12)*1.06
     valorF = valorP * 12
     print ("R$",valorF, "a quantidade de parcelar é 6, o valor da parcela", valorP)
    elif pr == 3:
     valorP = (valorC / 18)*1.09
     valorF = valorP * 18
     print ("R$",valorF, "a quantidade de parcelar é 6, o valor da parcela", valorP)
    elif pr == 4:
     valorP = (valorC / 24)*1.12
     valorF = valorP * 24
     print ("R$",valorF, "a quantidade de parcelar é 6, o valor da parcela", valorP)
    elif pr == 5:
     valorP = (valorC / 30)*1.15
     valorF = valorP * 30
     print ("R$",valorF, "a quantidade de parcelar é 6, o valor da parcela", valorP)
    elif pr == 6:
     valorP = (valorC / 36)*1.18
     valorF = valorP * 36
     print ("R$",valorF, "a quantidade de parcelar é 6, o valor da parcela", valorP)
    elif pr == 7:
     valorP = (valorC / 42)*1.21
     valorF = valorP * 42
     print ("R$",valorF, "a quantidade de parcelar é 6, o valor da parcela", valorP)
    elif pr == 8:
     valorP = (valorC / 48)*1.24
     valorF = valorP * 48
     print ("R$",valorF, "a quantidade de parcelar é 6, o valor da parcela", valorP)
    elif pr == 9:
     valorP = (valorC / 54)*1.27
     valorF = valorP * 54
     print ("R$",valorF, "a quantidade de parcelar é 6, o valor da parcela", valorP)
    elif pr == 10:
     valorP = (valorC / 60)*1.3
     valorF = valorP * 60
     print ("R$",valorF, "a quantidade de parcelar é 6, o valor da parcela", valorP)