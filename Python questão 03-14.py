valorDeVenda = float(input("Informe o valor de venda do produto: R$"))
print("=====================Codigos=====================")
print("1 - Venda a Vista - desconto de 10%")
print("2 - Venda a Prazo 30 dias - desconto de 5%")
print("3 - Venda a Prazo 60 dias - mesmo preço")
print("4 - Venda a Prazo 90 dias - acréscimo de 5%")
print("5 - Venda com cartão de débito - desconto de 8%")
print("6 - Venda com cartão de crédito - desconto de 7%")
print("=================================================")
codigo = int(input("Informe a forma de pagamento (de 1 a 6):"))

if(codigo == 1):
    valorDeVenda = valorDeVenda - valorDeVenda * 0.10
    print("O valor de compra do produto sera: R$ %.2f" %(valorDeVenda), "com desconto de 10%")
elif(codigo == 2):
    valorDeVenda = valorDeVenda - valorDeVenda * 0.05
    print("O valor de compra do produto sera: R$ %.2f" %(valorDeVenda), "com desconto de 5%")
elif(codigo == 3):
    print("Não teve mudança no valor do produto sendo assim: ", valorDeVenda)
elif(codigo == 4):
    valorDeVenda = valorDeVenda + valorDeVenda * 0.05
    print("O valor de compra do produto sera: R$ %.2f" %(valorDeVenda), "com acrescimo de 5%")
elif(codigo == 5):
    valorDeVenda = valorDeVenda - valorDeVenda * 0.08
    print("O valor de compra do produto sera: R$ %.2f" %(valorDeVenda), "com desconto de 8%")
elif(codigo == 6):
    valorDeVenda = valorDeVenda - valorDeVenda * 0.07
    print("O valor de compra do produto sera: R$ %.2f" %(valorDeVenda), "com desconto de 7%")

while(codigo != 1 and codigo != 2 and codigo != 3 and codigo != 4 and codigo != 5 and codigo != 6):
    print("!!!Codigo não encontrado tende novamente!!!")
    codigo = int(input("Informe a forma de pagamento (de 1 a 6):"))

    if(codigo == 1):
        valorDeVenda = valorDeVenda - valorDeVenda * 0.10
        print("O valor de compra do produto sera: R$ %.2f" %(valorDeVenda), "com desconto de 10%")
    elif(codigo == 2):
        valorDeVenda = valorDeVenda - valorDeVenda * 0.05
        print("O valor de compra do produto sera: R$ %.2f" %(valorDeVenda), "com desconto de 5%")
    elif(codigo == 3):
        print("Não teve mudança no valor do produto sendo assim: ", valorDeVenda)
    elif(codigo == 4):
        valorDeVenda = valorDeVenda + valorDeVenda * 0.05
        print("O valor de compra do produto sera: R$ %.2f" %(valorDeVenda), "com acrescimo de 5%")
    elif(codigo == 5):
        valorDeVenda = valorDeVenda - valorDeVenda * 0.08
        print("O valor de compra do produto sera: R$ %.2f" %(valorDeVenda), "com desconto de 8%")
    elif(codigo == 6):
        valorDeVenda = valorDeVenda - valorDeVenda * 0.07
        print("O valor de compra do produto sera: R$ %.2f" %(valorDeVenda), "com desconto de 7%")

