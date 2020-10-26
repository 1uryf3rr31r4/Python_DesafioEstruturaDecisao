num = float(input("Digite o valor: "))
opcao = 0

while opcao != 5:

    print("[1] Par ou Ímpar")
    print("[2] Positivo e negativo")
    print("[3] Inteiro ou Decimal")
    print("[4] Novos número")
    print("[5]Sair do programa")
    opcao = int(input("Qual é a opção: "))
    
    if opcao == 1:
        if num % 2 == 0:
            print("Esse número é par")

        else:
            print("Esse número é ímpar")

    elif opcao == 2:
        if num > 0:
            print("Esse número é positivo")

        else:
            print("Esse número é negativo")

    elif opcao == 3:
        if num == int(num):
            print("Esse número é inteiro")

        else:
            print("Esse número é decimal")
    elif opcao == 4:
        print("Informe o valor novamente")
        num = float(input("Digite o valor: "))

    elif opcao == 5:
        print("Saindo do programa")

    else:
        print("Opção Inválida")

    print("=-="*10)

