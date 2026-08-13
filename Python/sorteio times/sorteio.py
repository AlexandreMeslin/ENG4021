#!/home/codespace/.python/current/bin/python
'''
Este programa gera um sorteio de times para ENG4021
Entrada:
    - número de alunos
    - posição inicial da lista de alunos na planilha Excel
    - prefixo para a planilha Excel no formato '=aba!letra da célula (sem número)' (ex: "='Notas-Projeto-A'!C") 
Saída:
    - lista de times sorteados
'''

import random

def main():
    # Solicita o número de alunos e a posição inicial da lista
    num_alunos = int(input("Digite o número de alunos: "))
    pos_inicial = int(input("Digite a posição inicial da lista de alunos na planilha Excel: "))
    prefixo = input("Digite o prefixo para a planilha Excel: ")


    # Gera uma lista de alunos com base no número fornecido
    alunos = [f"{prefixo}{i + pos_inicial}" for i in range(num_alunos)]

    # Embaralha a lista de alunos
    random.shuffle(alunos)

    # Exibe os times sorteados
    for aluno in alunos:
        print(f"{aluno}")
    # Apenas para deixar claro que a função terminou aqui
    return

if __name__ == "__main__":
    main()