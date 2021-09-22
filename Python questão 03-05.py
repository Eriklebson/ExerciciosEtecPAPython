salario = float(input("Informe seu salario: R$"))

if(salario <= 600.00):
    salarioFinal = salario + salario * 0.30
elif (salario >=600.00 and salario <= 1100.00):
    salarioFinal = salario + salario * 0.25
elif (salario >=1100.01 and salario <= 2400.00):
    salarioFinal = salario + salario * 0.20
elif (salario >=2400.01 and salario <= 3550.00):
    salarioFinal = salario + salario * 0.15
else:
    salarioFinal = salario + salario * 0.10

print(salarioFinal)
