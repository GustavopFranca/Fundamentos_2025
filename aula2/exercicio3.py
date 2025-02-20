dias = int(input("digite a qunatidade de dias: "))
horas = int(input("digite a qunatidade de horas: "))
minutos = int(input("digite a qunatidade de minutos: "))
segundos  = int(input("digite a qunatidade de segundos: "))

total = (dias * 24 * 60 * 60 ) + (horas * 60 * 60) + (minutos * 60) + segundos

print(f"O total em segundos é: {total:2f}")