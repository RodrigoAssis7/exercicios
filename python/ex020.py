from random import shuffle
aluno01 = str(input('primeiro nome: '))
aluno02 =  str(input('segundo nome:'))
aluno03 =  str(input('terceiro nome: '))
aluno04 =  str(input('quarto nome: '))
lista = [aluno01, aluno02, aluno03, aluno04]
shuffle(lista)
print("a ordem sera: ")
print(lista)