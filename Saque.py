saque = int(input("Digite o valor do saque: "))

resultado100 = saque / 100
notas100 = int(resultado100)
sobra100 = saque - (notas100 * 100)

resultado50 = sobra100 / 50
notas50 = int(resultado50)
sobra50 = sobra100 - (notas50 * 50)

resultado10 = sobra50 / 10
notas10 = int(resultado10)
sobra10 = sobra50 - (notas10 * 10)

resultado5 = sobra10 / 5
notas5 = int(resultado5)
sobra5 = sobra10 - (notas5 * 5)

notas1 = sobra5

print("Para sacar a quantia de {} reais, o programa fornece {} notas de 100, {} nota de 50, {} nota de 10, {} nota de 5 e {} nota de 1".format(saque, notas100, notas50, notas10, notas5, notas1))

