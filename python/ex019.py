import random
aluno1= input('digite os nomes para o sorteio: ')
aluno2 = input('Digite o segundo nome: ')
aluno3 = input('digite o terceiro nome: ')
lista = [aluno1, aluno2, aluno3]
nome = random.choice(lista)
print('O nome sorteado e {}'.format(nome))