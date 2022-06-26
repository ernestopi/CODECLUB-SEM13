from random import *

#o programa continua em execução enquanto a variável for verdadeira 'True'
executa = True

adjetivos = ["maravilhoso", "acima da média", "excelente", "confiável", "dedicado", "tolerante", "gentil", "corajoso"]
hobbies = ["andar de bicicleta", "programar", "fazer chá"]

print("Gerador de Cumprimentos")
print("-" * 23)

nome = input("Qual é o seu nome?: ")

print('''
Menu
    c = obter cumprimento
    q = sair
''')

while executa == True:
    menuChoice = input("\n>_").lower()

    # 'C' para um cumprimento
    if menuChoice == 'c':

        print("Aqui está o seu cumprimento", choice(adjetivos), "em", choice(hobbies))
        print("De nada!")
    # 'q' para sair
    elif menuChoice == 'q':
        executa = False

    else:
        print("Escolha uma opção válida!")