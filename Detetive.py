pergunta1 = str(input("Telefonou para a vítima? "))
pergunta2 = str(input("Esteve no local do crime? "))
pergunta3 = str(input("Mora perto da vítima? "))
pergunta4 = str(input("Devia para a vítima? "))
pergunta5 = str(input("Já trabalhou com a vítima? "))
opcao = 0

while opcao != 3:

    print("[1] Veredito")
    print("[2] Nova Investigação")
    print("[3] Sair do programa")
    opcao = int(input("Qual é a opção: "))

    invest = 0
    
    if opcao == 1:
        
        if pergunta1 == "Sim":
            invest += 1 
        if pergunta2 == "Sim":
            invest += 1
        if pergunta3 == "Sim":
            invest += 1
        if pergunta4 == "Sim":
            invest += 1
        if pergunta5 == "Sim":
            invest += 1

        if invest == 5:
            print("A pessoa é o Assasino")

        elif invest == 4 or invest == 3:
            print("A pessoa é um Cúmplice")
            
        elif invest == 2:
            print("A pessoa é um Suspeito")

        else:
            print("A pessoa é inocente")

    elif opcao == 2:
        print("responda as perguntas novamente")
        pergunta1 = str(input("Telefonou para a vítima? "))
        pergunta2 = str(input("Esteve no local do crime? "))
        pergunta3 = str(input("Mora perto da vítima? "))
        pergunta4 = str(input("Devia para a vítima? "))
        pergunta5 = str(input("Já trabalhou com a vítima? "))

    elif opcao == 3:
        print("Saindo do programa")

    else:
        print("Opção Inválida")

    print("=-="*10)

