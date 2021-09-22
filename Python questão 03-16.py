n1 = int(input("Informe o primeiro valor: "))
n2 = int(input("Informe o segundo valor:"))
n3 = int(input("Informe o terceiro valor:"))

if (n1 > n3):
    if (n2 > n3):
        soma = n1 + n2
elif ( n3 > n1):
    if (n2 > n1): 
        soma = n2 + n3
else:
    soma = n1 + n3 

print("A soma dos 2 maiores numeros é", soma)
