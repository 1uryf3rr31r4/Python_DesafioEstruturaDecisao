kgMaca = float(input("Quantos kilos de maçã foram comprados: "))
kgMorango = float(input("Quantos kilos de morango foram comprados: "))

if kgMorango <= 5:
  compMorango = kgMorango * 2.5
else:
  compMorango = kgMorango * 2.2
  
if kgMaca <= 5:
  compMaca = kgMaca * 1.8
else:
  compMaca = kgMaca * 1.5

pgTotal = compMaca + compMorango

if kgMorango > 8 and kgMaca > 8 and pgTotal > 25:
  pgTotal = pgTotal * (1 - 0.1)

print(pgTotal)
