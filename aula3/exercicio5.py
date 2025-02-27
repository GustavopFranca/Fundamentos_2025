anoatual = int(input("Digite o ano atual: "))
anonascimento = int(input("Digite o seu ano de nascimento: "))

idade = anoatual - anonascimento

if idade >= 18:
    print("Você pode tirar a CNH!")
else:
    print("Você ainda não pode tirar a CNH.")
