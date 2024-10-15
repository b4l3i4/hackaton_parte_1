#6. Faça um programa que receba o salário base de um funcionário, calcule e mostre seusalário a receber, sabendo-se que o funcionário tem gratificação de R$ 50 e paga impostode 10% sobre o salário base.

salario_base = float(input("digite o salario base do funcionario: R$ "))
gratificacao = 50 
imposto = salario_base * 0.10

salario_receber = salario_base + gratificacao - imposto 

print(f"salario a receber: R$ {salario_receber:.2f}")

#