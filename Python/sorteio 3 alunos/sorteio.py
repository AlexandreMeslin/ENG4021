import random

alunos = ['Antonio',
           'Eduardo',
           'Giulio',
          ]

random.shuffle(alunos)

for pos, aluno in enumerate(alunos):
    print(f'{pos + 3} - {aluno}')
