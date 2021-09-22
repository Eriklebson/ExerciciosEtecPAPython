print("==================================================")
nomeDoPTime = input("Informe o nome do primeiro time:")
pontosDoTime1 = int(input("Informe a quantidade de pontos do time:"))
print("==================================================")
nomeDoSTime = input("Informe o nome do segundo time:")
pontosDoTime2 = int(input("Informe a quantidade de pontos do time:"))
print("==================================================")

if(pontosDoTime1 > pontosDoTime2):
    print("O time", nomeDoPTime, "é o vendedor")
elif(pontosDoTime1 == pontosDoTime2):
    print("EMPATE")
else:
    print("O time", nomeDoSTime, "é o vendedor")
