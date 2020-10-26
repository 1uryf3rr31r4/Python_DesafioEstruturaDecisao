a = float(input("Digite o Valor de a da equação de segundo grau: "))

if a != 0:
    b = float(input("Digite o Valor de b da equação de segundo grau: "))
    c = float(input("Digite o Valor de c da equação de segundo grau: "))

    delta = (b*b) - (4*a*c)

    if delta > 0:
        raiz1 = (-b + delta) / 2*a
        raiz2 = (-b - delta) / 2*a
        print("A equação {}x2 + {}x + {} tem o delta positivo e gera duas raizes: {} e {} ".format(a, b, c, raiz1, raiz2))

    elif delta == 0:
        raiz1 = (-b + delta) / 2*a
        print("A equação {}x2 + {}x + {} tem o delta igual a zero e gera uma raiz: {}".format(a, b, c, raiz1))

    else:
        print("A equação não possui raizes reais")

else:
    print("A equação não é do segundo grau")
