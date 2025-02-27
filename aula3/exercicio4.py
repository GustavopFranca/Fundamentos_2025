salario = float(input("Digite o salário do funcionário: R$ "))


if salario > 1250:
    aumento = salario * 0.10  
else:
    aumento = salario * 0.15  


novosalario = salario + aumento


print(f"O novo salário do funcionário é: R$ {novosalario:.2f}")
