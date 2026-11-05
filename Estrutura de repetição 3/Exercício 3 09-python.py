mediaSalOp = 0.0
totalSalAdm = 0.0
totalSal = 0.0
salarioAdm = 0.0
salarioOp = 0.0
qtdAdm = 0 
qtdOp = 0
salario = 0.0
cod = 0
repeticao = 4
while (qtdAdm + qtdOp) < 4:
    cod = int(input("Digite o código de funcionario, sendo:\n[1] - Setor Administrativo\n[2] - Setor Operacional\nDigite aqui: "))
    if cod == 1:
        qtdAdm +=1
        salarioAdm += salario
        totalSal += salario
    elif cod == 2:
        qtdOp +=1
        salarioOp += salario
        totalSal += salario
    else:
        print("Código invalido, digite novamente: ")
        salario = salario-salario

    salario = float(input("Digite o salário: "))

print("A media salarial do setor administrativo é: R$",salarioAdm/qtdAdm)
print("A media salarial do setor operacional é: R$",salarioOp/qtdOp)
print("O total de salarios pagos pela empresa é: R$",totalSal)
print("A quantidade de funcionarios do setor administrativo é: R$",qtdAdm)
print("A quantidade de funcionarios do setor operacional é: R$",qtdOp)