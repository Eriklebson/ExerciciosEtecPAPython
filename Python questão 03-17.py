n1 = int(input("Informe o primeiro valor: "))
n2 = int(input("Informe o segundo valor:"))
n3 = int(input("Informe o terceiro valor:"))

if (n1 < n2):
    if(n2 < n3):
        print(n1)
        print(n2)
        print(n3)
    elif (n1 < n3):
        print(n1)
        print(n3)
        print(n2)
    else:
        print(n3)
        print(n1)
        print(n2)
elif(n2 < n3):
    if(n1 < n3):
        print(n2)
        print(n1)
        print(n3)
    else:
        print(n2)
        print(n3)
        print(n1)
else:
    print(n3)
    print(n2)
    print(n1)
    
