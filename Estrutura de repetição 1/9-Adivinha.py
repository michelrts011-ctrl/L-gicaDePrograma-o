import random

adivinha = random.randint(1,50)

for i in range (5):
 num = int(input("Digite um número de 1 a 50: "))
 
 if num == adivinha:
  print ("Vitória!")
  break
 elif adivinha > num:
  print (num ," é menor que o número.")
 elif adivinha < num:
  print (num ," é maior que o número.")
 else:
  i += 1
if num != adivinha:
 print ("O número era ", adivinha)