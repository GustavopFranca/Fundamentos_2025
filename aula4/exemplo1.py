a = int(input("Digite o lado A: "))
b = int(input("Digite o lado B: "))
c = int(input("Digite o lado C: "))

if a < b + c and b< a + c and c < a + b:

    if a == b and a == c and b == c:
        print("Triangulo equilatero.")

    else:
        if a ==b or a == c or b ==c :
            print("Triangulo isosceles.")

        else:
            print("Triangulo escaleno.")


else: 
        
        print("Os lados não foram um triangulo")