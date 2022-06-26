from random import *
print("Gerador de Cumprimentos")
print("-" * 23)

adjetivos = ["maravilhoso", "acima da média", "excelente", "confiável", "dedicado", "tolerante", "gentil", "corajoso"]
hobbies = ["andar de bicicleta", "programar", "fazer chá"]

nome = input("Qual seu nome?: ")
print("Aqui está o seu cumprimento", nome,":" )

#obtém um item aleatório de ambas as listas e adciona-os ao cumprimento
print(nome, "você é", choice(adjetivos), "em",choice(hobbies),".")
print("De nada!")