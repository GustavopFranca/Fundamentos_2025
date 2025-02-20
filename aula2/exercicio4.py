taxa = float(input("digite a taxa horaria: "))
horas = int(input("digite a quantidade de horas: "))

salarioBruto = taxa * horas

desconto = salarioBruto * 0.11
descontoInss = salarioBruto * 0.8
descontoSindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - desconto - descontoInss - descontoSindicato

print(f"salario bruto: {salarioBruto:2f}")
print(f"Desconto imposto de renda: {salarioBruto:2f}")
print(f"salario bruto: {salarioBruto:2f}")
print(f"salario bruto: {salarioBruto:2f}")
print(f"salario bruto: {salarioBruto:2f}")
