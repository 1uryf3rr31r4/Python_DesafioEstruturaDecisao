num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))
num3 = float(input("Número 3: "))

if num1 > num2 > num3:
    print(num1, num2, num3)
if num1 > num3 > num2:
    print(num1, num3, num2)
if num2 > num1 > num3:
    print(num2, num1, num3)
if num2 > num3 > num1:
    print(num2, num3, num1)
if num3 > num1 > num2:
    print(num3, num1, num2)
if num3 > num2 > num1:
    print(num3, num2, num1)
if num1 == num2 or num1 == num3 or num2 == num3:
    print("Inválido")


