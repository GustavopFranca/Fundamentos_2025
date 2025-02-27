PI = 3.1415

# Recupera do usuário o raio  e a altura do clindro
raio = float(input("digite o raio do cilindro"))
altura = float(input("digite a autura do cilindro"))

# Calcular a area base

areabase = PI * raio * raio # pi * raio ** 2

# Calcular  a area lateral

arealateal = altura * 2  *PI * raio

#Calcular a area do cilindro

areacilindro = areabase + arealateal
print(f"Area a ser pintada: {areacilindro:.2f} m²")

# calcular o volume de tinta
volumetinta = areacilindro / 3
print(f"qtde de litros necessario {volumetinta:.2f}")

#
latastinta = ceill(volumetinta / 5)
print(f"qntd de latas: {latastinta}")

#Encontrar o preco unitario com base na quantidade de latas
if latastinta == 1:
    preco = 50
if latastinta == 2:
    preco = 48
if latastinta == 3:
    preco = 46
else:
    preco = 45

    print(f"preco unitario: {preco}")