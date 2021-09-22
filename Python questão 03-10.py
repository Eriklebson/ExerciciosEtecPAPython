print("=============================")
nome = input("Informe o nome do aluno:")
n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
n3 = float(input("Informe a terceira nota: "))
n4 = float(input("Informe a quarta nota: "))
media = float
print("=============================")

media = (n1 + n2 + n3 + n4) / 4

print("A media do aluno é", media)
if (media > 7):
     print("O", nome, "foi aprovado")
elif (media >= 5.1 and media <= 6.9):
       print("O", nome, "esta de recuperação")
else:
    print("O", nome, "foi reprovado")

print("=============================")
