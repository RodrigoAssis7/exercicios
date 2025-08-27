dias = int(input('Quantos dias alugados: '))
km = float(input('Quantos Km rodados: '))
c = (dias * 60) + (km * 0.15)
print("A quantidade a se pagar pelo aluguel e R${:.2f}!".format(c))