#5.5. Faça um programa que receba o salário de um funcionário e o percentual de aumento,calcule e mostre o valor do aumento e o novo salário.

salario = float(input("digita o salario atual do funcionario: R$ "))
percentual = float(input("digite o percentual de aumento"))

aumento = salario * (percentual / 100)
novo_salario = salario + aumento

print(f"valor do aumento: R${aumento:.2f}")
print(f"novo salario:R$ {novo_salario:.2f}")

#fiz um programa pra receber o salario percentual do aumento, calculei o valor e mostrei o novo salario . 



