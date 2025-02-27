salario = float(input("Digite  o valor  do salario  atual: "))

if salario < 10000:
    salario = salario * 1.1
    print("O Fucionário tem direito  ao aumento de 10%")
    print(" O novo salário é de  %.2f" % salario)
    print(f"O novo salário é de  {salario: .2f}")
    print("Parabéns pelo salario!!")