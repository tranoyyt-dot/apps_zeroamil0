"""
Crie um dicionario contendo sua ficha de personagem,
com nome, raça, classe, nível, arma, ouro. O dicionario
deve ter um subdicionario com seus atributos: vida, magia,
defesa, ataque e sorte. Cada atributo terá um valor de 1 a 5,
mas o total deve ser no máximo 18 pontos
"""
import random
ficharpg={
    'name': 'Tuzá', 'race':'Elf',
    'level': '2', 'weapon':'bow', 'gold':'1000',
    'attributes':{
        'heal':3,
        'magic':2,
        'defense':3,
        'strong':5,
        'luck':5
    }
}
mapa={
    1: 'monster',
    2: 'exit',
    3: 'treasure',
    4: 'sword',
    5: 'heal',
    6: 'armor'
}
inventario=['bow','gold']
portas=[0,0,0]
while True:
    portas.append(inventario)
    portas[1], portas[2]= random.sample(range(1,6), 2)
    escolha = int(input('Escolha 1, 2 ou 0:'))
    match portas[escolha]:
        case 0:
            if escolha == 0:
                print(inventario)
                continue
        case 1:
            print('BOSS ENCOTRADO!')
            if ('sword' in inventario or
            'heal' in inventario or
            'armor' in inventario):
                print('\nYOU SURVIVED.')
                inventario.append('treasure')
            else:
                print('GAME OVER.')
                break
        case 2:
            print('YOU WIN. TREASURE:')
            print(inventario.count('treasure'))
        case 3:
            print('Você encontrou um tesouro!')
        case 4:
            print('Você encontrou uma espada!')
        case 5:
            print('Você encontrou uma poção!')
        case 6:
            print('Você encontrou uma armadura!')
        case _:
            sala = portas[escolha]
            item = mapa[sala]
            inventario.append(item)
            continue
