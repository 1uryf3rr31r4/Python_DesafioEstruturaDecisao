comb = float(input("Quantos litros de combustivel foram comprados: "))
tipoComb = str(input("Qual tipo de combustivel foi comprado A-álcool e G-gasolina: "))

precoA = 1.9
precoG = 2.5  

if tipoComb == "A":
  combPG = comb * precoA

if tipoComb == "G":
  combPG = comb * precoG

if comb <= 20 and tipoComb == "A":
  combPG = combPG * (1 - 0.03)

if comb > 20 and tipoComb == "A":
  combPG = combPG * (1 - 0.05)

if comb <= 20 and tipoComb == "G":
  combPG = combPG * (1 - 0.04)

if comb > 20 and tipoComb == "G":
  combPG = combPG * (1 - 0.06)
  
print(combPG)
  
