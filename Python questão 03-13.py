nome = input("Informe o nome do atleta:")
idade = int(input("Informe a idade do atleta:"))

if(idade >= 5 and idade <=10):
    print("O", nome, "Pertence a categoria infantil")
elif(idade >= 11 and idade <= 15):
    print("O", nome, "Pertence a categoria Juvenil")
elif(idade >= 16 and idade <= 20):
    print("O", nome, "Pertence a categoria Junior")
elif(idade >=21 and idade <= 25):
    print("O", nome, "Pertence a categoria Profissional")
else:
    print("O", nome, "É muito jovem ou passou da idade que o club premite")

