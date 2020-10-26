tipoCarne = str(input("Qual o tipo de carne foram comprados F-File Duplo, A-Alcatara, P-Picanha: "))
kgCarne = float(input("Quantos kilos de carne foram comprados: "))
tipoPG = str(input("O pagamento foi no cartão Tabajara: "))

desconto = 0

if kgCarne <= 5 and tipoCarne == "F":
  pgCarne = kgCarne * 4.9
else:
  pgCarne = kgCarne * 5.8
  
if kgCarne <= 5  and tipoCarne == "A":
  pgCarne = kgCarne * 5.9
else:
  pgCarne = kgCarne * 6.8

if kgCarne <= 5  and tipoCarne == "P":
  pgCarne = kgCarne * 6.9
else:
  pgCarne = kgCarne * 7.8

if tipoPG == "Sim":
  desconto = pgCarne * 0.1
  pgCarneD = pgCarne - desconto

if tipoCarne == "F":
  print("Tipo de carne: Picanha ")
elif tipoCarne == "A":
  print("Tipo de carne: Alcantara ")
elif tipoCarne == "P":
  print("Tipo de carne: Picanha")

print("A quantidade de carne comprada:", kgCarne)
print("Preço Total:", pgCarne)

if tipoPG == "Sim":
  print("Pagamento com o uso do cartão Tabajara")
else:  
  print("Pagamento sem o uso do cartão Tabajara")

print("O valor do desconto: {}".format(desconto))

if tipoPG == "Sim":
  print("Valor pago:", pgCarneD)

else:
  print("Valor pago:", pgCarne)
