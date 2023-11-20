#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
import random
from random import choice, randint
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# Regras do Jogo:
# Pedra ganha de tesoura
# Tesoura ganha de papel
# Papel ganha de pedra

# opções do computador para escolha
escolha_computador = ['Pedra', 'Papel', 'Tesoura']

# escolha do computador
escolha_computador_choice = choice(escolha_computador)

loop = True

while (loop):
    # opções do computador para escolha
    escolha_computador = ['Pedra', 'Papel', 'Tesoura']
    # escolha do computador
    escolha_computador_choice = choice(escolha_computador)
    print('Eu escolhi minha jogada, escolha a sua humano!')

    print('''
    MENU DE OPÇÕES
    [1] - Pedra
    [2] - Papel
    [3] - Tesoura
    [4] - Sair do Jogo
    ''')

    escolha_jogador = str(input('Escolha a sua jogada:'))

    # escolha jogador - Pedra
    if escolha_jogador == '1':
        if escolha_computador == 'Pedra':
            print('ESCOLHA DO COMPUTADOR: ', escolha_computador)
            print('-=' * 20)
            print('RESULTADO: EMPATE')
            print('-=' * 20)
        if escolha_computador == 'Papel':
            print('ESCOLHA DO COMPUTADOR: ', escolha_computador)
            print('-=' * 20)
            print('RESULTADO: Computador Venceu!')
            print('-=' * 20)
        if escolha_computador == 'Tesoura':
            print('ESCOLHA DO COMPUTADOR: ', escolha_computador)
            print('-=' * 20)
            print('RESULTADO: Humano Venceu!')
            print('-=' * 20)
    # escolha jogador - Papel
    elif escolha_jogador == '2':
        if escolha_computador == 'Pedra':
            print('ESCOLHA DO COMPUTADOR: ', escolha_computador)
            print('-=' * 20)
            print('RESULTADO: Humano Venceu!')
            print('-=' * 20)
        if escolha_computador == 'Papel':
            print('ESCOLHA DO COMPUTADOR: ', escolha_computador)
            print('-=' * 20)
            print('RESULTADO: EMPATE')
            print('-=' * 20)
        if escolha_computador == 'Tesoura':
            print('ESCOLHA DO COMPUTADOR: ', escolha_computador)
            print('-=' * 20)
            print('RESULTADO: Computador Venceu!')
            print('-=' * 20)
    # escolha jogador - Tesoura
    elif escolha_jogador == '3':
        if escolha_computador == 'Pedra':
            print('ESCOLHA DO COMPUTADOR: ', escolha_computador)
            print('-=' * 20)
            print('RESULTADO: Computador Venceu!')
            print('-=' * 20)
        if escolha_computador == 'Papel':
            print('ESCOLHA DO COMPUTADOR: ', escolha_computador)
            print('-=' * 20)
            print('RESULTADO: Humano Venceu!')
            print('-=' * 20)
        if escolha_computador == 'Tesoura':
            print('ESCOLHA DO COMPUTADOR: ', escolha_computador)
            print('-=' * 20)
            print('RESULTADO: EMPATE')
            print('-=' * 20)
    # encerra o jogo
    elif escolha_jogador == '4':
        loop = False
    else:
        print('Opção inválida!')
