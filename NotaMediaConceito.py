nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media > 9 and media <= 10:
    conceito = "A"

elif media > 7.5 and media <= 9:
    conceito = "B"

elif media > 6 and media <= 7.5:
    conceito = "C"

elif media > 4 and media <= 6:
    conceito = "D"

elif media >= 0 and media <= 4:
    conceito = "E"
    
else:
    print("Nota Inválida")

if conceito == "A" or conceito == "B" or conceito == "C":
    resultado = "Aprovado"
else:
    resultado = "Reprovado"



print("A primeira nota do aluno: {}".format(nota1))
print("A segunda nota do aluno: {}".format(nota2))
print("A média das notas do aluno: {}".format(media))
print("Conceito de Aproveitamento deste aluno: {}".format(conceito))
print("O aluno foi : {}".format(resultado))
