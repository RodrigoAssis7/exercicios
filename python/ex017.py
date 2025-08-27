from math import hypot
Catops = float(input('digite o valor do cateto oposto: '))
catadj = float(input('Digite o valor do cateto adjacente: '))
conta1 = hypot(Catops, catadj)
print ('A hipotenusa sera {:.2f}!'.format(conta1))