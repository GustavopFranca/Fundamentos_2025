distancia = float(input("Digite a distância que você deseja percorrer em km: "))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = 0.50 * 200 + (distancia - 200) * 0.45 

print(f"O preço da passagem é R$ {preco:.2f}")
