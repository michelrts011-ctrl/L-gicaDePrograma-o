paisA = 90000000
paisB = 140000000
ano = 0

while paisA <= paisB:
    paisA += paisA*0.035
    paisB += paisB*0.01
    ano += 1

print ("Levou ",ano , "anos para o pais A ter mais população que o pais B.")
print ("A população do pais A ficou: ",paisA)
print ("A população do pais B ficou: ",paisB)