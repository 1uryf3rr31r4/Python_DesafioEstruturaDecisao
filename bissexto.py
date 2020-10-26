ano = int(input("Digite o ano a ser verificado: "))

bissexto = ano % 4

if bissexto == 0:
    print("O ano {} é bissexto".format(ano))
else:
    print("O ano {} não é bissexto".format(ano))
    
