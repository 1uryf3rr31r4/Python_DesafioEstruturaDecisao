'''ladoT = [0, 0, 0]
igual = 0
for l in range(0,3):
    ladoT[l] = float(input("Digite o lado do triângulo: "))

for i in range(0,3):
    for j in range(0,3):
        if ladoT[i] == ladoT[j]:
            igual += 1

print(igual)'''

ladoT1 = float(input("Digite o lado 1 do triangulo: "))
ladoT2 = float(input("Digite o lado 2 do triangulo: "))
ladoT3 = float(input("Digite o lado 3 do triangulo: "))

if ladoT1 == ladoT2 and ladoT1 == ladoT3 and ladoT2 == ladoT3:
    print("Triangulo Equilátero")

elif ladoT1 != ladoT2 and ladoT1 != ladoT3 and ladoT2 != ladoT3:
    print("Triangulo Escaleno")

elif ladoT1 == ladoT2 and ladoT1 == ladoT3 and ladoT2 != ladoT3:
    print("Triangulo Isósceles")

elif ladoT1 == ladoT2 and ladoT1 != ladoT3 and ladoT2 == ladoT3:
    print("Triangulo Isósceles")

elif ladoT1 != ladoT2 and ladoT1 == ladoT3 and ladoT2 == ladoT3:
    print("Triangulo Isósceles")

elif ladoT1 == ladoT2 and ladoT1 != ladoT3 and ladoT2 != ladoT3:
    print("Triangulo Isósceles")

elif ladoT1 != ladoT2 and ladoT1 == ladoT3 and ladoT2 != ladoT3:
    print("Triangulo Isósceles")

elif ladoT1 != ladoT2 and ladoT1 != ladoT3 and ladoT2 == ladoT3:
    print("Triangulo Isósceles")

else:
    print("Valores Inválidos")
