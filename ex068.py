#Faça um programa que jogue par ou ímpar com o camputador. O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
from time import sleep
print('\033[31m=\033[m'*40)
print('             PAR OU ÝMPAR')
print('\033[31m=\033[m'*40)
vitorias = 0
nome = str(input('Qual o seu nome? ')).upper()
while True:
    escolhajogador = str(input('Escolhe Par ou Ýmpar? ')).upper()
    while escolhajogador not in 'PARIMPARÝMPAR':
        print('Escolha Inválida. Tente novamente.')
        escolhajogador = str(input('Escolhe Par ou Ýmpar? ')).upper()
        numjogador = str(input('Escolha um número inteiro entre 0 e 10: '))
        if '.' in numjogador:
            numjogador = float(numjogador)
            numjogador = int(numjogador)
            print(f'Vamos brincar só com a parte inteira, tá? Então fica com {numjogador}.')
        else:
            numjogador = int(numjogador)
            while numjogador > 10 or numjogador < 0:
                print('Escolha Inválida. Tente novamente.')
                numjogador = str(input('Escolha um número entre 0 e 10: '))
                if '.' in numjogador:
                    numjogador = float(numjogador)
                    numjogador = int(numjogador)
                    print(f'Vamos brincar só com a parte inteira, tá? Então fica com {numjogador}.')
                else:
                    numjogador = int(numjogador)
                numcomputador = randint(0, 10)
                for c in range(1, 4):
                    print(c, end='... ')
                    sleep(1)
                print('e', end='... ')
                sleep(1)
                print('JÝ!')
                print('\033[32m=\033[m'*40)
                print(f'{nome}         vs.        COMPUTADOR')
                print(f'   {numjogador}             +              {numcomputador}')
                soma = numjogador + numcomputador
                print(f'              SOMA: {soma}')
                if soma %2 == 0:
                    resultado = 'P'
                else:
                    resultado = 'IÝ'
                print('\033[32m=\033[m'*40)
                escolhajogador = escolhajogador.strip()[0]
                if escolhajogador in resultado:
                    print(f'         {nome} VENCEU!\n'
                        f'          Vamos de novo!')
                    vitorias += 1
                    print(f'\033[32m=\033[m'*40)
                if escolhajogador not in resultado:
                    break
        print('           EU VENCI!')
        if vitorias > 1:
            print(f'Você conquistou {vitorias} vitórias consecutivas!')
        elif vitorias == 1:
            print('Você conquistou apenas uma vitória!')
        else:
            print('Você não conquistou nenhuma vitória!')
