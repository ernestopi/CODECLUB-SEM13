#Escolhendo os nomes para seus animais.
from random import *

executa = True
nomes_macho = ['Leleco', 'Snow', 'Bingo', 'Tufão', 'Luke']

nomes_femea = ['Leya', 'Lessie', 'Marisa', 'Juju', 'Zara']

print('Gerador de nomes para animais')
print('-'*30)
quant_animais = int(input('Quantos nomes de animais você precisa?:  '))
sexo = input('Qual o sexo do seu animal? (m - macho / f - fêmea) ').strip().lower()
print('''
Menu
c = imprimir nome
a = adicionar nome
d = remover nome
q = sair
''')

while executa == True:

    menuchoice = input('\n>_').lower()
    if menuchoice == 'c' and sexo == 'm':
        for i in range(quant_animais):
            if quant_animais <= 1:
                print(f'Seu animal de estimação deve-se chamar {choice(nomes_macho)}')

            else:
                print(f'Seu animail de estimação deve-se chamar {choice(nomes_macho)}:')
        print('De nada!')

    elif menuchoice == 'c' and sexo == 'f':
        for i in range(quant_animais):
            if quant_animais <= 1:
                print(f'Seu animal de estimação deve-se chamar {choice(nomes_femea)}')

            else:
                print(f'Seu animal de estimação deve-se chamar {choice(nomes_femea)}')
        print('De nada!')

    elif menuchoice == 'a' and sexo == 'm':
        itemtoadd = input('Adicione o nome: ').strip()
        if itemtoadd not in nomes_macho:
            nomes_macho.append(itemtoadd)

    elif menuchoice == 'a' and sexo == 'f':
        itemtoadd = input('Adicione o nome: ').strip()
        if itemtoadd not in nomes_femea:
            nomes_femea.append(itemtoadd)

    elif menuchoice == 'd' and sexo == 'm':
        itemtodelete = input('Insira o nome a ser removido: ').strip()
        if itemtodelete in nomes_macho:
            nomes_macho.remove(itemtodelete)

    elif menuchoice == 'd' and sexo == 'f':
        itemtodelete = input('Insira o nome a ser removido: ').strip()
        if itemtodelete in nomes_femea:
            nomes_femea.remove(itemtodelete)

    elif menuchoice == 'q':
        executa = False

    else:
        print('Insira uma opção válida!')
